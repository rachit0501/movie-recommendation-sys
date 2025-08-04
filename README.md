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
```

---

## ▶️ How to Run

```bash
python movie_recommender.py
```

Modify the movie title and number of recommendations inside the script:

```python
get_recommendations("Toy Story (1995)", top_n=5)
```

---

## 📤 Example Output

```
Recommendations for 'Toy Story (1995)':
1. Bug's Life, A (1998)
2. Aladdin (1992)
3. Beauty and the Beast (1991)
4. Lion King, The (1994)
5. Hercules (1997)
```

---

## 📌 Future Improvements

- Add content-based filtering (genre, cast, tags)  
- Use matrix factorization (e.g., SVD)  
- Build a web interface (Flask/Streamlit)  
- Support for user-specific recommendations

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)  
- [Scikit-learn Documentation](https://scikit-learn.org/)
