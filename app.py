import streamlit as st
from ai.detect import detect_ingredients
from ai.recipe_engine import recommend
from chatbot import gen_z_chat
from PIL import Image
import time

st.set_page_config(page_title="Pantry AI", layout="wide", initial_sidebar_state="collapsed")

# ══════════════════════════════════════════════════════════════════
# CUSTOM STYLING
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap');

footer { visibility: hidden; }
.block-container { max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }

:root {
    --sage: #6aa67a;
    --sage-light: #b8d9c2;
    --cream: #f8faf7;
    --text-dark: #1c271e;
}

.stApp {
    background: linear-gradient(135deg, #f8faf7 0%, #eef5ef 50%, #e8f3ec 100%) !important;
    font-family: 'DM Sans', sans-serif !important;
}

.home-container {
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    min-height: 100vh; text-align: center; padding: 2rem;
}

.home-title {
    font-size: 2.5rem; color: var(--text-dark); margin-bottom: 1rem; font-weight: 600;
}

.home-subtitle {
    font-size: 1.1rem; color: #8aa08c; margin-bottom: 3rem;
}

.fridge-image {
    width: 200px; height: 280px; margin: 2rem auto;
    border-radius: 12px; box-shadow: 0 10px 40px rgba(106, 166, 122, 0.15);
}

.button-group {
    display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;
}

.ingredient-chip {
    display: inline-block; background: #6aa67a; color: white;
    padding: 0.5rem 1rem; border-radius: 24px; margin: 0.5rem;
    font-size: 0.9rem; font-weight: 500;
}

.recipe-card {
    background: white; border-radius: 12px; padding: 1.5rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08); margin: 1rem;
    border-left: 4px solid #6aa67a; transition: transform 0.2s;
}

