from ultralytics import YOLO

model = YOLO("model/food_detector.pt")

def detect_food(frame):
    results = model(frame, conf=0.4)
    detected = {}

    for r in results:
        for box in r.boxes:
            label = model.names[int(box.cls)]

            # Solo aceptar clases que están en el menú
            detected[label] = detected.get(label, 0) + 1

    return detected
