from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .database import Base


class SubjectType(str, enum.Enum):
    """NCEA English Subject type."""
    ENGLISH = "english"


class LevelType(int, enum.Enum):
    """NCEA Level types including Scholarship."""
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    SCHOLARSHIP = 4  # Special level for Scholarship


class GradeType(str, enum.Enum):
    """NCEA Grade types."""
    NOT_ACHIEVED = "not_achieved"
    ACHIEVED = "achieved"
    MERIT = "merit"
    EXCELLENCE = "excellence"


class User(Base):
    """User model for tracking progress."""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    attempts = relationship("Attempt", back_populates="user")
    progress = relationship("Progress", back_populates="user")


class Standard(Base):
    """NCEA Achievement Standards."""
    __tablename__ = "standards"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)  # e.g., "AS90858"
    name = Column(String)
    subject = Column(Enum(SubjectType))
    level = Column(Enum(LevelType))
    credits = Column(Integer)
    
    # Relationships
    questions = relationship("Question", back_populates="standard")
    attempts = relationship("Attempt", back_populates="standard")


class Question(Base):
    """Generated or stored NCEA questions."""
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    standard_id = Column(Integer, ForeignKey("standards.id"))
    question_text = Column(Text)
    question_type = Column(String)  # e.g., "unfamiliar_text", "essay", "practical"
    text_content = Column(Text, nullable=True)  # For unfamiliar texts
    level = Column(Enum(LevelType))
    subject = Column(Enum(SubjectType))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    standard = relationship("Standard", back_populates="questions")
    attempts = relationship("Attempt", back_populates="question")


class Attempt(Base):
    """Student attempts at answering questions."""
    __tablename__ = "attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    standard_id = Column(Integer, ForeignKey("standards.id"))
    response = Column(Text)
    predicted_grade = Column(Enum(GradeType))
    feedback = Column(Text)
    strengths = Column(Text)
    weaknesses = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="attempts")
    question = relationship("Question", back_populates="attempts")
    standard = relationship("Standard", back_populates="attempts")


class Progress(Base):
    """User progress tracking by standard."""
    __tablename__ = "progress"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    standard_id = Column(Integer, ForeignKey("standards.id"))
    confidence_score = Column(Float, default=0.0)  # 0-100
    attempts_count = Column(Integer, default=0)
    last_attempt_date = Column(DateTime(timezone=True))
    
    # Relationships
    user = relationship("User", back_populates="progress")
    standard = relationship("Standard")
