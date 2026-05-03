from ultralytics import YOLO
import cv2
import os

_model = None

LABEL_MAP = {
    "banana": "banana",
    "apple": "apple",
    "carrot": "carrot",
    "broccoli": "broccoli",
    "orange": "orange",
}

def _get_model():
    global _model
    if _model is None:
        model_path = os.path.join(os.path.dirname(__file__), "yolov8n.pt")
        _model = YOLO(model_path)
    return _model

def detect_ingredients(img_path: str) -> list:
    model = _get_model()
    img = cv2.imread(img_path)
    results = model(img)
    detected = set()
    for r in results:
        for cls in r.boxes.cls:
            label = model.names[int(cls)]
            if label in LABEL_MAP:
                detected.add(LABEL_MAP[label])
    return list(detected)