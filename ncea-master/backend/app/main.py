"""NCEA Master - FastAPI Backend Application."""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.exception_handlers import rate_limit_exceeded_handler

from .config import settings
from .database import engine, Base
from .core.security import limiter
from .routers import questions, marking, dashboard, research

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="NCEA Master API",
    description="AI-powered NCEA practice and marking platform",
    version="1.0.0"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js dev server
        "https://nceamaster.nz",  # Production domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

# Include routers
app.include_router(questions.router)
app.include_router(marking.router)
app.include_router(dashboard.router)
app.include_router(research.router)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "NCEA Master API",
        "version": "1.0.0",
        "description": "AI-powered NCEA practice and marking platform",
        "features": [
            "Question Generation",
            "AI Marking with NZQA alignment",
            "Progress Tracking",
            "Research Tools"
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "database": "connected",
        "llm_provider": settings.llm_provider
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize application on startup."""
    print(f"Starting NCEA Master API with {settings.llm_provider} LLM provider")
    print(f"Rate limit: {settings.rate_limit_per_minute} requests per minute")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Clean up on shutdown."""
    print("Shutting down NCEA Master API")
