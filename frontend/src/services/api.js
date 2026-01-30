import axios from 'axios';

// In production (Vercel), use relative path. In development, use localhost
const API_URL = import.meta.env.VITE_API_URL || 
  (import.meta.env.PROD ? '' : 'http://localhost:8000');

// Create axios instance with default config
const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 seconds
});

// Request interceptor
axiosInstance.interceptors.request.use(
  (config) => {
    // You can add auth tokens here if needed
    // const token = localStorage.getItem('token');
    // if (token) {
    //   config.headers.Authorization = `Bearer ${token}`;
    // }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // Server responded with error
      console.error('API Error:', error.response.data);
    } else if (error.request) {
      // Request made but no response
      console.error('Network Error:', error.message);
    } else {
      // Something else happened
      console.error('Error:', error.message);
    }
    return Promise.reject(error);
  }
);

// API methods
export const api = {
  // Bug endpoints
  getBugs: (params = {}) => axiosInstance.get('/api/bugs', { params }),
  
  getBug: (id) => axiosInstance.get(`/api/bugs/${id}`),
  
  createBug: (data) => axiosInstance.post('/api/bugs', data),
  
  updateBug: (id, data) => axiosInstance.put(`/api/bugs/${id}`, data),
  
  deleteBug: (id) => axiosInstance.delete(`/api/bugs/${id}`),
  
  // Prediction endpoint
  predictSeverity: (data) => axiosInstance.post('/api/predict', data),
  
  // Statistics endpoint
  getStats: () => axiosInstance.get('/api/stats'),
  
  // Health check
  healthCheck: () => axiosInstance.get('/health'),
};

export default api;
