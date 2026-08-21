"""API Router for user dashboard endpoints."""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from typing import List
from datetime import datetime

from ..database import get_db
from ..models import User, Attempt, Progress, Standard, Question, GradeType
from ..schemas import DashboardResponse, ProgressSummary, AttemptRecord
from ..core.security import limiter

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/", response_model=DashboardResponse)
@limiter.limit("30/minute")
async def get_dashboard(
    user_id: int = 1,  # In real app, get from authentication
    db: Session = Depends(get_db)
):
    """Get user dashboard with progress overview."""
    
    try:
        # Get total attempts
        total_attempts = db.query(Attempt).filter(
            Attempt.user_id == user_id
        ).count()
        
        # Get progress by standard
        progress_records = db.query(Progress).filter(
            Progress.user_id == user_id
        ).options(
            joinedload(Progress.standard)
        ).all()
        
        standards_summary = []
        for prog in progress_records:
            standard = prog.standard
            if standard:
                # Get grade distribution for this standard
                grade_dist_query = db.query(
                    Attempt.predicted_grade,
                    func.count(Attempt.id).label('count')
                ).filter(
                    Attempt.user_id == user_id,
                    Attempt.standard_id == standard.id
                ).group_by(Attempt.predicted_grade).all()
                
                grade_distribution = {
                    grade.value if grade else "not_attempted": count
                    for grade, count in grade_dist_query
                }
                
                standards_summary.append(ProgressSummary(
                    standard_code=standard.code,
                    standard_name=standard.name,
                    subject=standard.subject,
                    level=standard.level,
                    confidence_score=prog.confidence_score,
                    attempts_count=prog.attempts_count,
                    last_attempt_date=prog.last_attempt_date,
                    grade_distribution=grade_distribution
                ))
        
        # Get recent attempts
        recent_attempts = db.query(Attempt).filter(
            Attempt.user_id == user_id
        ).options(
            joinedload(Attempt.question),
            joinedload(Attempt.standard)
        ).order_by(
            Attempt.created_at.desc()
        ).limit(5).all()
        
        recent_records = [
            AttemptRecord(
                id=attempt.id,
                question_text=attempt.question.question_text if attempt.question else "",
                response=attempt.response,
                predicted_grade=attempt.predicted_grade,
                feedback=attempt.feedback,
                created_at=attempt.created_at,
                standard_code=attempt.standard.code if attempt.standard else ""
            )
            for attempt in recent_attempts
        ]
        
        # Calculate subject summaries
        subjects = {}
        for std_summary in standards_summary:
            subj = std_summary.subject.value
            if subj not in subjects:
                subjects[subj] = {
                    "total_attempts": 0,
                    "average_confidence": 0.0,
                    "standards_count": 0
                }
            
            # Get attempts for this subject
            subject_attempts = db.query(Attempt).join(Question).filter(
                Attempt.user_id == user_id,
                Question.subject == std_summary.subject
            ).count()
            
            subjects[subj]["total_attempts"] += subject_attempts
            subjects[subj]["standards_count"] += 1
        
        # Calculate average confidence per subject
        for subj in subjects:
            subj_progress = db.query(Progress).join(Standard).filter(
                Progress.user_id == user_id,
                Standard.subject == subj
            ).all()
            
            if subj_progress:
                avg_confidence = sum(p.confidence_score for p in subj_progress) / len(subj_progress)
                subjects[subj]["average_confidence"] = round(avg_confidence, 2)
        
        return DashboardResponse(
            total_attempts=total_attempts,
            subjects=subjects,
            standards=standards_summary,
            recent_attempts=recent_records
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dashboard retrieval failed: {str(e)}")


@router.get("/attempts", response_model=List[AttemptRecord])
async def get_attempt_history(
    user_id: int = 1,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get user's attempt history."""
    
    attempts = db.query(Attempt).filter(
        Attempt.user_id == user_id
    ).options(
        joinedload(Attempt.question),
        joinedload(Attempt.standard)
    ).order_by(
        Attempt.created_at.desc()
    ).limit(limit).all()
    
    return [
        AttemptRecord(
            id=attempt.id,
            question_text=attempt.question.question_text if attempt.question else "",
            response=attempt.response,
            predicted_grade=attempt.predicted_grade,
            feedback=attempt.feedback,
            created_at=attempt.created_at,
            standard_code=attempt.standard.code if attempt.standard else ""
        )
        for attempt in attempts
    ]


@router.get("/progress/{standard_code}")
async def get_standard_progress(
    standard_code: str,
    user_id: int = 1,
    db: Session = Depends(get_db)
):
    """Get detailed progress for a specific standard."""
    
    standard = db.query(Standard).filter(
        Standard.code == standard_code
    ).first()
    
    if not standard:
        raise HTTPException(status_code=404, detail="Standard not found")
    
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.standard_id == standard.id
    ).first()
    
    if not progress:
        return {
            "standard": standard.code,
            "name": standard.name,
            "confidence_score": 0.0,
            "attempts_count": 0,
            "grade_distribution": {}
        }
    
    # Get grade distribution
    grade_dist_query = db.query(
        Attempt.predicted_grade,
        func.count(Attempt.id).label('count')
    ).filter(
        Attempt.user_id == user_id,
        Attempt.standard_id == standard.id
    ).group_by(Attempt.predicted_grade).all()
    
    grade_distribution = {
        grade.value if grade else "not_attempted": count
        for grade, count in grade_dist_query
    }
    
    return {
        "standard": standard.code,
        "name": standard.name,
        "confidence_score": progress.confidence_score,
        "attempts_count": progress.attempts_count,
        "last_attempt": progress.last_attempt_date,
        "grade_distribution": grade_distribution
    }
