import cv2
import numpy as np
from flask import Blueprint, jsonify

emotion_bp = Blueprint("emotion", __name__)

# Load Pre-trained Model (Replace with better model if needed)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

@emotion_bp.route("/detect", methods=["GET"])
def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return jsonify({"error": "Failed to capture image"}), 500

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    emotion = "Neutral"  # Placeholder: Integrate Deep Learning Model for actual emotion classification
    if len(faces) > 0:
        emotion = "Detected Face, Analyzing Emotion..."

    return jsonify({"emotion": emotion})
