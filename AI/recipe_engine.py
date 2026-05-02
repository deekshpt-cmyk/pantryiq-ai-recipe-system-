from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

with open("recipes.json") as f:
    recipes = json.load(f)

corpus = [" ".join(r["ingredients"]) for r in recipes]

vectorizer = TfidfVectorizer()
recipe_matrix = vectorizer.fit_transform(corpus)

def recommend(user_ingredients):
    user_text = " ".join(user_ingredients)
    user_vec = vectorizer.transform([user_text])

    scores = cosine_similarity(user_vec, recipe_matrix)[0]

    ranked = sorted(zip(recipes, scores), key=lambda x: x[1], reverse=True)

    return ranked[:3]