'use client';

import { useState } from 'react';
import { markingAPI } from '@/lib/api';

interface AIMarkerProps {
  question: string;
  subject: string;
  level: number;
  standardCode?: string;
}

export default function AIMarker({ question, subject, level, standardCode }: AIMarkerProps) {
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState('');
  const [showExemplar, setShowExemplar] = useState(false);
  const [exemplar, setExemplar] = useState('');
  const [breakdown, setBreakdown] = useState<any>(null);

  const handleMark = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const markingResult = await markingAPI.mark({
        response,
        question,
        level,
        subject,
        standard_code: standardCode,
      });
      
      setResult(markingResult.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to mark response');
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateExemplar = async () => {
    setLoading(true);
    try {
      const exemplarResult = await markingAPI.generateExemplar(question, level, subject, standardCode);
      setExemplar(exemplarResult.data.exemplar);
      setShowExemplar(true);
    } catch (err: any) {
      setError('Failed to generate exemplar');
    } finally {
      setLoading(false);
    }
  };

  const handleBreakDown = async () => {
    setLoading(true);
    try {
      const breakdownResult = await markingAPI.breakDown(question, subject);
      setBreakdown(breakdownResult.data);
    } catch (err: any) {
      setError('Failed to break down question');
    } finally {
      setLoading(false);
    }
  };

  const getGradeColor = (grade: string) => {
    switch (grade) {
      case 'excellence': return 'bg-green-100 border-green-500 text-green-800';
      case 'merit': return 'bg-blue-100 border-blue-500 text-blue-800';
      case 'achieved': return 'bg-yellow-100 border-yellow-500 text-yellow-800';
      default: return 'bg-red-100 border-red-500 text-red-800';
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold text-ncea-secondary mb-4">AI Marking</h2>

      {/* Question Display */}
      <div className="mb-4 p-4 bg-ncea-light rounded-lg">
        <h3 className="font-semibold text-ncea-primary mb-2">Question:</h3>
        <p className="whitespace-pre-wrap">{question}</p>
      </div>

      {/* Action Buttons */}
      <div className="flex gap-2 mb-4">
        <button
          onClick={handleBreakDown}
          disabled={loading}
          className="px-4 py-2 bg-ncea-accent text-ncea-secondary rounded-lg font-semibold hover:opacity-90 transition disabled:opacity-50"
        >
          💡 Study Mode (Break Down)
        </button>
        <button
          onClick={handleGenerateExemplar}
          disabled={loading}
          className="px-4 py-2 bg-ncea-primary text-white rounded-lg font-semibold hover:bg-ncea-secondary transition disabled:opacity-50"
        >
          📚 View Exemplar
        </button>
      </div>

      {/* Study Mode Breakdown */}
      {breakdown && (
        <div className="mb-4 p-4 bg-purple-50 border border-purple-200 rounded-lg">
          <h3 className="font-bold text-purple-800 mb-2">
            {breakdown.framework} Framework Breakdown
          </h3>
          <div className="whitespace-pre-wrap text-sm">{breakdown.breakdown}</div>
        </div>
      )}

      {/* Response Input */}
      <form onSubmit={handleMark} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Your Response
          </label>
          <textarea
            value={response}
            onChange={(e) => setResponse(e.target.value)}
            rows={8}
            className="w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-ncea-primary focus:border-ncea-primary"
            placeholder="Write your answer here..."
            required
          />
        </div>

        <button
          type="submit"
          disabled={loading || !response.trim()}
          className="w-full bg-ncea-primary text-white py-3 rounded-lg font-semibold hover:bg-ncea-secondary transition disabled:opacity-50"
        >
          {loading ? 'Marking...' : 'Get AI Feedback'}
        </button>
      </form>

      {error && (
        <div className="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
          {error}
        </div>
      )}

      {/* Marking Results */}
      {result && (
        <div className="mt-6 space-y-4">
          {/* Grade Badge */}
          <div className={`p-4 border-2 rounded-lg ${getGradeColor(result.predicted_grade)}`}>
            <div className="flex justify-between items-center">
              <div>
                <h3 className="text-lg font-bold capitalize">{result.predicted_grade.replace('_', ' ')}</h3>
                <p className="text-sm opacity-75">Confidence: {(result.confidence * 100).toFixed(0)}%</p>
              </div>
              <div className="text-4xl">
                {result.predicted_grade === 'excellence' && '🌟'}
                {result.predicted_grade === 'merit' && '⭐'}
                {result.predicted_grade === 'achieved' && '✓'}
                {result.predicted_grade === 'not_achieved' && '✗'}
              </div>
            </div>
          </div>

          {/* Overall Feedback */}
          <div className="p-4 bg-gray-50 rounded-lg">
            <h4 className="font-semibold mb-2">Overall Feedback</h4>
            <p className="whitespace-pre-wrap">{result.feedback}</p>
          </div>

          {/* Strengths */}
          {result.strengths && result.strengths.length > 0 && (
            <div className="p-4 bg-green-50 rounded-lg">
              <h4 className="font-semibold text-green-800 mb-2">✓ Strengths</h4>
              <ul className="list-disc list-inside space-y-1">
                {result.strengths.map((s: string, i: number) => (
                  <li key={i} className="text-sm">{s}</li>
                ))}
              </ul>
            </div>
          )}

          {/* Weaknesses */}
          {result.weaknesses && result.weaknesses.length > 0 && (
            <div className="p-4 bg-yellow-50 rounded-lg">
              <h4 className="font-semibold text-yellow-800 mb-2">⚠ Areas for Improvement</h4>
              <ul className="list-disc list-inside space-y-1">
                {result.weaknesses.map((w: string, i: number) => (
                  <li key={i} className="text-sm">{w}</li>
                ))}
              </ul>
            </div>
          )}

          {/* Next Steps */}
          {result.next_steps && result.next_steps.length > 0 && (
            <div className="p-4 bg-blue-50 rounded-lg">
              <h4 className="font-semibold text-blue-800 mb-2">📋 Next Steps to Reach Next Level</h4>
              <ol className="list-decimal list-inside space-y-1">
                {result.next_steps.map((n: string, i: number) => (
                  <li key={i} className="text-sm">{n}</li>
                ))}
              </ol>
            </div>
          )}
        </div>
      )}

      {/* Exemplar Modal/Section */}
      {showExemplar && exemplar && (
        <div className="mt-6 p-4 bg-indigo-50 border border-indigo-200 rounded-lg">
          <div className="flex justify-between items-center mb-4">
            <h3 className="font-bold text-indigo-800">Excellence Exemplar</h3>
            <button
              onClick={() => setShowExemplar(false)}
              className="text-indigo-600 hover:text-indigo-800"
            >
              ✕ Close
            </button>
          </div>
          <div className="whitespace-pre-wrap text-sm max-h-96 overflow-y-auto">
            {exemplar}
          </div>
        </div>
      )}
    </div>
  );
}
