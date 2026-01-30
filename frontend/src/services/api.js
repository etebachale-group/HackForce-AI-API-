import axios from 'axios';

// API Base URL - uses relative path in production, localhost in development
const API_BASE_URL = import.meta.env.PROD ? '' : 'http://localhost:8000';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    console.log(`API Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// API Methods
export const bugAPI = {
  // Get all bugs with optional filters
  getAll: (params = {}) => api.get('/api/bugs', { params }),
  
  // Get single bug by ID
  getById: (id) => api.get(`/api/bugs/${id}`),
  
  // Create new bug
  create: (data) => api.post('/api/bugs', data),
  
  // Update bug
  update: (id, data) => api.put(`/api/bugs/${id}`, data),
  
  // Delete bug
  delete: (id) => api.delete(`/api/bugs/${id}`),
  
  // Search bugs
  search: (term) => api.get(`/api/bugs/search/${term}`),
};

export const developerAPI = {
  // Get all developers
  getAll: (params = {}) => api.get('/api/developers', { params }),
  
  // Get single developer
  getById: (id) => api.get(`/api/developers/${id}`),
  
  // Create developer
  create: (data) => api.post('/api/developers', data),
  
  // Get developer workload
  getWorkload: (id) => api.get(`/api/developers/${id}/workload`),
};

export const predictionAPI = {
  // Predict bug severity
  predict: (data) => api.post('/api/predict', data),
};

export const statsAPI = {
  // Get statistics
  get: () => api.get('/api/stats'),
};

export const systemAPI = {
  // Health check
  health: () => api.get('/health'),
  
  // API info
  info: () => api.get('/'),
};

export default api;
