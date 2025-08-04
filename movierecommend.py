import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: Load datasets
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

# STEP 2: Merge ratings with movie titles
data = pd.merge(ratings, movies, on='movieId')

# STEP 3: Create user-movie matrix
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

# STEP 4: Fill missing values with 0
user_movie_matrix.fillna(0, inplace=True)

# STEP 5: Calculate cosine similarity between movies
movie_similarity = cosine_similarity(user_movie_matrix.T)
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# STEP 6: Define a recommendation function
def recommend_movies(movie_name, top_n=5):
    if movie_name not in movie_similarity_df.columns:
        return f"❌ Movie '{movie_name}' not found in the dataset."
    similar_scores = movie_similarity_df[movie_name].sort_values(ascending=False)
    return similar_scores[1:top_n+1].index.tolist()

# Example usage
movie_to_search = "Waiting to Exhale (1995)"
recommendations = recommend_movies(movie_to_search)

print(f"🎬 Recommendations for '{movie_to_search}':")
for i, movie in enumerate(recommendations, 1):
    print(f"{i}. {movie}")
