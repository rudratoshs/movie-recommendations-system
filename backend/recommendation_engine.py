import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import logging

# Load the movie rating and metadata data
ratings_data = pd.read_csv('data/ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
columns = ['movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_URL',
           'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 
           'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 
           'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movie_data = pd.read_csv('data/ml-100k/u.item', sep='|', header=None, names=columns, encoding='latin-1')

# Create a user-item matrix for collaborative filtering
def create_user_item_matrix():
    user_item_matrix = ratings_data.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
    return user_item_matrix

# Train the SVD model for collaborative filtering
def train_svd_model():
    user_item_matrix = create_user_item_matrix()
    svd = TruncatedSVD(n_components=20)  # Adjust number of components based on optimal performance
    svd_matrix = svd.fit_transform(user_item_matrix)
    return svd, svd_matrix

# Initialize SVD model
svd, svd_matrix = train_svd_model()

# Enhance collaborative filtering with cosine similarity
def get_collaborative_recommendations(user_movie_id, top_n=10):
    try:
        # Get the latent vector for the given movie
        item_row = svd_matrix[user_movie_id, :].reshape(1, -1)
        
        # Compute cosine similarity between all movies and the given movie
        similarities = cosine_similarity(svd_matrix, item_row).flatten()
        
        # Get the indices of the top similar movies
        similar_items = similarities.argsort()[::-1][1:top_n + 1]  # Exclude the input movie itself
        return movie_data[movie_data['movie_id'].isin(similar_items)][['movie_title']].to_dict(orient='records')
    
    except IndexError:
        logging.error(f"Movie ID {user_movie_id} not found in the matrix.")
        return []

# Build a graph of movies connected by shared genres
def build_movie_graph():
    G = nx.Graph()
    for _, movie in movie_data.iterrows():
        movie_id = movie['movie_id']
        genres = movie[columns[5:]]  # Fetch genre columns
        genre_labels = [columns[i] for i in range(5, len(columns)) if movie.iloc[i] == 1]
        G.add_node(movie_id, title=movie['movie_title'])
        for genre in genre_labels:
            G.add_node(genre)
            G.add_edge(movie_id, genre)
    return G

# Initialize the movie graph
movie_graph = build_movie_graph()

# Get recommendations based on graph traversal (genre-based)
# Function for graph-based recommendation (using genre similarity)
def get_graph_based_recommendations(movie_title, top_n=10):
    try:
        # Find the movie node by its title
        movie_node = next(node for node, attr in movie_graph.nodes(data=True) if attr.get('title') == movie_title)
        
        # Get neighbors of the movie node (related by genre) with a cutoff of 2 hops
        neighbors = list(nx.single_source_shortest_path_length(movie_graph, movie_node, cutoff=2).keys())
        
        # Filter neighbors to return only valid movie nodes
        recommended_movies = []
        for n in neighbors:
            if n != movie_node and not movie_data[movie_data['movie_id'] == n].empty:
                recommended_movies.append(movie_data.loc[movie_data['movie_id'] == n]['movie_title'].values[0])
        
        return recommended_movies[:top_n]
    
    except StopIteration:
        logging.error(f"Movie {movie_title} not found in the graph.")
        return []

# Combine collaborative filtering and graph-based recommendations for hybrid recommendations
# Function to get hybrid recommendations
def get_hybrid_recommendations(user_movie_id, top_n=10):
    # Ensure user_movie_id is an integer
    user_movie_id = int(user_movie_id)

    # Debugging: print out the user_movie_id
    print(f"Looking for movie ID: {user_movie_id}")
    
    # Ensure the movie ID exists in the dataset
    if user_movie_id not in movie_data['movie_id'].values:
        logging.error(f"Movie ID {user_movie_id} not found in the dataset.")
        return []

    # Fetch recommendations
    collaborative_recs = get_collaborative_recommendations(user_movie_id, top_n=top_n)
    movie_title = movie_data.loc[movie_data['movie_id'] == user_movie_id, 'movie_title'].values[0]
    graph_recs = get_graph_based_recommendations(movie_title, top_n=top_n)

    # Combine both sets of recommendations
    hybrid_recs = {rec['movie_title'] for rec in collaborative_recs} | set(graph_recs)
    return list(hybrid_recs)

# Function to filter movies based on user preferences (rating, genre, year)
def filter_movies(filters):
    """Apply filters to the dataset based on rating, genre, and year."""
    min_rating = filters.get('min_rating', 0)
    genre = filters.get('genre', None)
    year = filters.get('year', 0)

    # Ensure release_year is available in movie_data
    if 'release_year' not in movie_data.columns:
        movie_data['release_year'] = pd.to_datetime(movie_data['release_date'], errors='coerce').dt.year
    
    # Step 1: Filter by rating
    filtered_data = ratings_data[ratings_data['rating'] >= min_rating]

    # Step 2: Merge with movie data for further filtering
    filtered_data = pd.merge(filtered_data, movie_data, on='movie_id')

    # Step 3: Filter by genre
    if genre and genre in movie_data.columns:
        filtered_data = filtered_data[filtered_data[genre] == 1]

    # Step 4: Filter by release year
    if year:
        filtered_data = filtered_data[filtered_data['release_year'] >= int(year)]

    # Return the filtered movie details
    return filtered_data[['movie_title', 'release_year', 'rating']].to_dict(orient='records')