import React, { useState } from 'react';
import axios from 'axios';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';

const FilterForm = ({ setFilteredMovies }) => {
  const [minRating, setMinRating] = useState(3);  // Default to 3
  const [genre, setGenre] = useState('');         // Default to empty
  const [year, setYear] = useState('');           // Default to empty

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Ensure the year is sent as an integer (or null if empty)
    const yearInt = year ? parseInt(year) : null;

    try {
      const response = await axios.post('http://127.0.0.1:5000/analytics', {
        min_rating: Number(minRating),  // Ensure min_rating is a number
        genre: genre || null,           // Ensure genre is null if empty
        year: yearInt                   // Year is sent as an integer or null
      });

      setFilteredMovies(response.data);
    } catch (error) {
      console.error('Error fetching filtered movies:', error);
    }
  };

  return (
    <Container className="mt-4">
      <h2 className="mb-4">Filter Movies</h2>
      <Form onSubmit={handleSubmit}>
        <Row>
          <Col md={4}>
            <Form.Group controlId="minRating">
              <Form.Label>Minimum Rating</Form.Label>
              <Form.Control
                type="number"
                value={minRating}
                onChange={(e) => setMinRating(e.target.value)}
                placeholder="Enter minimum rating"
              />
            </Form.Group>
          </Col>
          <Col md={4}>
            <Form.Group controlId="genre">
              <Form.Label>Genre</Form.Label>
              <Form.Control
                type="text"
                value={genre}
                onChange={(e) => setGenre(e.target.value)}
                placeholder="Enter genre"
              />
            </Form.Group>
          </Col>
          <Col md={4}>
            <Form.Group controlId="year">
              <Form.Label>Year</Form.Label>
              <Form.Control
                type="number"
                value={year}
                onChange={(e) => setYear(e.target.value)}
                placeholder="Enter year"
              />
            </Form.Group>
          </Col>
        </Row>
        <Button className="mt-3" variant="primary" type="submit">
          Apply Filters
        </Button>
      </Form>
    </Container>
  );
};

export default FilterForm;