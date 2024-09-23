from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from recommendation_engine import get_hybrid_recommendations as get_recommendations, filter_movies

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all domains
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response

# Load dataset
data = pd.read_csv('data/ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

# Route to get movie recommendations based on filters
@app.route('/recommend', methods=['POST'])
def recommend():
    filters = request.json
    page = int(filters.get('page', 1))
    limit = int(filters.get('limit', 10))
    recommendations = get_recommendations(filters)
    # Implement pagination logic
    start = (page - 1) * limit
    end = start + limit
    paginated_recommendations = recommendations[start:end]
    return jsonify(paginated_recommendations)

# Route to get filtered data for analytics
@app.route('/analytics', methods=['POST'])
def analytics():
    filters = request.json
    filtered_data = filter_movies(filters)
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)