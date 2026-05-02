from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

LABEL_MAP = {
    "banana": "banana",
    "apple": "apple",
    "carrot": "carrot",
    "broccoli": "broccoli",
    "orange": "orange"
}

def detect_ingredients(img_path):
    img = cv2.imread(img_path)
    results = model(img)

    detected = set()
    for r in results:
        for cls in r.boxes.cls:
            label = model.names[int(cls)]
            if label in LABEL_MAP:
                detected.add(LABEL_MAP[label])

    return list(detected)

print(detect_ingredients("test.jpg"))
