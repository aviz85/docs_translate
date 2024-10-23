import React from 'react';
import { Typography, Button, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

function Home() {
  const navigate = useNavigate();
  const { isAuthenticated } = useSelector((state) => state.auth);

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        textAlign: 'center',
        mt: 8,
      }}
    >
      <Typography variant="h2" component="h1" gutterBottom>
        Welcome to Docs Translate
      </Typography>
      <Typography variant="h5" color="textSecondary" paragraph>
        Translate your documents quickly and efficiently
      </Typography>
      <Box sx={{ mt: 4 }}>
        {isAuthenticated ? (
          <>
            <Button
              variant="contained"
              color="primary"
              size="large"
              onClick={() => navigate('/upload')}
              sx={{ mr: 2 }}
            >
              Upload Document
            </Button>
            <Button
              variant="outlined"
              color="primary"
              size="large"
              onClick={() => navigate('/documents')}
            >
              My Documents
            </Button>
          </>
        ) : (
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={() => navigate('/login')}
          >
            Get Started
          </Button>
        )}
      </Box>
    </Box>
  );
}

export default Home;
