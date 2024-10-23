import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const login = async ({ username, password }) => {
  const response = await api.post('/token/', {
    username,
    password
  });
  return {
    access: response.data.access,
    user: {
      username
    }
  };
};

export const getDocuments = async () => {
  const response = await api.get('/documents/');
  return response.data.results || []; // עדכון לטיפול בתגובת DRF pagination
};

export const uploadDocument = async (formData) => {
  const response = await api.post('/documents/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export default api;
