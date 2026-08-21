"""LLM Client for interacting with various AI providers."""

import json
from typing import Optional, Dict, Any
from .config import settings


class LLMClient:
    """Unified client for multiple LLM providers."""
    
    def __init__(self):
        self.provider = settings.llm_provider
        self.api_key = settings.llm_api_key
        
        if self.provider == "openai":
            self._init_openai()
        elif self.provider == "anthropic":
            self._init_anthropic()
        elif self.provider == "ollama":
            self._init_ollama()
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")
    
    def _init_openai(self):
        """Initialize OpenAI client."""
        try:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=settings.openai_api_base
            )
            self.model_name = "gpt-4o-mini"  # Cost-effective option
        except ImportError:
            raise ImportError("OpenAI package not installed. Run: pip install openai")
    
    def _init_anthropic(self):
        """Initialize Anthropic client."""
        try:
            from anthropic import Anthropic
            self.client = Anthropic(
                api_key=self.api_key,
                base_url=settings.anthropic_api_base
            )
            self.model_name = "claude-3-haiku-20240307"  # Cost-effective option
        except ImportError:
            raise ImportError("Anthropic package not installed. Run: pip install anthropic")
    
    def _init_ollama(self):
        """Initialize Ollama client (local LLM)."""
        import httpx
        self.base_url = settings.ollama_base_url
        self.model_name = settings.ollama_model
        self.client = httpx.Client(timeout=120.0)
    
    async def generate_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """Generate a completion from the LLM."""
        
        if self.provider == "openai":
            return await self._openai_generate(
                system_prompt, user_prompt, temperature, max_tokens
            )
        elif self.provider == "anthropic":
            return await self._anthropic_generate(
                system_prompt, user_prompt, temperature, max_tokens
            )
        elif self.provider == "ollama":
            return await self._ollama_generate(
                system_prompt, user_prompt, temperature, max_tokens
            )
    
    async def _openai_generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float,
        max_tokens: int
    ) -> str:
        """Generate completion using OpenAI."""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    
    async def _anthropic_generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float,
        max_tokens: int
    ) -> str:
        """Generate completion using Anthropic."""
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.content[0].text
    
    async def _ollama_generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float,
        max_tokens: int
    ) -> str:
        """Generate completion using Ollama (local)."""
        payload = {
            "model": self.model_name,
            "prompt": f"{system_prompt}\n\n{user_prompt}",
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            },
            "stream": False
        }
        
        response = self.client.post(
            f"{self.base_url}/api/generate",
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    
    async def generate_structured_response(
        self,
        system_prompt: str,
        user_prompt: str,
        output_schema: Dict[str, Any],
        temperature: float = 0.3
    ) -> Dict[str, Any]:
        """Generate a structured JSON response."""
        
        # Add instruction for JSON output
        schema_instruction = (
            "\n\nIMPORTANT: Respond ONLY with valid JSON in the following format:\n"
            f"{json.dumps(output_schema, indent=2)}\n"
            "Do not include any other text or explanation."
        )
        
        full_user_prompt = user_prompt + schema_instruction
        
        response_text = await self.generate_completion(
            system_prompt,
            full_user_prompt,
            temperature,
            max_tokens=1500
        )
        
        # Parse JSON response
        try:
            # Extract JSON from response (handle markdown code blocks)
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0]
            elif "```" in response_text:
                json_str = response_text.split("```")[1].split("```")[0]
            else:
                json_str = response_text
            
            return json.loads(json_str.strip())
        except json.JSONDecodeError as e:
            # Return a fallback structure if parsing fails
            return {
                "error": f"Failed to parse JSON response: {str(e)}",
                "raw_response": response_text
            }


# Singleton instance
llm_client = LLMClient()
