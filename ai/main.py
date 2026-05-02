from AI.detect import detect_ingredients
from AI.recipe_engine import recommend

img = "test.jpg"

ingredients = detect_ingredients(img)
results = recommend(ingredients)

print("Detected:", ingredients)

for r, score in results:
    print(r["name"], "Score:", score)
