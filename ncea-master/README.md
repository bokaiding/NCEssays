# NCEA Master - AI-Powered NCEA Practice Platform

A comprehensive web-based platform for generating, practicing, and receiving AI-marked feedback on NCEA-style questions for English, History, and Digital Technologies across Levels 1-3.

## 🎯 Features

### Core Features
- **Question Generation Engine**: Generate authentic NCEA-style questions aligned with achievement standards
- **AI Marking System**: Get instant feedback using NZQA marking schedules (Achieved/Merit/Excellence)
- **User Dashboard**: Track progress by standard with confidence scores
- **Research Tools**: Integrated Wikipedia search and curated NCEA resources

### Additional Features
- **Study Mode**: Break down complex questions using PETAL (English) or IDEAR (Digital Technologies) frameworks
- **Exemplar Viewer**: Compare work against AI-generated Excellence-level responses
- **Text Upload**: For Unfamiliar Texts, paste or upload texts for CAPTE/PETAL-style analysis
- **Rate Limiting**: Prevents API abuse with configurable rate limits

## 🏗️ Technical Architecture

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **LLM Integration**: Support for OpenAI, Anthropic, or Ollama (local LLM)
- **Security**: Server-side API key management, rate limiting with SlowAPI
- **CORS**: Configured for frontend integration

### Frontend
- **Framework**: Next.js 14 (React) with TypeScript
- **Styling**: Tailwind CSS
- **API Client**: Axios with typed endpoints
- **Components**: Reusable UI components for question generation and marking

## 📁 Project Structure

```
ncea-master/
├── backend/                    # Python FastAPI Backend
│   ├── app/
│   │   ├── config.py          # Environment configuration
│   │   ├── database.py        # Database connection
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── schemas.py         # Pydantic schemas
│   │   ├── main.py            # FastAPI application
│   │   ├── core/
│   │   │   ├── security.py    # Rate limiting
│   │   │   └── llm_client.py  # LLM API client
│   │   ├── routers/
│   │   │   ├── questions.py   # Question generation endpoints
│   │   │   ├── marking.py     # AI marking endpoints
│   │   │   ├── dashboard.py   # Dashboard endpoints
│   │   │   └── research.py    # Research/search endpoints
│   │   ├── services/
│   │   │   ├── ai_marker.py   # AI marking service
│   │   │   └── question_generator.py  # Question generation service
│   │   └── prompts/
│   │       ├── system_prompts.py      # AI system prompts
│   │       └── marking_rubrics.py     # NCEA rubrics
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/                   # Next.js Frontend
│   ├── src/
│   │   ├── app/               # Next.js App Router pages
│   │   ├── components/        # React components
│   │   │   ├── QuestionGenerator.tsx
│   │   │   └── AIMarker.tsx
│   │   └── lib/
│   │       └── api.ts         # API client
│   ├── package.json
│   └── tailwind.config.js
│
└── database/migrations/        # Database migrations
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL 13+
- LLM API key (OpenAI, Anthropic, or Ollama for local)

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Edit .env with your configuration
# Required: LLM_API_KEY, DATABASE_URL
```

**Configure `.env`:**
```env
# Required
LLM_API_KEY=your_api_key_here
LLM_PROVIDER=openai  # or anthropic, ollama
DATABASE_URL=postgresql://user:password@localhost:5432/ncea_master

# Optional
RATE_LIMIT_PER_MINUTE=10
OLLAMA_BASE_URL=http://localhost:11434  # Only if using Ollama
```

**Setup Database:**
```bash
# Create PostgreSQL database
createdb ncea_master

# Or using psql
psql -U postgres
CREATE DATABASE ncea_master;
\q

# Tables will be created automatically on first run
```

**Run Backend:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/docs` for API documentation.

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.local.example .env.local

# Run development server
npm run dev
```

Visit `http://localhost:3000` to access the application.

## 🔐 Security & API Key Management

**IMPORTANT**: The LLM API key is stored server-side only and never exposed to the client.

### Supported LLM Providers

1. **OpenAI** (Recommended for production)
   ```env
   LLM_PROVIDER=openai
   LLM_API_KEY=sk-...
   ```
   Uses `gpt-4o-mini` for cost-effective operations

2. **Anthropic**
   ```env
   LLM_PROVIDER=anthropic
   LLM_API_KEY=sk-ant-...
   ```
   Uses `claude-3-haiku-20240307`

3. **Ollama** (Local, free, privacy-focused)
   ```env
   LLM_PROVIDER=ollama
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_MODEL=llama2
   ```
   Requires Ollama installed locally

### Rate Limiting
- Default: 10 requests per minute per endpoint
- Configurable via `RATE_LIMIT_PER_MINUTE` in `.env`
- Prevents API key abuse