.recipe-card:hover {
    transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.recipe-name {
    font-size: 1.3rem; font-weight: 600; color: var(--text-dark);
}

.recipe-meta {
    color: #8aa08c; font-size: 0.9rem; margin-top: 0.5rem;
}

.match-score {
    display: inline-block; background: #6aa67a; color: white;
    padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem;
}

.progress-container {
    text-align: center; padding: 3rem 2rem;
}

.ingredient-grid {
    display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;
    padding: 2rem 0;
}

.shopping-item {
    background: white; padding: 1rem; border-radius: 8px;
    margin-bottom: 0.5rem; border-left: 4px solid #6aa67a;
    display: flex; justify-content: space-between; align-items: center;
}

.back-button {
    margin-bottom: 1rem; padding: 0.5rem 1rem;
    background: #6aa67a; color: white; border: none;
    border-radius: 6px; cursor: pointer; font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# SESSION STATE INITIALIZATION
# ══════════════════════════════════════════════════════════════════
if "page" not in st.session_state:
    st.session_state.page = "home"
if "detected_ingredients" not in st.session_state:
    st.session_state.detected_ingredients = []
if "recipe_results" not in st.session_state:
    st.session_state.recipe_results = []
if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = None
if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

# ══════════════════════════════════════════════════════════════════
# HOME PAGE
# ══════════════════════════════════════════════════════════════════
def show_home():
    st.title("🥬 Pantry AI")
    st.markdown("## What's in your fridge today?")
    
    st.write("Upload a photo of your refrigerator and get instant recipe ideas")
    
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("📷 Upload Photo", type=["jpg", "jpeg", "png"], key="uploader")
        if uploaded_file:
            st.session_state.uploaded_image = uploaded_file
            st.session_state.page = "analyzing"
            st.rerun()
    
    with col2:
        if st.button("📷 Use Camera", use_container_width=True, key="camera_btn"):
            st.info("Camera feature coming soon! For now, use Upload Photo.")

# ══════════════════════════════════════════════════════════════════
# ANALYZING PAGE
# ══════════════════════════════════════════════════════════════════
def show_analyzing():
    st.title("🔍 Analyzing your ingredients...")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Simulate analysis with real detection
    img = Image.open(st.session_state.uploaded_image)
    st.session_state.uploaded_image.seek(0)
    img.save("temp.jpg")
    
    for i in range(0, 101, 20):
        time.sleep(0.2)
        progress_bar.progress(i)
        status_text.write(f"Processing image... {i}%")
    
    # Actual detection
    status_text.write("Detecting ingredients...")
    time.sleep(0.3)
    
    ingredients = detect_ingredients("temp.jpg")
    st.session_state.detected_ingredients = ingredients if ingredients else ["tomato", "onion", "cheese", "bread"]
    
    time.sleep(0.2)
    progress_bar.progress(100)
    status_text.write("✅ Detection complete!")
    
    time.sleep(0.8)
    st.session_state.page = "ingredients"
    st.rerun()

# ══════════════════════════════════════════════════════════════════
# DETECTED INGREDIENTS PAGE
# ══════════════════════════════════════════════════════════════════
def show_ingredients():
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("← Back", key="back_from_ing"):
            st.session_state.page = "home"
            st.session_state.detected_ingredients = []
            st.rerun()
    
    with col_title:
        st.title("🥕 Detected Ingredients")
    
    st.write("✏️ Customize your ingredients to find all kinds of recipes!")
    
    # Display ingredient chips
    st.write("**Detected:**")
    st.write(", ".join([i.capitalize() for i in st.session_state.detected_ingredients]))
    
    st.divider()
    
    # Allow users to add more ingredients
    st.markdown("**🥬 Add more ingredients from common list:**")
    
    common_ingredients = [
        "tomato", "onion", "garlic", "pepper", "lettuce", "cucumber", "carrot",
        "chicken", "beef", "bacon", "ham", "fish", "eggs", "cheese", "milk",
        "bread", "pasta", "rice", "olive oil", "butter", "salt", "black pepper",
        "mushroom", "broccoli", "spinach", "potato", "corn", "green beans"
    ]
    
    # Remove already detected ingredients from suggestions
    available = [ing for ing in common_ingredients if ing.lower() not in [i.lower() for i in st.session_state.detected_ingredients]]
    
    if available:
        cols = st.columns(6)
        for idx, ingredient in enumerate(available[:18]):
            with cols[idx % 6]:
                if st.button(f"+ {ingredient}", key=f"quick_add_{ingredient}", use_container_width=True):
                    st.session_state.detected_ingredients.append(ingredient.lower())
                    st.rerun()
    
    st.divider()
    
    # Manual add
    col_input, col_btn = st.columns([3, 1])
    with col_input:
        new_ingredient = st.text_input("Or type a custom ingredient:", placeholder="e.g., chicken, rice, etc.", label_visibility="collapsed")
    with col_btn:
        if new_ingredient and new_ingredient.lower() not in [i.lower() for i in st.session_state.detected_ingredients]:
            if st.button("Add", key="add_ingredient", use_container_width=True):
                st.session_state.detected_ingredients.append(new_ingredient.lower())
                st.rerun()
    
    st.divider()
    
    # Remove ingredients
    if st.session_state.detected_ingredients:
        st.markdown("**Remove ingredients:**")
        cols = st.columns(len(st.session_state.detected_ingredients))
        for idx, ingredient in enumerate(st.session_state.detected_ingredients):
            with cols[idx]:
                if st.button(f"❌ {ingredient.capitalize()}", key=f"remove_{ingredient}", use_container_width=True):
                    st.session_state.detected_ingredients.remove(ingredient)
                    st.rerun()
    
    st.divider()
    
    # Get recipe recommendations (all recipes, not just top 3)
    st.session_state.recipe_results = recommend(st.session_state.detected_ingredients, top_n=100)
    
    recipe_count = len([r for r, _ in st.session_state.recipe_results if _ > 0.05])
    
    st.success(f"🎉 Found **{recipe_count}** recipes! Ready to see all the amazing dishes you can cook?")
    
    if st.button("👀 Browse All Recipes", use_container_width=True, key="view_recipes"):
        st.session_state.page = "recipes"
        st.rerun()

# ══════════════════════════════════════════════════════════════════
# RECIPE SUGGESTIONS PAGE
# ══════════════════════════════════════════════════════════════════
def show_recipes():
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("← Back", key="back_from_recipes"):
            st.session_state.page = "ingredients"
            st.rerun()
    
    with col_title:
        st.title("👨‍🍳 All Recipes You Can Make")
    
    if not st.session_state.recipe_results:
        st.info("No recipes found. Try different ingredients!")
        return
    
    # Filter recipes with good match scores
    good_recipes = [(r, s) for r, s in st.session_state.recipe_results if s > 0.1]
    
    if not good_recipes:
        st.info("No recipes found with these ingredients. Try adding more!")
        return
    
    # Add sorting and filtering options
    col1, col2 = st.columns([1, 1])
    with col1:
        sort_by = st.selectbox("Sort by:", ["Best Match", "Recipe Name"], key="sort_recipes")
    with col2:
        min_match = st.slider("Minimum match %:", 0, 100, 10, key="min_match")
    
    # Filter by minimum match
    filtered = [(r, s) for r, s in good_recipes if s * 100 >= min_match]
    
    if sort_by == "Recipe Name":
        filtered = sorted(filtered, key=lambda x: x[0]['name'])
    
    st.write(f"Showing **{len(filtered)}** recipes")
    
    st.divider()
    
    # Display recipe cards in grid (3 columns)
    cols = st.columns(3)
    for idx, (recipe, score) in enumerate(filtered):
        with cols[idx % 3]:
            st.subheader(recipe['name'])
            st.write(f"⏱️ {recipe.get('time', '?')} mins | Easy")
            st.write(f"Match: **{round(score * 100, 1)}%**")
            
            if st.button("View Recipe →", key=f"recipe_{idx}_{recipe['name']}"):
                st.session_state.selected_recipe = recipe
                st.session_state.page = "recipe_detail"
                st.rerun()

# ══════════════════════════════════════════════════════════════════
# RECIPE DETAIL PAGE
# ══════════════════════════════════════════════════════════════════
def show_recipe_detail():
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("← Back", key="back_from_detail"):
            st.session_state.page = "recipes"
            st.rerun()
    
    with col_title:
        st.title(st.session_state.selected_recipe["name"])
    
    recipe = st.session_state.selected_recipe
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("🥘 Ingredients")
        for ingredient in recipe.get("ingredients", []):
            col_check, col_text = st.columns([1, 5])
            with col_check:
                st.checkbox("", key=f"ing_{ingredient}")
            with col_text:
                st.write(f"**{ingredient}**")
    
    with col2:
        st.subheader("📋 Recipe Info")
        st.write(f"⏱️ **Time:** {recipe.get('time', '?')} minutes")
        st.write(f"👥 **Servings:** {recipe.get('servings', '4')}")
        st.write(f"📊 **Difficulty:** Easy")
    
    st.divider()
    
    col_add, col_chat = st.columns([1, 1])
    with col_add:
        if st.button("🛒 Add Missing to Shopping List", use_container_width=True):
            for ingredient in recipe.get("ingredients", []):
                if ingredient not in st.session_state.shopping_list:
                    st.session_state.shopping_list[ingredient] = False
            st.success("Added to shopping list!")
    
    with col_chat:
        if st.button("💬 Chat about this recipe", use_container_width=True):
            st.session_state.page = "chat"
            st.rerun()

# ══════════════════════════════════════════════════════════════════
# SHOPPING LIST PAGE
# ══════════════════════════════════════════════════════════════════
def show_shopping_list():
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("← Back", key="back_from_shopping"):
            st.session_state.page = "home"
            st.rerun()
    
    with col_title:
        st.title("🛒 Shopping List")
    
    if not st.session_state.shopping_list:
        st.info("Your shopping list is empty!")
        return
    
    for ingredient, checked in list(st.session_state.shopping_list.items()):
        col_check, col_text, col_delete = st.columns([0.5, 4, 0.5])
        with col_check:
            st.session_state.shopping_list[ingredient] = st.checkbox(
                "Done", value=checked, key=f"shop_{ingredient}"
            )
        with col_text:
            text_style = "text-decoration: line-through; color: #aaa;" if checked else ""
            st.markdown(f'<span style="{text_style}">{ingredient}</span>', unsafe_allow_html=True)
        with col_delete:
            if st.button("✕", key=f"del_{ingredient}"):
                del st.session_state.shopping_list[ingredient]
                st.rerun()

# ══════════════════════════════════════════════════════════════════
# CHAT PAGE (Chatbot with Gen-Z Chef)
# ══════════════════════════════════════════════════════════════════
def show_chat():
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("← Back", key="back_from_chat"):
            st.session_state.page = "recipe_detail"
            st.rerun()
    
    with col_title:
        st.title("💬 Chat with Your Gen-Z Chef!")
    
    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Chat input
    user_input = st.chat_input("Ask anything about this recipe! 🍕")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.write(user_input)
        
        # Get bot response
        try:
            bot_response = gen_z_chat(user_input, st.session_state.chat_history)
            st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
            
            with st.chat_message("assistant"):
                st.write(bot_response)
        except Exception as e:
            st.error(f"Error getting response: {e}")
            if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "user":
                st.session_state.chat_history.pop()

# ══════════════════════════════════════════════════════════════════
# PAGE ROUTER
# ══════════════════════════════════════════════════════════════════
if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "analyzing":
    show_analyzing()
elif st.session_state.page == "ingredients":
    show_ingredients()
elif st.session_state.page == "recipes":
    show_recipes()
elif st.session_state.page == "recipe_detail":
    show_recipe_detail()
elif st.session_state.page == "shopping_list":
    show_shopping_list()
elif st.session_state.page == "chat":
    show_chat()
