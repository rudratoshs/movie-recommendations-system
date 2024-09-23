import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import axios from 'axios';
import { Container } from 'react-bootstrap';

// Register necessary Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Analytics = () => {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Movie Ratings',
        data: [],
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }
    ]
  });

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:5000/analytics', {
          min_rating: 3,
          genre: 'Action',
          year: 1995
        });

        const data = response.data;

        // Ensure data is an array and contains items before using map
        if (Array.isArray(data) && data.length > 0) {
          const titles = data.map((movie) => movie.movie_title);
          const ratings = data.map((movie) => movie.rating);

          setChartData({
            labels: titles,
            datasets: [
              {
                label: 'Movie Ratings',
                data: ratings,
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
              }
            ]
          });
        } else {
          console.error('No data available or data format is incorrect');
        }
      } catch (error) {
        console.error('Error fetching analytics data:', error);
      }
    };

    fetchAnalytics();
  }, []);

  return (
    <Container className="my-4">
      <h2>Movie Analytics</h2>
      <Line data={chartData} />
    </Container>
  );
};


export default Analytics;