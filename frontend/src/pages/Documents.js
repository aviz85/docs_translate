import React, { useEffect, useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Typography,
  Chip,
  CircularProgress,
  Box,
  Alert,
} from '@mui/material';
import { getDocuments } from '../services/api';

function Documents() {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDocuments = async () => {
      try {
        const data = await getDocuments();
        setDocuments(data);
      } catch (error) {
        console.error('Error fetching documents:', error);
        setError('Failed to fetch documents. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchDocuments();
  }, []);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" mt={4}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error" sx={{ mt: 2 }}>
        {error}
      </Alert>
    );
  }

  return (
    <>
      <Typography variant="h4" gutterBottom>
        My Documents
      </Typography>
      {documents.length === 0 ? (
        <Alert severity="info">
          You haven't uploaded any documents yet.
        </Alert>
      ) : (
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Title</TableCell>
                <TableCell>Source Language</TableCell>
                <TableCell>Target Language</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Created At</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {documents.map((doc) => (
                <TableRow key={doc.id}>
                  <TableCell>{doc.title}</TableCell>
                  <TableCell>{doc.source_language}</TableCell>
                  <TableCell>{doc.target_language}</TableCell>
                  <TableCell>
                    <Chip
                      label={doc.status}
                      color={
                        doc.status === 'completed'
                          ? 'success'
                          : doc.status === 'failed'
                          ? 'error'
                          : doc.status === 'in_progress'
                          ? 'warning'
                          : 'default'
                      }
                    />
                  </TableCell>
                  <TableCell>
                    {new Date(doc.created_at).toLocaleDateString()}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </>
  );
}

export default Documents;
