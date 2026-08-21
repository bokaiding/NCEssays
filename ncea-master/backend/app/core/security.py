"""Rate limiting and security utilities."""

from slowapi import Limiter
from slowapi.util import get_remote_address
from .config import settings

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)


def get_rate_limit() -> str:
    """Get rate limit string from settings."""
    return f"{settings.rate_limit_per_minute}/minute"
