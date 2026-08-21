# NCEA Master - AI-Powered NCEA English Practice Platform

A comprehensive web-based platform for generating, practicing, and receiving AI-marked feedback on **NCEA English** questions across Levels 1, 2, 3, and Scholarship.

## 🎯 Features

### Core Features
- **Question Generation Engine**: Generate authentic NCEA English-style questions aligned with achievement standards
- **AI Marking System**: Get instant feedback using NZQA marking schedules (Not Achieved/Achieved/Merit/Excellence)
- **User Dashboard**: Track progress by standard with confidence scores
- **Study Mode**: Break down complex questions using PETAL or CAPTE frameworks

### Additional Features
- **Exemplar Viewer**: Compare work against AI-generated Excellence-level responses
- **Text Upload**: For Unfamiliar Texts, paste or upload texts for CAPTE/PETAL-style analysis
- **Rate Limiting**: Prevents API abuse with configurable rate limits
- **Scholarship Support**: Specialized prompts and rubrics for Scholarship English

## 📚 NCEA English Achievement Standards Supported

### Level 1 English
- **AS90858** - Unfamiliar Text (4 credits)
- **AS90856** - Write selected texts (6 credits)
- **AS90857** - Deliver an oral presentation (4 credits)

### Level 2 English
- **AS91107** - Respond critically to specified aspect(s) of studied written text(s) (4 credits)
- **AS91108** - Respond critically to aspects of unfamiliar written text(s) (4 credits)
- **AS91106** - Form and deliver an oral presentation (4 credits)
- **AS91105** - Write a selection of crafted and controlled writing (6 credits)

### Level 3 English
- **AS91472** - Respond critically to significant aspects of visual and/or oral texts (4 credits)
- **AS91473** - Respond critically to specified aspect(s) of studied written text(s) (4 credits)
- **AS91476** - Create a fluent text (6 credits)
- **AS91477** - Respond critically to ideas in literary texts (4 credits)

### Scholarship English
- **SCHOLARSHIP_ENGLISH** - Performance Standard (awards scholarship status)
- Requires demonstration of high-level critical thinking, originality, and sophisticated synthesis

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

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL 13+
- LLM API key (OpenAI, Anthropic, or Ollama for local)

### 1. Backend Setup

```bash
cd ncea-master/backend

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
```

**Run Backend:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/docs` for API documentation.

### 2. Frontend Setup

```bash
cd ncea-master/frontend

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

## 📝 NCEA English Marking Alignment

The AI uses official NZQA terminology and marking criteria:

### Grade Descriptors
- **Not Achieved**: Does not meet the criteria for Achieved
- **Achieved**: Demonstrates basic understanding, addresses the question with supporting evidence
- **Merit**: Shows in-depth understanding with justified analysis and integrated evidence
- **Excellence**: Displays perceptive understanding with comprehensive, insightful analysis and critical evaluation

### Scholarship English Expectations
- Demonstration of high-level critical thinking
- Originality and independence of thought
- Integration of multiple texts and perspectives
- Polished, precise, and compelling writing
- Outstanding critical thinking with original insights for Excellence

### Frameworks Used
- **PETAL**: Point, Evidence, Technique, Analysis, Link (for essay paragraphs)
- **CAPTE**: Context, Audience/Purpose, Point, Technique, Effect (for unfamiliar texts)

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

## 📄 License

This project is designed for educational purposes. Ensure compliance with NZQA copyright when using official materials.

## ⚠️ Disclaimer

This platform uses AI to provide practice and feedback. While aligned with NZQA standards:
- AI marking is predictive, not official
- Always verify with official NZQA resources
- Do not use for actual assessment decisions
- Students should consult teachers for formal guidance

---

Built with ❤️ for New Zealand students achieving NCEA English success.

## 👥 How to Use This Application (For Students & Teachers)

If you're new to the platform, start here! This section explains how to actually use the app once it's running.

### 🎯 For Students: Your Study Workflow

#### Step 1: Choose Your Focus
When you open the app at `http://localhost:3000`:
1. **Select your Level** (1, 2, 3, or Scholarship) from the dropdown
2. **Choose a Standard** - Pick the achievement standard you want to practice:
   - *Unfamiliar Texts* → AS90858 (L1), AS91108 (L2), AS91473 (L3)
   - *Written Texts* → AS91107 (L2), AS91473 (L3)
   - *Writing Portfolio* → AS90856 (L1), AS91105 (L2), AS91476 (L3)
   - *Scholarship* → Select "Scholarship" level

#### Step 2: Generate a Practice Question
1. Click **"Generate Question"** in the navigation
2. **For Unfamiliar Texts**:
   - Paste an article, poem, or speech OR click "Use Sample Text"
   - Choose your framework: **PETAL** (paragraph focus) or **CAPTE** (holistic analysis)
