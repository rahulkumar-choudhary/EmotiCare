import google.generativeai as genai
from flask import Blueprint, request, jsonify
from app.config import GEMINI_API_KEY

chatbot_bp = Blueprint("chatbot", __name__)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

@chatbot_bp.route("/ask", methods=["POST"])
def chatbot_response():
    data = request.json
    user_message = data.get("message", "")

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
