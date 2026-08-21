"""API Router for question generation endpoints."""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional, List

from ..database import get_db
from ..schemas import QuestionGenerateRequest, QuestionResponse
from ..services.question_generator import QuestionGeneratorService
from ..core.security import limiter

router = APIRouter(prefix="/api/questions", tags=["questions"])


@router.post("/generate", response_model=QuestionResponse)
@limiter.limit("10/minute")
async def generate_question(
    request: QuestionGenerateRequest,
    db: Session = Depends(get_db)
):
    """
    Generate an NCEA-style practice question.
    
    Supports:
    - English (Unfamiliar Texts, Writing)
    - History
    - Digital Technologies
    - Levels 1, 2, and 3
    """
    
    try:
        generator_service = QuestionGeneratorService()
        
        question_data = await generator_service.generate_question(
            subject=request.subject.value,
            level=request.level.value,
            question_type=request.question_type,
            text_content=request.text_content,
            standard_code=request.standard_code
        )
        
        # In a real implementation, you would save to database here
        # For now, return the generated question
        return QuestionResponse(
            id=0,  # Would be assigned by database
            question_text=question_data["question_text"],
            question_type=question_data["question_type"],
            text_content=question_data["text_content"],
            level=question_data["level"],
            subject=question_data["subject"],
            standard_code=question_data["standard_code"]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Question generation failed: {str(e)}")


@router.post("/generate-batch")
@limiter.limit("5/minute")
async def generate_questions_batch(
    subject: str,
    level: int,
    count: int = 3,
    standard_codes: Optional[List[str]] = None
):
    """Generate multiple practice questions."""
    
    try:
        generator_service = QuestionGeneratorService()
        
        questions = await generator_service.generate_questions_batch(
            subject=subject,
            level=level,
            count=count,
            standard_codes=standard_codes
        )
        
        return {"questions": questions}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch generation failed: {str(e)}")


@router.post("/adapt")
@limiter.limit("10/minute")
async def adapt_question(
    question: str,
    current_level: int,
    target_level: int,
    subject: str
):
    """Adapt a question to a different difficulty level."""
    
    try:
        generator_service = QuestionGeneratorService()
        
        adapted = await generator_service.adapt_question_difficulty(
            question=question,
            current_level=current_level,
            target_level=target_level,
            subject=subject
        )
        
        return {"adapted_question": adapted}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Question adaptation failed: {str(e)}")


@router.post("/follow-up")
@limiter.limit("10/minute")
async def generate_follow_up(
    original_question: str,
    student_response: str,
    subject: str
):
    """Generate follow-up questions based on student response."""
    
    try:
        generator_service = QuestionGeneratorService()
        
        questions = await generator_service.generate_follow_up_questions(
            original_question=original_question,
            student_response=student_response,
            subject=subject
        )
        
        return {"follow_up_questions": questions}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Follow-up generation failed: {str(e)}")
