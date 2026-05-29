from ultralytics import YOLO
import cv2
import os
import streamlit as st

# Use cached model loading to prevent reloading on every Streamlit rerun
@st.cache_resource
def load_model():
    # Model file is in the parent directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, "yolov8n.pt")
    return YOLO(model_path)

model = load_model()

# Extended food ingredient mapping
LABEL_MAP = {
    # Produce
    "banana": "banana",
    "apple": "apple",
    "carrot": "carrot",
    "broccoli": "broccoli",
    "orange": "orange",
    "tomato": "tomato",
    "lettuce": "lettuce",
    "onion": "onion",
    "garlic": "garlic",
    "potato": "potato",
    "pepper": "pepper",
    "bell pepper": "pepper",
    "cucumber": "cucumber",
    "mushroom": "mushroom",
    "pea": "pea",
    "corn": "corn",
    "pineapple": "pineapple",
    "strawberry": "strawberry",
    "grape": "grape",
    "lemon": "lemon",
    "lime": "lime",
    
    # Proteins
    "chicken": "chicken",
    "pizza": "pizza",
    "sandwich": "sandwich",
    "bread": "bread",
    "cheese": "cheese",
    "egg": "egg",
    "milk": "milk",
    "yogurt": "yogurt",
    "bacon": "bacon",
    "ham": "ham",
    "fish": "fish",
    "meat": "meat",
    "beef": "beef",
    "pork": "pork",
    
    # Pantry items
    "pasta": "pasta",
    "rice": "rice",
    "salt": "salt",
    "pepper": "pepper",
    "sugar": "sugar",
    "flour": "flour",
    "oil": "oil",
    
    # Things to ignore
    "person": None,
    "backpack": None,
    "umbrella": None,
    "handbag": None,
    "tie": None,
    "suitcase": None,
    "frisbee": None,
    "skis": None,
    "snowboard": None,
    "sports ball": None,
    "kite": None,
    "baseball bat": None,
    "baseball glove": None,
    "skateboard": None,
    "surfboard": None,
    "tennis racket": None,
    "bottle": None,
    "wine glass": None,
    "cup": None,
    "fork": None,
    "knife": None,
    "spoon": None,
    "bowl": None,
    "bear": None,
    "sheep": None,
    "cow": None,
    "elephant": None,
    "cat": None,
    "dog": None,
    "donut": None,
    "cake": None,
    "hot dog": None,
    "dining table": None,
    "potted plant": None,
    "bed": None,
    "couch": None,
    "toilet": None,
    "tv": None,
    "laptop": None,
    "mouse": None,
    "remote": None,
    "keyboard": None,
    "microwave": None,
    "oven": None,
    "toaster": None,
    "sink": None,
    "refrigerator": None,
    "book": None,
    "clock": None,
    "vase": None,
    "scissors": None,
    "teddy bear": None,
    "hair drier": None,
    "toothbrush": None,
}

# Common food groups for fallback suggestions
COMMON_FOODS = [
    "tomato", "onion", "garlic", "pepper", "lettuce", 
    "cheese", "bread", "chicken", "bacon", "egg",
    "milk", "pasta", "rice", "oil", "salt"
]

def detect_ingredients(img_path):
    """Detect ingredients from image using YOLO"""
    try:
        img = cv2.imread(img_path)
        if img is None:
            return COMMON_FOODS[:3]  # Fallback
        
        results = model(img)
        detected = set()
        
        for r in results:
            for cls in r.boxes.cls:
                label = model.names[int(cls)].lower().strip()
                
                # Exact match
                if label in LABEL_MAP and LABEL_MAP[label]:
                    detected.add(LABEL_MAP[label])
                else:
                    # Check for partial matches
                    for key, value in LABEL_MAP.items():
                        if value and (key in label or label in key):
                            detected.add(value)
                            break
        
        # Return detected ingredients, or some defaults if nothing found
        if detected:
            return list(detected)
        else:
            return COMMON_FOODS[:5]  # Fallback to common ingredients
    
    except Exception as e:
        print(f"Detection error: {e}")
        return COMMON_FOODS[:5]
