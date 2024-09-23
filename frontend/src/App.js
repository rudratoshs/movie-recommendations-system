import React, { useState } from 'react';
import { Container } from 'react-bootstrap';
import FilterForm from './components/FilterForm';
import Recommendations from './components/Recommendations';
import Analytics from './components/Analytics';

const App = () => {
  const [filteredMovies, setFilteredMovies] = useState([]);

  return (
    <Container>
      <h1 className="my-4 text-center">Movie Recommendation System</h1>
      <FilterForm setFilteredMovies={setFilteredMovies} />
      <Recommendations movies={filteredMovies} />
      <Analytics />
    </Container>
  );
};

export default App;