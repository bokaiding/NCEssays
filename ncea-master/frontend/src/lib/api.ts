import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Question Generation API
export const questionsAPI = {
  generate: (data: {
    subject: string;
    level: number;
    question_type?: string;
    text_content?: string;
    standard_code?: string;
  }) => api.post('/api/questions/generate', data),
  
  generateBatch: (subject: string, level: number, count?: number) =>
    api.post(`/api/questions/generate-batch?subject=${subject}&level=${level}&count=${count || 3}`),
  
  adapt: (question: string, currentLevel: number, targetLevel: number, subject: string) =>
    api.post(`/api/questions/adapt?question=${encodeURIComponent(question)}&current_level=${currentLevel}&target_level=${targetLevel}&subject=${subject}`),
  
  followUp: (originalQuestion: string, studentResponse: string, subject: string) =>
    api.post(`/api/questions/follow-up?original_question=${encodeURIComponent(originalQuestion)}&student_response=${encodeURIComponent(studentResponse)}&subject=${subject}`),
};

// Marking API
export const markingAPI = {
  mark: (data: {
    response: string;
    question: string;
    level: number;
    subject: string;
    standard_code?: string;
  }) => api.post('/api/mark/', data),
  
  generateExemplar: (question: string, level: number, subject: string, standardCode?: string) =>
    api.post(`/api/mark/exemplar?question=${encodeURIComponent(question)}&level=${level}&subject=${subject}${standardCode ? `&standard_code=${standardCode}` : ''}`),
  
  breakDown: (question: string, subject: string, framework?: string) =>
    api.post(`/api/mark/breakdown?question=${encodeURIComponent(question)}&subject=${subject}${framework ? `&framework=${framework}` : ''}`),
};

// Dashboard API
export const dashboardAPI = {
  getDashboard: () => api.get('/api/dashboard/'),
  getAttempts: (limit?: number) => api.get(`/api/dashboard/attempts?limit=${limit || 20}`),
  getProgress: (standardCode: string) => api.get(`/api/dashboard/progress/${standardCode}`),
};

// Research API
export const researchAPI = {
  search: (query: string, limit?: number) =>
    api.get(`/api/research/search?query=${encodeURIComponent(query)}&limit=${limit || 5}`),
  
  getSummary: (title: string) =>
    api.get(`/api/research/summary/${encodeURIComponent(title)}`),
  
  getNCEAResources: (subject?: string, level?: number) =>
    api.get(`/api/research/ncea-resources${subject ? `?subject=${subject}${level ? `&level=${level}` : ''}` : ''}`),
};
