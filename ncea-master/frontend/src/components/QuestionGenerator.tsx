'use client';

import { useState } from 'react';
import { questionsAPI, markingAPI } from '@/lib/api';

interface QuestionGeneratorProps {
  onQuestionGenerated?: (question: any) => void;
}

export default function QuestionGenerator({ onQuestionGenerated }: QuestionGeneratorProps) {
  const [subject, setSubject] = useState('english');
  const [level, setLevel] = useState(1);
  const [questionType, setQuestionType] = useState('essay');
  const [textContent, setTextContent] = useState('');
  const [loading, setLoading] = useState(false);
  const [question, setQuestion] = useState<any>(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await questionsAPI.generate({
        subject,
        level,
        question_type: questionType,
        text_content: textContent || undefined,
      });
      
      setQuestion(response.data);
      if (onQuestionGenerated) {
        onQuestionGenerated(response.data);
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to generate question');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold text-ncea-secondary mb-4">Generate Practice Question</h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Subject</label>
            <select
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
              className="w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-ncea-primary focus:border-ncea-primary"
            >
              <option value="english">English</option>
              <option value="history">History</option>
              <option value="digital_technologies">Digital Technologies</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Level</label>
            <select
              value={level}
              onChange={(e) => setLevel(Number(e.target.value))}
              className="w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-ncea-primary focus:border-ncea-primary"
            >
              <option value={1}>Level 1</option>
              <option value={2}>Level 2</option>
              <option value={3}>Level 3</option>
            </select>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Question Type</label>
          <select
            value={questionType}
            onChange={(e) => setQuestionType(e.target.value)}
            className="w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-ncea-primary focus:border-ncea-primary"
          >
            <option value="essay">Essay</option>
            <option value="unfamiliar_text">Unfamiliar Text</option>
            <option value="practical">Practical/Technical</option>
          </select>
        </div>

        {questionType === 'unfamiliar_text' && (
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Text to Analyze (optional - paste or upload)
            </label>
            <textarea
              value={textContent}
              onChange={(e) => setTextContent(e.target.value)}
              rows={6}
              className="w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-ncea-primary focus:border-ncea-primary"
              placeholder="Paste the text you want to analyze here..."
            />
          </div>
        )}

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-ncea-primary text-white py-3 rounded-lg font-semibold hover:bg-ncea-secondary transition disabled:opacity-50"
        >
          {loading ? 'Generating...' : 'Generate Question'}
        </button>
      </form>

      {error && (
        <div className="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
          {error}
        </div>
      )}

      {question && (
        <div className="mt-6 p-4 bg-ncea-light rounded-lg">
          <h3 className="font-bold text-ncea-secondary mb-2">Generated Question:</h3>
          <p className="whitespace-pre-wrap">{question.question_text}</p>
        </div>
      )}
    </div>
  );
}
