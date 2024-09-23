# 🎬 Movie Recommendation System 🍿

Welcome to the **Movie Recommendation System**! This project uses **Collaborative Filtering** and **Graph-Based Recommendations** to suggest movies based on user preferences. It leverages **Python**, **Flask**, and **React** for a full-stack application that allows users to explore movie recommendations and analytics.

### 🌟 Key Features:
- **Hybrid Recommendation Engine** combining **Collaborative Filtering** (SVD) and **Graph-Based** recommendations.
- Filter movies by **genre**, **year**, and **ratings**.
- Visualize **analytics** with interactive charts.
- Provides **personalized movie recommendations**.
- Frontend built using **React** with **Bootstrap** for a responsive UI.
- Backend API using **Flask** with **Machine Learning** models for real-time predictions.

---

## 🛠️ Project Structure:
```
movie-recommendation-system/
├── backend/                           # Backend code (Python, Flask API)
│   ├── data/                          # Folder for dataset (e.g., MovieLens)
│   ├── models/                        # Trained models and matrix factorization files
│   ├── app.py                         # Main backend server (Flask)
│   ├── recommendation_engine.py       # Code for recommendation system logic
│   └── requirements.txt               # Backend dependencies (Python, Flask, etc.)
├── frontend/                          # Frontend code (React.js or HTML/JS)
│   ├── public/                        # Public folder for frontend assets (if using React)
│   ├── src/                           # Source code for React frontend
│   │   ├── components/                # UI components
│   │   │   ├── FilterForm.js          # Component for user input filters
│   │   │   ├── Recommendations.js     # Component to display recommended movies
│   │   │   ├── Analytics.js           # Component to show graphs/tables
│   │   ├── App.js                     # Main frontend logic
│   │   ├── index.js                   # Entry point for frontend
│   └── package.json                   # Frontend dependencies (React, Axios, etc.)
├── visualizations/                    # Folder for graphs and plots (optional)
├── README.md                          # Project documentation
├── .gitignore                         # Git ignore file
```

---

## 🚀 Getting Started:

### Prerequisites:
1. **Python 3.9+**
2. **Node.js** and **npm** for the frontend
3. **Git**

### Backend Setup (Python, Flask):
1. **Clone the repository:**
   ```bash
   git clone https://github.com/rudratoshs/movie-recommendation-system.git
   cd movie-recommendation-system/backend
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download the dataset:**
   - Get the MovieLens dataset from [MovieLens Dataset](https://grouplens.org/datasets/movielens/100k/)
   - Place it in the `backend/data/` folder.

5. **Run the Flask server:**
   ```bash
   flask run
   ```

### Frontend Setup (React.js):
1. **Navigate to the frontend folder:**
   ```bash
   cd ../frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Start the React development server:**
   ```bash
   npm start
   ```

---

## 🎯 Use Case:

This system is designed to provide **personalized movie recommendations** to users based on their previous preferences and interactions. It combines **Collaborative Filtering** with **Graph-Based** recommendations to enhance accuracy.

**Scenarios:**
1. **User-specific recommendations:** Users can get movie recommendations by selecting a specific movie they've liked in the past.
2. **Filtered search:** Users can apply multiple filters like **ratings**, **genre**, and **year** to get the most relevant recommendations.
3. **Analytics and Visualization:** Real-time data visualization allows users to see trends in movie ratings and genres.

---

## 🔮 Features Breakdown:

### 🎲 Hybrid Recommendation System:
- **Collaborative Filtering**: This component is based on **SVD** (Singular Value Decomposition) to recommend movies that are similar to those a user has rated highly.
- **Graph-Based Recommendations**: A **network graph** is built using **genres**, allowing genre-based movie recommendations.

### 📊 Interactive Analytics:
- Use **Chart.js** with React to generate interactive graphs.
- Analyze movie rating trends based on **year**, **genre**, and **rating** filters.

---

## 📂 Sample Data

You can download the **MovieLens 100k dataset** [here](https://grouplens.org/datasets/movielens/100k/). After downloading, place the files in the `backend/data/` directory.

---

## 📋 API Endpoints:

### `/recommend`
- **Method**: `POST`
- **Description**: Provides movie recommendations based on collaborative filtering and graph-based algorithms.
- **Payload**:
  ```json
  {
    "movie": <movie_id>
  }
  ```

### `/analytics`
- **Method**: `POST`
- **Description**: Provides analytics data to visualize movie ratings and trends.
- **Payload**:
  ```json
  {
    "min_rating": 3,
    "genre": "Action",
    "year": 2000
  }
  ```

---

## 🤖 Technologies Used:
- **Backend**: Python, Flask, Pandas, Scikit-Learn (SVD for collaborative filtering)
- **Frontend**: React.js, Axios, Bootstrap, Chart.js
- **Graph-Based Recommendations**: NetworkX

---

## 💡 Future Enhancements:
- **User Authentication**: Add user profiles to save preferences and track viewing history.
- **Extended Dataset**: Add more datasets for better recommendations.
- **Improved Recommendation Algorithms**: Implement content-based filtering or deep learning-based methods.

---

## 🎉 Contributions:
Feel free to open issues or submit pull requests for new features, bug fixes, or any improvements!

---

### 🎬 Happy Movie Recommending! 🎉

---