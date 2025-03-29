def get_support_methods(disorder):
    methods = {
        "Anxiety": "Try deep breathing, mindfulness meditation, and journaling.",
        "Depression": "Maintain a routine, talk to someone, get sunlight daily.",
        "Stress": "Do short walks, take breaks, use progressive muscle relaxation.",
        "General Emotional Concern": "Practice gratitude journaling and positive affirmations."
    }
    return methods.get(disorder, methods["General Emotional Concern"])
