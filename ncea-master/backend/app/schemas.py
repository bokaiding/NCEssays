from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .models import SubjectType, LevelType, GradeType


# Question Generation Schemas
class QuestionGenerateRequest(BaseModel):
    """Request schema for generating questions."""
    subject: SubjectType
    level: LevelType
    question_type: str = "essay"  # essay, unfamiliar_text, practical
    text_content: Optional[str] = None  # For unfamiliar texts
    standard_code: Optional[str] = None


class QuestionResponse(BaseModel):
    """Response schema for generated questions."""
    id: int
    question_text: str
    question_type: str
    text_content: Optional[str]
    level: LevelType
    subject: SubjectType
    standard_code: Optional[str]


# AI Marking Schemas
class MarkingRequest(BaseModel):
    """Request schema for AI marking."""
    response: str = Field(..., min_length=10, description="Student's answer")
    question: str = Field(..., description="Original question")
    standard_code: Optional[str] = None
    level: LevelType
    subject: SubjectType
    marking_schedule: Optional[str] = None  # Custom rubric


class FeedbackItem(BaseModel):
    """Individual feedback item."""
    criterion: str
    comment: str
    grade_level: str


class MarkingResponse(BaseModel):
    """Response schema for AI marking results."""
    predicted_grade: GradeType
    confidence: float = Field(..., ge=0.0, le=1.0)
    feedback: str
    strengths: List[str]
    weaknesses: List[str]
    next_steps: List[str]
    exemplar_comparison: Optional[str] = None


# Dashboard Schemas
class ProgressSummary(BaseModel):
    """Progress summary for a standard."""
    standard_code: str
    standard_name: str
    subject: SubjectType
    level: LevelType
    confidence_score: float
    attempts_count: int
    last_attempt_date: Optional[datetime]
    grade_distribution: dict


class DashboardResponse(BaseModel):
    """User dashboard response."""
    total_attempts: int
    subjects: dict
    standards: List[ProgressSummary]
    recent_attempts: List[dict]


# Attempt History Schema
class AttemptRecord(BaseModel):
    """Record of a past attempt."""
    id: int
    question_text: str
    response: str
    predicted_grade: GradeType
    feedback: str
    created_at: datetime
    standard_code: str
