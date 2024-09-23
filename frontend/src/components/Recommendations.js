import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Card, Pagination } from 'react-bootstrap';
import axios from 'axios';

const Recommendations = () => {
  const [movies, setMovies] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const moviesPerPage = 10; // Number of movies per page

  const fetchMovies = async (page) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/recommend', {
        min_rating: 3,
        genre: 'Action',
        year: 2000,
        page: page,
        limit: moviesPerPage,
      });

      const data = response.data;
      setMovies(data);
      // Assuming you return the total count of recommendations from the backend
      setTotalPages(Math.ceil(100 / moviesPerPage)); // Replace `100` with total count from backend
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  // Fetch data when the component mounts or when the page changes
  useEffect(() => {
    fetchMovies(currentPage);
  }, [currentPage]);

  // Handle page change
  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  return (
    <Container className="my-4">
      <h2>Movie Recommendations</h2>
      <Row>
        {movies.map((movie, index) => (
          <Col key={index} sm={12} md={6} lg={4} className="mb-3">
            <Card>
              <Card.Body>
                <Card.Title>{movie.movie_title}</Card.Title>
                <Card.Text>Release Year: {movie.release_year}</Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>

      {/* Pagination Controls */}
      <Pagination>
        <Pagination.First onClick={() => handlePageChange(1)} />
        <Pagination.Prev
          onClick={() => handlePageChange(currentPage > 1 ? currentPage - 1 : 1)}
        />
        {[...Array(totalPages)].map((_, idx) => (
          <Pagination.Item
            key={idx}
            active={idx + 1 === currentPage}
            onClick={() => handlePageChange(idx + 1)}
          >
            {idx + 1}
          </Pagination.Item>
        ))}
        <Pagination.Next
          onClick={() =>
            handlePageChange(currentPage < totalPages ? currentPage + 1 : totalPages)
          }
        />
        <Pagination.Last onClick={() => handlePageChange(totalPages)} />
      </Pagination>
    </Container>
  );
};

export default Recommendations;