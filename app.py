from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from flask import request, jsonify
import cv2

from ultralytics import YOLO

from nutrition.evaluator import evaluate_menu
from nutrition.user_profile import UserProfile

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Cargar modelo
model = YOLO("model/food_detector_small.pt")

# Perfil de usuario (vacío al inicio)
user = UserProfile()

def generate_frames():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        success, frame = camera.read()
        if not success:
            break

        detected_items = {}

        results = model(frame, conf=0.5, stream=True)

        for result in results:
            if result.boxes is None:
                continue

            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                class_id = int(box.cls[0])
                class_name = result.names[class_id]
                confidence = float(box.conf[0])

                detected_items[class_name] = detected_items.get(class_name, 0) + 1

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{class_name} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

        # Evaluación nutricional
        nutrition_result = evaluate_menu(detected_items, user)

        socketio.emit("nutrition_update", {
            "items": detected_items,
            "nutrition": nutrition_result
        })

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
        )


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update_profile", methods=["POST"])
def update_profile():
    data = request.json

    try:
        user.height = int(float(data["height"]) * 100)  # metros → cm
        user.weight = int(data["weight"])
        user.target_weight = int(data["target_weight"])
        user.type = data["type"]

        user.calculate_daily_calories()

        print("👤 PERFIL GUARDADO:", vars(user))

        return jsonify({
            "status": "ok",
            "goal": user.goal,
            "daily_calories": user.daily_calories
        })

    except Exception as e:
        print("❌ ERROR update_profile:", e)
        return jsonify({"status": "error", "msg": str(e)}), 400

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    socketio.run(app, debug=True)
