import os
import re

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from recipe_engine import recommend

# Gen-Z slang and meme responses
GEN_Z_RESPONSES = {
    "help": "Yo bestie! Need help? We got you covered fam! 💯 Ask me anything about food and I'll spill the tea! ☕✨",
    "cooking": "Cooking is literally giving main character energy fr fr! 🔥👑 Let's get you prepped and ready to serve looks AND meals! 💅🍳",
    "recipe": "Bestie, recipes hit different when they're actually bussin bussin! 💅 No cap, these combos are so fire! 🔥",
    "healthy": "Girl/Guy, eating healthy is the vibe! 💚 Your body is a temple and we're about to make it slay! 🧘‍♀️✨",
    "dessert": "OMG YAAAS! Dessert? That's literally a whole mood! 🍰😍 Warning: these sweets are gonna have you in a chokehold! 🤤",
    "fail": "Nah girl/guy, cooking fail = character development fr! 😭 No cap, even Gordon Ramsay had L's! It's giving growth! 📈",
    "quick": "Aight bet, quick meals are clutch! ⚡ No time to waste, let's get it done fast - that's some sigma energy right there! 💪",
    "budget": "Budget friendly? That's giving smart money moves cha! 💰✨ Saving coins while eating good? That's the MOVE! 🎯",
    "tired": "Bestie, I feel you! Tired energy is real! 😴 But food? Food never stops slaying! Let me hit you with something easy that still eats! 👀",
    "vibe": "Yo, what's the vibe? What mood are we giving? Spicy? Comforting? Fancy? Tell me and I'll serve you the perfect recipe energy! 🍽️✨",
}

# Common ingredients to look for
INGREDIENTS_LIST = [
    "banana", "apple", "carrot", "broccoli", "orange", "chicken", "bread", "cheese",
    "egg", "milk", "tomato", "lettuce", "onion", "garlic", "potato", "pasta", "rice",
    "fish", "bacon", "ham", "pepper", "salt", "sugar", "flour", "meat", "beef", "pork",
    "mushroom", "pea", "corn", "pineapple", "strawberry", "grape", "pizza", "sandwich"
]

def extract_ingredients(text):
    """Extract ingredient mentions from user text"""
    text_lower = text.lower()
    found = []
    
    for ingredient in INGREDIENTS_LIST:
        if ingredient in text_lower:
            found.append(ingredient)
    
    return list(set(found))  # Remove duplicates

def get_genz_personality(user_message: str) -> str:
    """Add gen-z personality to responses"""
    genz_starters = [
        "Yo bestie! ",
        "Slay! ",
        "Listen bestie, ",
        "Not you asking that! ",
        "Okay but like, ",
        "No cap, ",
        "Literally me! ",
        "Periodt! ",
        "Lowkey though, ",
    ]
    
    genz_enders = [
        " fr fr! 💯",
        " no cap! ✨",
        " it's giving! 🔥",
        " and that's on periodt! 💅",
        " bestie! 👑",
        " slay! 💅✨",
        " catch my drift? 👀",
        " it's literally so fire! 🌶️",
    ]
    
    import random
    
    # Check for keywords and return appropriate response
    message_lower = user_message.lower()
    for keyword, response in GEN_Z_RESPONSES.items():
        if keyword in message_lower:
            return response
    
    return None

def format_recipes_genz(recipes):
    """Format recipe recommendations in Gen-Z style"""
    if not recipes:
        return "Bestie, I couldn't find any recipes! 😭 Maybe try different ingredients? No cap! 💯"
    
    response = "OMG YAAAS! Check out these recipes fr fr! 🔥✨\n\n"
    
    for recipe, score in recipes:
        match_pct = round(score * 100, 1)
        response += f"**{recipe['name']}** - {match_pct}% match 💯\n"
        response += f"Ingredients: {', '.join(recipe['ingredients'])}\n"
        response += f"Time: {recipe.get('time', '?')} mins ⏰\n"
        response += "That's giving BUSSIN vibes! 🍳✨\n\n"
    
    return response

def gen_z_chat(user_message: str, chat_history: list = None) -> str:
    """
    Generate a gen-z response using OpenAI API or fallback responses
    Also recommends recipes if ingredients are mentioned
    """
    
    # Extract ingredients from user message
    ingredients = extract_ingredients(user_message)
    
    # If ingredients found, recommend recipes
    if ingredients:
        recipes = recommend(ingredients)
        return format_recipes_genz(recipes)
    
    # First try to match with pre-made gen-z responses
    genz_response = get_genz_personality(user_message)
    if genz_response:
        return genz_response
    
    # Try to use OpenAI API
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if openai_api_key:
        try:
            from openai import OpenAI
            
            client = OpenAI(api_key=openai_api_key)
            
            # Build conversation history for context
            messages = [
                {
                    "role": "system",
                    "content": """You are a fun, sassy Gen-Z food expert chatbot named "Chef Bestie". 
You respond ONLY in Gen-Z slang and meme culture language. 
- Use phrases like: "no cap", "fr fr", "periodt", "slay", "bussin", "it's giving", "lowkey", "that's the vibe", "bestie", "sis/fam"
- Include emojis generously
- Be enthusiastic, supportive, and fun
- Give actual helpful cooking/food advice but in a Gen-Z way
- Roast jokingly when appropriate
- Keep responses concise but energetic"""
                }
            ]
            
            # Add chat history if provided
            if chat_history:
                for msg in chat_history[-6:]:  # Last 6 messages for context
                    messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
            
            # Add current user message
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.8,
                max_tokens=200
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"OpenAI API error: {e}")
    
    # Fallback responses when API not available
    fallback_responses = [
        "Okay bestie, that's giving main character energy! 🔥 Tell me more and I'll hit you with the recipe tea! ☕✨",
        "Yo! That's literally so fire! 💯 Let me cook something up for you real quick! 🍳",
        "Slay! I love the energy! 👑 What ingredients you working with? Let's make some magic! ✨",
        "Nah fr fr, that's the vibe! 💚 I got you covered bestie! 🙌",
        "Periodt! Not you asking the right questions! 💅 Let's get you fed! 🍽️",
        "It's literally giving gourmet energy! 🤩 What's your food mood today?",
        "Lowkey that's genius! 🧠✨ I'm here to help you create culinary masterpieces! 👨‍🍳",
        "Based and delicious pilled! 💊 Let's talk about your cooking dreams!",
    ]
    
    import random
    return random.choice(fallback_responses)
