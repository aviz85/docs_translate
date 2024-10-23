import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  TextField,
  Button,
  Paper,
  Typography,
  Box,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Alert,
  CircularProgress,
} from '@mui/material';
import { uploadDocument } from '../services/api';

const languages = [
  { code: 'en', name: 'English' },
  { code: 'he', name: 'Hebrew' },
  { code: 'es', name: 'Spanish' },
  { code: 'fr', name: 'French' },
];

function Upload() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    title: '',
    source_language: '',
    target_language: '',
    original_file: null,
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [selectedFileName, setSelectedFileName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const data = new FormData();
      Object.keys(formData).forEach((key) => {
        if (formData[key]) {
          data.append(key, formData[key]);
        }
      });
      
      await uploadDocument(data);
      navigate('/documents');
    } catch (error) {
      console.error('Upload error:', error);
      setError(
        error.response?.data?.detail || 
        error.response?.data?.original_file?.[0] ||
        'Upload failed. Please try again.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFormData({ ...formData, original_file: file });
      setSelectedFileName(file.name);
    }
  };

  return (
    <Box display="flex" justifyContent="center">
      <Paper sx={{ p: 4, maxWidth: 600, width: '100%' }}>
        <Typography variant="h5" component="h1" gutterBottom>
          Upload Document
        </Typography>
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Title"
            margin="normal"
            value={formData.title}
            onChange={(e) =>
              setFormData({ ...formData, title: e.target.value })
            }
            required
          />
          
          <FormControl fullWidth margin="normal" required>
            <InputLabel>Source Language</InputLabel>
            <Select
              value={formData.source_language}
              onChange={(e) =>
                setFormData({ ...formData, source_language: e.target.value })
              }
              label="Source Language"
            >
              {languages.map((lang) => (
                <MenuItem key={lang.code} value={lang.code}>
                  {lang.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <FormControl fullWidth margin="normal" required>
            <InputLabel>Target Language</InputLabel>
            <Select
              value={formData.target_language}
              onChange={(e) =>
                setFormData({ ...formData, target_language: e.target.value })
              }
              label="Target Language"
            >
              {languages.map((lang) => (
                <MenuItem key={lang.code} value={lang.code}>
                  {lang.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <Button
            variant="contained"
            component="label"
            fullWidth
            sx={{ mt: 2 }}
          >
            Choose File
            <input
              type="file"
              hidden
              onChange={handleFileChange}
              accept=".doc,.docx,.pdf,.txt"
            />
          </Button>
          
          {selectedFileName && (
            <Typography variant="body2" sx={{ mt: 1, ml: 1 }}>
              Selected file: {selectedFileName}
            </Typography>
          )}

          <Button
            fullWidth
            variant="contained"
            type="submit"
            sx={{ mt: 2 }}
            disabled={loading || !formData.original_file}
          >
            {loading ? <CircularProgress size={24} /> : 'Upload'}
          </Button>
        </form>
      </Paper>
    </Box>
  );
}

export default Upload;
