"""API Router for AI marking endpoints."""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional

from ..database import get_db
from ..schemas import MarkingRequest, MarkingResponse
from ..services.ai_marker import AIMarkerService
from ..core.security import limiter

router = APIRouter(prefix="/api/mark", tags=["marking"])


@router.post("/", response_model=MarkingResponse)
@limiter.limit("10/minute")
async def mark_response(
    request: MarkingRequest,
    db: Session = Depends(get_db)
):
    """
    Mark a student response using AI.
    
    This endpoint takes a student's response and returns:
    - Predicted grade (Not Achieved, Achieved, Merit, Excellence)
    - Confidence score
    - Detailed feedback
    - Strengths and weaknesses
    - Next steps for improvement
    - Exemplar comparison
    """
    
    try:
        marker_service = AIMarkerService()
        
        result = await marker_service.mark_response(
            response=request.response,
            question=request.question,
            level=request.level.value,
            subject=request.subject.value,
            standard_code=request.standard_code,
            custom_rubric=request.marking_schedule
        )
        
        return MarkingResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Marking failed: {str(e)}")


@router.post("/exemplar")
@limiter.limit("5/minute")
async def generate_exemplar(
    question: str,
    level: int,
    subject: str,
    standard_code: Optional[str] = None
):
    """Generate an Excellence-level exemplar response."""
    
    try:
        marker_service = AIMarkerService()
        
        exemplar = await marker_service.generate_exemplar(
            question=question,
            level=level,
            subject=subject,
            standard_code=standard_code
        )
        
        return {"exemplar": exemplar}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exemplar generation failed: {str(e)}")


@router.post("/breakdown")
@limiter.limit("10/minute")
async def break_down_question(
    question: str,
    subject: str,
    framework: Optional[str] = "PETAL"
):
    """Break down a complex question into smaller steps."""
    
    try:
        marker_service = AIMarkerService()
        
        breakdown = await marker_service.break_down_question(
            question=question,
            subject=subject,
            framework=framework
        )
        
        return breakdown
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Question breakdown failed: {str(e)}")
