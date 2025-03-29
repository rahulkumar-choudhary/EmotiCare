# app.py
from flask import Flask, render_template, request, jsonify
from utils.gemini_api import analyze_message
from utils.classify_disorder import classify_disorder
from utils.support_methods import get_support_methods
from utils.resources import get_nearby_resources, book_appointment
import os

app = Flask(__name__)

chat_history = []

# 🚀 Landing Page
@app.route('/')
def landing_page():
    return render_template('launch.html')

# 💬 Chat Page
@app.route('/chat')
def chat_page():
    return render_template('index.html')

# 📸 Webcam Face Detection Page
@app.route('/face-check')
def face_check():
    return render_template('face_check.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    chat_history.append({'role': 'user', 'text': user_input})

    analysis = analyze_message(user_input)
    disorder = classify_disorder(analysis)
    support_methods = get_support_methods(disorder)

    severe_distress_keywords = ['suicide', 'end it all', 'kill myself', 'hopeless', 'worthless', "can't go on", 'harm myself']
    is_urgent = any(kw in user_input.lower() for kw in severe_distress_keywords)

    if is_urgent:
        response = """
        <strong>🚨 It seems you're in deep distress.</strong><br>
        Please consider talking to a professional immediately.<br><br>
        <button onclick=\"showUrgentContactForm()\">📞 Contact a Human Counselor</button>
        """
    else:
        response = f"""
        I sense you're dealing with <strong>{disorder}</strong>.<br>
        Here are some support techniques:<br><br>{support_methods}<br><br>
        Would you like to:<br>
        <button onclick=\"showBookingForm()\">📅 Book an Appointment</button>
        <button onclick=\"showNotifyForm()\">📢 Notify a Mental Health Professional</button>
        """

    chat_history.append({'role': 'bot', 'text': response})
    return jsonify({'response': response, 'disorder': disorder, 'urgent': is_urgent})

@app.route('/resources', methods=['POST'])
def resources():
    data = request.json
    disorder = data['disorder']
    location = data['location']
    resources = get_nearby_resources(disorder, location)
    return jsonify({'resources': resources})

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    success = book_appointment(data['resource'], data['user_info'])
    return jsonify({'success': success})

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    print(f"Notifying provider: {data}")
    return jsonify({'notified': True})

@app.route('/urgent-contact', methods=['POST'])
def urgent_contact():
    data = request.json
    print(f"Urgent contact request: {data}")
    return jsonify({'escalated': True})

if __name__ == '__main__':
    app.run(debug=True)
