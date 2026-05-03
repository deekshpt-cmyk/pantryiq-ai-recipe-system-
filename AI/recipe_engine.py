from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "recipes.json")

def _load():
    with open(_DATA_PATH) as f:
        recipes = json.load(f)
    corpus = [" ".join(r["ingredients"]) for r in recipes]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(corpus)
    return recipes, vectorizer, matrix

_recipes, _vectorizer, _matrix = _load()

def recommend(user_ingredients: list, top_n: int = 3):
    user_vec = _vectorizer.transform([" ".join(user_ingredients)])
    scores = cosine_similarity(user_vec, _matrix)[0]
    ranked = sorted(zip(_recipes, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_n]