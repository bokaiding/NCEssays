"""Question Generation Service for NCEA practice questions."""

from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session

from ..core.llm_client import llm_client
from ..prompts.system_prompts import QUESTION_GENERATION_PROMPT
from ..prompts.marking_rubrics import format_rubric_for_prompt


class QuestionGeneratorService:
    """Service for generating NCEA-style practice questions."""
    
    async def generate_question(
        self,
        subject: str,
        level: int,
        question_type: str = "essay",
        text_content: Optional[str] = None,
        standard_code: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate an NCEA-style practice question.
        
        Args:
            subject: Subject area (english, history, digital_technologies)
            level: NCEA level (1, 2, or 3)
            question_type: Type of question (essay, unfamiliar_text, practical)
            text_content: Optional text for unfamiliar texts
            standard_code: Optional achievement standard code
            
        Returns:
            Dictionary containing question details
        """
        
        # Get rubric if standard code provided
        rubric_text = format_rubric_for_prompt(standard_code) if standard_code else ""
        
        # Build the generation prompt
        user_prompt = f"""
Generate an NCEA practice question with these specifications:

- Subject: {subject}
- Level: {level}
- Question Type: {question_type}
- Achievement Standard: {standard_code if standard_code else "General"}

{rubric_text}

{"TEXT TO ANALYZE:\n" + text_content if text_content else ""}

Requirements:
1. Use authentic NCEA wording and formatting
2. Include clear instructions and context
3. Ensure the question allows students to demonstrate skills at all grade levels (A/M/E)
4. Include time recommendations
5. Provide the achievement standard code and name if applicable

For Unfamiliar Texts: Include analysis questions about language features
For History: Include source analysis or causal reasoning questions
For Digital Technologies: Include scenario-based technical questions
"""
        
        question_text = await llm_client.generate_completion(
            system_prompt=QUESTION_GENERATION_PROMPT,
            user_prompt=user_prompt,
            temperature=0.7,
            max_tokens=800
        )
        
        return {
            "question_text": question_text,
            "subject": subject,
            "level": level,
            "question_type": question_type,
            "text_content": text_content,
            "standard_code": standard_code
        }
    
    async def generate_questions_batch(
        self,
        subject: str,
        level: int,
        count: int = 3,
        standard_codes: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Generate multiple practice questions."""
        
        questions = []
        
        # If standard codes provided, generate one per standard
        if standard_codes:
            for code in standard_codes[:count]:
                question = await self.generate_question(
                    subject=subject,
                    level=level,
                    standard_code=code
                )
                questions.append(question)
        else:
            # Generate varied questions
            for i in range(count):
                question = await self.generate_question(
                    subject=subject,
                    level=level,
                    question_type="essay" if i == 0 else "unfamiliar_text" if i == 1 else "practical"
                )
                questions.append(question)
        
        return questions
    
    async def adapt_question_difficulty(
        self,
        question: str,
        current_level: int,
        target_level: int,
        subject: str
    ) -> str:
        """Adapt a question to a different difficulty level."""
        
        user_prompt = f"""
Adapt this NCEA question from Level {current_level} to Level {target_level}:

Original Question:
{question}

Subject: {subject}

Make the question appropriately challenging for Level {target_level}:
- For higher levels: Require more sophisticated analysis, evaluation, and synthesis
- For lower levels: Focus on identification, description, and basic explanation

Maintain the core concept but adjust cognitive demands to match the target level.
"""
        
        adapted_question = await llm_client.generate_completion(
            system_prompt=QUESTION_GENERATION_PROMPT,
            user_prompt=user_prompt,
            temperature=0.7,
            max_tokens=600
        )
        
        return adapted_question
    
    async def generate_follow_up_questions(
        self,
        original_question: str,
        student_response: str,
        subject: str
    ) -> List[str]:
        """Generate follow-up questions based on student response."""
        
        user_prompt = f"""
Based on this NCEA question and student response, generate 2-3 follow-up questions to deepen understanding:

Original Question: {original_question}
Student Response: {student_response}
Subject: {subject}

Follow-up questions should:
1. Address gaps or weaknesses in the response
2. Encourage deeper analysis or evaluation
3. Help student progress toward the next grade level
4. Be specific and actionable

Return each question on a separate line.
"""
        
        response_text = await llm_client.generate_completion(
            system_prompt=QUESTION_GENERATION_PROMPT,
            user_prompt=user_prompt,
            temperature=0.7,
            max_tokens=500
        )
        
        # Parse questions from response
        questions = [
            q.strip() for q in response_text.split('\n') 
            if q.strip() and any(c.isalpha() for c in q)
        ]
        
        return questions[:3]  # Return max 3 questions
