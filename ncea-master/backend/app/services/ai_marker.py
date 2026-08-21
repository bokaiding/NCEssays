"""AI Marking Service for NCEA assessments."""

import json
from typing import List, Dict, Any
from sqlalchemy.orm import Session

from ..core.llm_client import llm_client
from ..prompts.system_prompts import NZQA_SENIOR_MARKER_PROMPT
from ..prompts.marking_rubrics import format_rubric_for_prompt, get_rubric
from ..models import GradeType


class AIMarkerService:
    """Service for AI-powered NCEA marking."""
    
    async def mark_response(
        self,
        response: str,
        question: str,
        level: int,
        subject: str,
        standard_code: str = None,
        custom_rubric: str = None
    ) -> Dict[str, Any]:
        """
        Mark a student response using AI.
        
        Returns:
            Dictionary containing grade, feedback, strengths, weaknesses, and next steps
        """
        
        # Get rubric for the standard
        if standard_code:
            rubric_text = format_rubric_for_prompt(standard_code)
            rubric_data = get_rubric(standard_code)
        else:
            rubric_text = "Use general NCEA marking principles for this subject and level."
            rubric_data = {}
        
        # Build the marking prompt
        user_prompt = f"""
CONTEXT:
- Subject: {subject}
- Level: {level}
- Question: {question}
- Student Response: {response}

{rubric_text}

TASK:
Mark this response as an experienced NZQA Senior Marker. Provide:

1. Predicted grade (not_achieved, achieved, merit, or excellence)
2. Confidence score (0.0 to 1.0)
3. Overall feedback explaining the grade
4. List of 3-5 specific strengths using NCEA terminology
5. List of 3-5 specific weaknesses or areas for improvement
6. List of 3-5 actionable next steps to reach the next grade level
7. An exemplar comparison showing what an Excellence response would include

Be specific about what evidence is missing for the next grade level. Use official NCEA terminology throughout.
"""
        
        # Define expected output schema
        output_schema = {
            "predicted_grade": "not_achieved|achieved|merit|excellence",
            "confidence": 0.95,
            "feedback": "string",
            "strengths": ["string"],
            "weaknesses": ["string"],
            "next_steps": ["string"],
            "exemplar_comparison": "string"
        }
        
        # Generate structured response from LLM
        result = await llm_client.generate_structured_response(
            system_prompt=NZQA_SENIOR_MARKER_PROMPT,
            user_prompt=user_prompt,
            output_schema=output_schema,
            temperature=0.3  # Lower temperature for more consistent marking
        )
        
        # Validate and process the result
        return self._process_marking_result(result, rubric_data)
    
    def _process_marking_result(
        self,
        result: Dict[str, Any],
        rubric_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Process and validate the marking result."""
        
        # Handle potential errors
        if "error" in result:
            return {
                "predicted_grade": GradeType.NOT_ACHIEVED,
                "confidence": 0.0,
                "feedback": f"Error during marking: {result['error']}",
                "strengths": [],
                "weaknesses": ["Could not analyze response"],
                "next_steps": ["Please try again"],
                "exemplar_comparison": None
            }
        
        # Map grade string to enum
        grade_str = result.get("predicted_grade", "not_achieved").lower()
        grade_mapping = {
            "not_achieved": GradeType.NOT_ACHIEVED,
            "achieved": GradeType.ACHIEVED,
            "merit": GradeType.MERIT,
            "excellence": GradeType.EXCELLENCE
        }
        predicted_grade = grade_mapping.get(grade_str, GradeType.NOT_ACHIEVED)
        
        # Ensure confidence is within bounds
        confidence = float(result.get("confidence", 0.5))
        confidence = max(0.0, min(1.0, confidence))
        
        return {
            "predicted_grade": predicted_grade,
            "confidence": confidence,
            "feedback": result.get("feedback", ""),
            "strengths": result.get("strengths", []),
            "weaknesses": result.get("weaknesses", []),
            "next_steps": result.get("next_steps", []),
            "exemplar_comparison": result.get("exemplar_comparison")
        }
    
    async def generate_exemplar(
        self,
        question: str,
        level: int,
        subject: str,
        standard_code: str = None
    ) -> str:
        """Generate an Excellence-level exemplar response."""
        
        from ..prompts.system_prompts import EXEMPLAR_GENERATION_PROMPT
        
        rubric_text = format_rubric_for_prompt(standard_code) if standard_code else ""
        
        user_prompt = f"""
Generate an Excellence-level exemplar response for this NCEA question:

Question: {question}
Subject: {subject}
Level: {level}

{rubric_text}

Your exemplar should demonstrate perceptive understanding, comprehensive analysis, and insightful connections. Include annotations explaining why this meets Excellence criteria.
"""
        
        exemplar = await llm_client.generate_completion(
            system_prompt=EXEMPLAR_GENERATION_PROMPT,
            user_prompt=user_prompt,
            temperature=0.7,
            max_tokens=1500
        )
        
        return exemplar
    
    async def break_down_question(
        self,
        question: str,
        subject: str,
        framework: str = "PETAL",
        level: int = None
    ) -> Dict[str, Any]:
        """Break down a complex question into smaller steps using a framework."""
        
        # Always use PETAL or CAPTE for English
        if framework.upper() == "CAPTE":
            from ..prompts.system_prompts import CAPTE_FRAMEWORK_PROMPT as FRAMEWORK_PROMPT
            framework_name = "CAPTE"
        else:
            from ..prompts.system_prompts import PETAL_FRAMEWORK_PROMPT as FRAMEWORK_PROMPT
            framework_name = "PETAL"
        
        level_context = f"Level {level}" if level else ""
        if level == "scholarship":
            level_context = "Scholarship"
        
        user_prompt = f"""
Break down this NCEA English question using the {framework_name} framework:

Question: {question}
{level_context}

Provide:
1. What the question is asking (identify command words and key concepts)
2. How to approach it using {framework_name}
3. Example points for each step of {framework_name}
4. Common mistakes to avoid at this level
5. Tips for achieving Excellence (or Scholarship distinction)
6. Grade-level expectations (what's needed for A/M/E)
"""
        
        breakdown = await llm_client.generate_completion(
            system_prompt=FRAMEWORK_PROMPT,
            user_prompt=user_prompt,
            temperature=0.7,
            max_tokens=1200
        )
        
        return {
            "framework": framework_name,
            "breakdown": breakdown
        }
