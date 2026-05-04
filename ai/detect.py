from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

LABEL_MAP = {
    "banana": "banana",
    "apple": "apple",
    "carrot": "carrot",
    "broccoli": "broccoli",
    "orange": "orange",
    "person": None,  # Ignore people
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
    "chicken": "chicken",
    "bear": None,
    "sheep": None,
    "cow": None,
    "elephant": None,
    "cat": None,
    "dog": None,
    "pizza": "pizza",
    "donut": None,
    "cake": None,
    "sandwich": "sandwich",
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
    # Add more food items
    "bread": "bread",
    "cheese": "cheese",
    "egg": "egg",
    "milk": "milk",
    "yogurt": "yogurt",
    "tomato": "tomato",
    "lettuce": "lettuce",
    "onion": "onion",
    "garlic": "garlic",
    "potato": "potato",
    "pasta": "pasta",
    "rice": "rice",
    "fish": "fish",
    "bacon": "bacon",
    "ham": "ham",
    "salt": "salt",
    "pepper": "pepper",
    "sugar": "sugar",
    "flour": "flour",
    "meat": "meat",
    "beef": "beef",
    "pork": "pork",
    "pepper bell": "pepper",
    "cucumber": "cucumber",
    "mushroom": "mushroom",
    "pea": "pea",
    "corn": "corn",
    "pineapple": "pineapple",
    "strawberry": "strawberry",
    "grape": "grape"
}

def detect_ingredients(img_path):
    img = cv2.imread(img_path)
    results = model(img)

    detected = set()
    for r in results:
        for cls in r.boxes.cls:
            label = model.names[int(cls)].lower()
            
            # Check if label or similar label is in our map
            if label in LABEL_MAP and LABEL_MAP[label]:
                detected.add(LABEL_MAP[label])
            
            # Also check partial matches
            for key, value in LABEL_MAP.items():
                if value and (key in label or label in key):
                    detected.add(value)
                    break

    return list(detected)
