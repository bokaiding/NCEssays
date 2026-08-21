# NCEA Master - Project Structure

```
ncea-master/
├── backend/                    # Python FastAPI Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI application entry point
│   │   ├── config.py          # Configuration and environment variables
│   │   ├── database.py        # Database connection setup
│   │   ├── models.py          # SQLAlchemy database models
│   │   ├── schemas.py         # Pydantic schemas for validation
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── security.py    # API key management, rate limiting
│   │   │   └── llm_client.py  # LLM API client (OpenAI/Anthropic/Ollama)
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── questions.py   # Question generation endpoints
│   │   │   ├── marking.py     # AI marking endpoints
│   │   │   ├── dashboard.py   # User dashboard endpoints
│   │   │   └── research.py    # Research/search endpoints
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── question_generator.py  # Question generation logic
│   │   │   ├── ai_marker.py           # AI marking logic
│   │   │   ├── progress_tracker.py    # Progress tracking logic
│   │   │   └── research_service.py    # Research/search logic
│   │   └── prompts/
│   │       ├── __init__.py
│   │       ├── system_prompts.py      # System prompts for AI
│   │       └── marking_rubrics.py     # NCEA marking rubrics
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── frontend/                   # Next.js React Frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx       # Landing page
│   │   │   ├── dashboard/
│   │   │   │   └── page.tsx   # User dashboard
│   │   │   ├── practice/
│   │   │   │   └── page.tsx   # Practice/question interface
│   │   │   ├── marking/
│   │   │   │   └── page.tsx   # AI marking interface
│   │   │   └── research/
│   │   │       └── page.tsx   # Research tool
│   │   ├── components/
│   │   │   ├── ui/            # Reusable UI components
│   │   │   ├── QuestionGenerator.tsx
│   │   │   ├── AIMarker.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── TextUploader.tsx
│   │   │   └── ExemplarViewer.tsx
│   │   ├── lib/
│   │   │   ├── api.ts         # API client
│   │   │   └── utils.ts       # Utility functions
│   │   ├── hooks/
│   │   │   └── usePractice.ts
│   │   └── types/
│   │       └── index.ts       # TypeScript types
│   ├── public/
│   ├── package.json
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   └── .env.local.example
│
├── database/
│   └── migrations/            # Database migration files
│
├── README.md                  # Main project documentation
└── .gitignore
```

## Quick Start

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your LLM API key
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

### Database Setup
```bash
# Install PostgreSQL
# Create database: ncea_master
# Run migrations
```

## Environment Variables

### Backend (.env)
```
LLM_API_KEY=your_api_key_here
LLM_PROVIDER=openai  # or anthropic, ollama
DATABASE_URL=postgresql://user:password@localhost:5432/ncea_master
RATE_LIMIT_PER_MINUTE=10
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Key Features

1. **Question Generation**: Generates NCEA-style questions for English, History, and Digital Technologies
2. **AI Marking**: Provides NZQA-aligned marking with Achieved/Merit/Excellence grades
3. **User Dashboard**: Tracks progress by standard with confidence scores
4. **Research Tool**: Integrated search for context and exemplars
5. **Study Mode**: Breaks down complex questions using PETAL/IDEAR frameworks
6. **Exemplar Viewer**: Compare work against AI-generated excellence responses

## NCEA Alignment

The system is designed to align with NZQA marking schedules and assessment standards:
- English: AS90858 (Level 1), AS91107 (Level 2), AS91472 (Level 3)
- History: Various achievement standards across levels
- Digital Technologies: AS91896, AS91897, AS91898 (Level 1)

All AI prompts are engineered to act as "NZQA Senior Markers" and reference specific criteria from official NZQA documents.
