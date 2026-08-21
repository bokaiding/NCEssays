'use client';

import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-ncea-light to-white">
      {/* Header */}
      <header className="bg-ncea-primary text-white py-6">
        <div className="container mx-auto px-4">
          <nav className="flex justify-between items-center">
            <h1 className="text-3xl font-bold">NCEA Master</h1>
            <div className="space-x-4">
              <Link href="/dashboard" className="hover:text-ncea-accent transition">Dashboard</Link>
              <Link href="/practice" className="hover:text-ncea-accent transition">Practice</Link>
              <Link href="/research" className="hover:text-ncea-accent transition">Research</Link>
            </div>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-5xl font-bold text-ncea-secondary mb-6">
            Master NCEA with AI-Powered Practice
          </h2>
          <p className="text-xl text-gray-700 mb-8 max-w-2xl mx-auto">
            Generate NCEA-style questions, get instant AI marking feedback aligned with NZQA standards,
            and track your progress across English, History, and Digital Technologies.
          </p>
          <div className="flex justify-center gap-4">
            <Link 
              href="/practice" 
              className="bg-ncea-primary text-white px-8 py-3 rounded-lg text-lg font-semibold hover:bg-ncea-secondary transition"
            >
              Start Practicing
            </Link>
            <Link 
              href="/dashboard" 
              className="border-2 border-ncea-primary text-ncea-primary px-8 py-3 rounded-lg text-lg font-semibold hover:bg-ncea-primary hover:text-white transition"
            >
              View Dashboard
            </Link>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <h3 className="text-3xl font-bold text-center text-ncea-secondary mb-12">
            Key Features
          </h3>
          <div className="grid md:grid-cols-3 gap-8">
            <FeatureCard
              icon="📝"
              title="Question Generation"
              description="Generate authentic NCEA-style questions for Levels 1-3 in English, History, and Digital Technologies."
            />
            <FeatureCard
              icon="🤖"
              title="AI Marking"
              description="Get instant feedback aligned with NZQA marking schedules. Know exactly what you need for Achieved, Merit, or Excellence."
            />
            <FeatureCard
              icon="📊"
              title="Progress Tracking"
              description="Track your confidence scores by standard. See your improvement over time with detailed analytics."
            />
            <FeatureCard
              icon="💡"
              title="Study Mode"
              description="Break down complex questions using PETAL and IDEAR frameworks. Step-by-step guidance to Excellence."
            />
            <FeatureCard
              icon="📚"
              title="Exemplar Viewer"
              description="Compare your work against AI-generated Excellence responses. Learn what top-grade answers look like."
            />
            <FeatureCard
              icon="🔍"
              title="Research Tools"
              description="Access curated NCEA resources and search for context to enhance your understanding."
            />
          </div>
        </div>
      </section>

      {/* Subjects Section */}
      <section className="py-16 bg-ncea-light">
        <div className="container mx-auto px-4">
          <h3 className="text-3xl font-bold text-center text-ncea-secondary mb-12">
            Supported Subjects
          </h3>
          <div className="grid md:grid-cols-3 gap-8">
            <SubjectCard
              subject="English"
              levels={[1, 2, 3]}
              standards={['AS90858', 'AS91107', 'AS91472']}
              description="Unfamiliar Texts, Writing, and Critical Analysis"
            />
            <SubjectCard
              subject="History"
              levels={[1, 2, 3]}
              standards={['AS91003', 'AS91233', 'AS91434']}
              description="Historical Perspectives, Contexts, and Critical Analysis"
            />
            <SubjectCard
              subject="Digital Technologies"
              levels={[1, 2, 3]}
              standards={['AS91896', 'AS91897', 'AS91906']}
              description="Algorithms, Processes, and Technological Systems"
            />
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-ncea-secondary text-white py-8">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2024 NCEA Master. Aligned with NZQA standards.</p>
          <p className="mt-2 text-sm">
            This platform uses AI to provide practice and feedback. Always verify with official NZQA resources.
          </p>
        </div>
      </footer>
    </main>
  );
}

function FeatureCard({ icon, title, description }: { icon: string; title: string; description: string }) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition">
      <div className="text-4xl mb-4">{icon}</div>
      <h4 className="text-xl font-semibold text-ncea-secondary mb-2">{title}</h4>
      <p className="text-gray-600">{description}</p>
    </div>
  );
}

function SubjectCard({ subject, levels, standards, description }: { 
  subject: string; 
  levels: number[]; 
  standards: string[];
  description: string;
}) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h4 className="text-2xl font-bold text-ncea-primary mb-2">{subject}</h4>
      <p className="text-gray-600 mb-4">{description}</p>
      <div className="mb-2">
        <span className="font-semibold">Levels: </span>
        {levels.map(l => (
          <span key={l} className="inline-block bg-ncea-accent text-ncea-secondary px-2 py-1 rounded text-sm mr-1">
            Level {l}
          </span>
        ))}
      </div>
      <div>
        <span className="font-semibold">Standards: </span>
        <span className="text-gray-600">{standards.join(', ')}</span>
      </div>
    </div>
  );
}