## 📚 NCEA Alignment

### Achievement Standards Supported

**English:**
- Level 1: AS90858 (Unfamiliar Text)
- Level 2: AS91107 (Written Texts)
- Level 3: AS91472 (Visual/Oral Texts)

**History:**
- Level 1: AS91003 (Perspectives & Contexts)
- Level 2: AS91233 (Historical Events)
- Level 3: AS91434 (Historical Interpretations)

**Digital Technologies:**
- Level 1: AS91896 (Algorithms)
- Level 2: AS91897 (Advanced Processes)
- Level 3: AS91906 (Complex Processes)

### Marking Rubrics

The AI uses official NZQA terminology:
- **Not Achieved**: Does not meet criteria
- **Achieved**: Basic understanding, addresses question
- **Merit**: In-depth understanding, justified analysis
- **Excellence**: Perceptive understanding, comprehensive analysis

System prompts force the AI to act as a "NZQA Senior Marker" with 10+ years experience.

## 🛠️ API Endpoints

### Question Generation
- `POST /api/questions/generate` - Generate single question
- `POST /api/questions/generate-batch` - Generate multiple questions
- `POST /api/questions/adapt` - Adapt difficulty level
- `POST /api/questions/follow-up` - Generate follow-up questions

### AI Marking
- `POST /api/mark/` - Mark student response
- `POST /api/mark/exemplar` - Generate excellence exemplar
- `POST /api/mark/breakdown` - Break down question (Study Mode)

### Dashboard
- `GET /api/dashboard/` - Get user dashboard
- `GET /api/dashboard/attempts` - Get attempt history
- `GET /api/dashboard/progress/{standard_code}` - Get standard progress

### Research
- `GET /api/research/search?query=` - Search Wikipedia
- `GET /api/research/summary/{title}` - Get Wikipedia summary
- `GET /api/research/ncea-resources` - Get NCEA resources

## 🧪 Testing

### Backend Testing
```bash
cd backend
pytest  # When tests are added
```

### Frontend Testing
```bash
cd frontend
npm test  # When tests are added
```

## 📦 Deployment

### Backend (Production)

**Using Docker:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Using Gunicorn:**
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend (Production)

```bash
cd frontend
npm run build
npm start
```

**Deploy to Vercel:**
```bash
npm i -g vercel
vercel deploy
```

### Environment Variables (Production)

Set these in your hosting platform:
- `LLM_API_KEY`: Your API key
- `DATABASE_URL`: Production database URL
- `NEXT_PUBLIC_API_URL`: Backend API URL

## 💰 Cost Management

### Estimated API Costs (OpenAI)
- Question generation: ~$0.01 per question (gpt-4o-mini)
- AI marking: ~$0.02 per marking (gpt-4o-mini)
- Exemplar generation: ~$0.03 per exemplar

**With 100 students practicing daily:**
- ~$50-100/month depending on usage

### Cost Reduction Strategies
1. Use Ollama with local LLM (free, but requires GPU)
2. Implement caching for common questions
3. Use smaller models for simpler tasks
4. Set strict rate limits

## 🔧 Customization

### Adding New Achievement Standards

Edit `backend/app/prompts/marking_rubrics.py`:

```python
MARKING_RUBRICS = {
    "ASXXXXX": {
        "name": "Standard Name",
        "subject": "english",
        "level": 1,
        "criteria": {
            "not_achieved": "...",
            "achieved": ["...", "..."],
            "merit": ["...", "..."],
            "excellence": ["...", "..."]
        }
    }
}
```

### Customizing Prompts

Edit `backend/app/prompts/system_prompts.py` to modify:
- NZQA marker persona
- PETAL/IDEAR framework instructions
- Question generation guidelines
- Exemplar generation rules

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is designed for educational purposes. Ensure compliance with NZQA copyright when using official materials.

## ⚠️ Disclaimer

This platform uses AI to provide practice and feedback. While aligned with NZQA standards:
- AI marking is predictive, not official
- Always verify with official NZQA resources
- Do not use for actual assessment decisions
- Students should consult teachers for formal guidance

## 📞 Support

For issues or questions:
1. Check API documentation at `/docs`
2. Review example prompts in `backend/app/prompts/`
3. Ensure environment variables are correctly set
4. Check rate limit settings if experiencing throttling

## 🎓 Educational Best Practices

### For Teachers
- Use as supplementary practice tool
- Review AI feedback with students
- Customize rubrics for specific cohorts
- Monitor student progress via dashboard

### For Students
- Use feedback to identify gaps
- Compare responses with exemplars
- Practice regularly across standards
- Track confidence score improvements

---

Built with ❤️ for New Zealand students achieving NCEA success.
