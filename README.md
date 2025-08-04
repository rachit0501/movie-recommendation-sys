# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommendation System** built using Python. It recommends movies similar to a selected title by analyzing user rating patterns using **cosine similarity**.

---

## 🔍 Features

- Recommend similar movies based on a given movie
- Uses movie ratings from users (collaborative insights)
- Simple and beginner-friendly codebase
- Easily extendable for other recommendation models

---

## 📂 Dataset

This project uses the [MovieLens dataset](https://grouplens.org/datasets/movielens/) which includes:

- `movies.csv` — movie ID and title
- `ratings.csv` — user ID, movie ID, and rating

Make sure both files are in the same directory as the script.

---

## 🧠 How It Works

1. Load and merge movie ratings with titles  
2. Create a **user-movie matrix**  
3. Transpose to get **movie-user matrix**  
4. Use **cosine similarity** to find similar movies  
5. Return top-N recommendations for a selected title

---

## 📦 Libraries Used

- `pandas`
- `numpy`
- `scikit-learn`

Install them using:

```bash
pip install pandas numpy scikit-learn
# movie-recommendation-sys
