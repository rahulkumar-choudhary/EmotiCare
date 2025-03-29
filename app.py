from flask import Flask, render_template, request, jsonify
from utils.gemini_api import analyze_message
from utils.classify_disorder import classify_disorder
from utils.support_methods import get_support_methods
from utils.resources import get_nearby_resources, book_appointment
import os

app = Flask(__name__)

chat_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    chat_history.append({'role': 'user', 'text': user_input})

    analysis = analyze_message(user_input)
    disorder = classify_disorder(analysis)
    support_methods = get_support_methods(disorder)

    response = f"I sense you're dealing with <strong>{disorder}</strong>. Here are some support techniques:<br><br>{support_methods}"

    chat_history.append({'role': 'bot', 'text': response})
    return jsonify({'response': response, 'disorder': disorder})

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

if __name__ == '__main__':
    app.run(debug=True)