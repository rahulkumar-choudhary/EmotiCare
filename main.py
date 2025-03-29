from flask import Flask
from app.routes.chatbot import chatbot_bp
from app.routes.emotion_detection import emotion_bp
from app.routes.resources import resources_bp

app = Flask(__name__)

# Register Blueprints (Modular Routes)
app.register_blueprint(chatbot_bp, url_prefix="/chatbot")
app.register_blueprint(emotion_bp, url_prefix="/emotion")
app.register_blueprint(resources_bp, url_prefix="/resources")

if __name__ == "__main__":
    app.run(debug=True)