3. **For Writing Tasks**:
   - Select genre (Creative, Formal Essay, etc.)
   - Enter a theme or topic
4. Click **"Generate"** - The AI creates an authentic NCEA-style question

#### Step 3: Write Your Response
- Type your answer in the text editor
- Treat it like a real exam - manage your time!
- Aim for depth appropriate to your level:
  - **Level 1**: 2-3 well-developed paragraphs
  - **Level 2**: 3-4 paragraphs with justified analysis
  - **Level 3/Scholarship**: 4+ paragraphs with perceptive insights

#### Step 4: Get AI Marking
1. Click **"Submit for Marking"**
2. Wait 5-10 seconds while the AI marks your work
3. Review your results:
   - **Predicted Grade** (Not Achieved/Achieved/Merit/Excellence)
   - **Why** you got that grade (with NZQA terminology)
   - **Strengths** - What you did well
   - **Next Steps** - Specific advice to reach the next grade
   - **Exemplar** - Click "View Excellence Response" to see a model answer

#### Step 5: Learn & Improve
- Compare your response to the exemplar
- Note the vocabulary and structure differences
- Try again with the feedback in mind
- Track your **Confidence Score** improving on the dashboard

---

### 🍎 For Teachers: Classroom Integration

#### Setting Up for Your Class
1. **Create Accounts** for students (if authentication is enabled)
2. **Assign Standards** based on your teaching plan
3. **Monitor Progress** via the dashboard analytics

#### Lesson Ideas
- **In-Class Practice**: Generate questions during lessons, students write responses
- **Homework**: Students complete practice at home, review feedback next class
- **Peer Comparison**: Have students compare their responses with AI exemplars
- **Targeted Intervention**: Use dashboard data to identify struggling students

#### Customization
- Adjust rate limits in `.env` for classroom use (`RATE_LIMIT_PER_MINUTE=30`)
- Use local Ollama models to avoid API costs for large classes
- Export student progress reports for assessment evidence

---

### 💡 Pro Tips for Best Results

| If you want to... | Do this... |
|------------------|------------|
| **Improve from A to M** | Focus on explaining HOW techniques create meaning, not just identifying them |
| **Improve from M to E** | Make connections to wider contexts, authorial intent, or universal themes |
| **Practice Unfamiliar Texts** | Use CAPTE framework to ensure you cover Context and Audience/Purpose |
| **Write Better Essays** | Use PETAL structure for each paragraph |
| **Prepare for Scholarship** | Challenge yourself with abstract questions and focus on originality |
| **Save Money on API** | Use Ollama (local LLM) instead of OpenAI - free but needs good computer |

---

### ❓ Common Questions

**Q: The AI marking seems different from my teacher's feedback?**  
A: AI marking is predictive based on patterns in NZQA schedules. Always prioritize your teacher's feedback for actual assessments.

**Q: How accurate is the predicted grade?**  
A: It's a strong indicator but not official. Use it to gauge your level, not as a final judgment.

**Q: Can I use this for actual NCEA submissions?**  
A: No! This is for PRACTICE only. Using AI-generated content for actual assessments is malpractice.

**Q: My response was marked too harshly/generously**  
A: Try providing more context in your response. Longer, more detailed answers (3+ paragraphs) get more accurate feedback.

**Q: The app is slow when marking**  
A: This depends on the AI provider. OpenAI is fastest (~5 sec), local Ollama may take longer depending on your computer.

---

### 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "API Error" when marking | Check your internet connection. If using OpenAI, verify your API key has credits |
| "Rate Limit Exceeded" | You've made too many requests. Wait 1 minute and try again |
| Generic/vague feedback | Write a longer response (at least 2-3 paragraphs) |
| Wrong marking rubric used | Double-check you selected the correct standard before generating |
| App won't load | Ensure both backend (port 8000) and frontend (port 3000) are running |

---

### 📱 Mobile Access
The platform works on tablets and phones! Great for:
- Quick practice sessions
- Reading exemplars on the go
- Checking progress dashboard

However, for writing full essays, we recommend using a laptop or desktop computer.

---

### 🎓 Example Study Session (15 minutes)

1. **Min 0-2**: Select Level 2 → AS91108 (Unfamiliar Texts)
2. **Min 2-3**: Generate question with sample text using CAPTE
3. **Min 3-8**: Write your response (aim for 2 solid paragraphs)
4. **Min 8-10**: Submit and read AI feedback
5. **Min 10-13**: View exemplar and note 2 things to improve
6. **Min 13-15**: Plan how you'll apply this to your next attempt

Repeat 2-3 times per week for best results!
