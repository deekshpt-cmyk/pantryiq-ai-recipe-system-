import streamlit as st
from detect import detect_ingredients
from recipe_engine import recommend
from chatbot import gen_z_chat
from PIL import Image

st.set_page_config(page_title="PantryIQ", layout="wide", initial_sidebar_state="expanded")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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
    
    # Chatbot section below recipes
    st.divider()
    st.subheader("💬 Chat with Your Gen-Z Chef!")
    
    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Chat input
    user_input = st.chat_input("Ask the Gen-Z Chef anything about these recipes! 🍕")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.write(user_input)
        
        # Get bot response
        bot_response = gen_z_chat(user_input, st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        
        with st.chat_message("assistant"):
            st.write(bot_response)
        
        st.rerun()
