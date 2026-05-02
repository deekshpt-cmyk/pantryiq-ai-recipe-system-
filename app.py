import streamlit as st
from detect import detect_ingredients
from recipe_engine import recommend
from PIL import Image

st.title("PantryIQ 🍳")

uploaded = st.file_uploader("Upload fridge image")

if uploaded:
    img = Image.open(uploaded)
    img.save("temp.jpg")

    st.image(img)

    ingredients = detect_ingredients("temp.jpg")
    st.write("Detected:", ingredients)

    results = recommend(ingredients)

    for r, score in results:
        st.subheader(r["name"])
        st.write("Ingredients:", r["ingredients"])
        st.write("Match score:", round(score, 2))
