import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

def analyze_message(message):
    prompt = f"""
    You are a compassionate mental health assistant.

    Analyze the user message below and return:
    1. Emotional Tone (sad, anxious, hopeful, etc.)
    2. Likely Mental Health Concern (e.g., anxiety, depression, stress)
    3. Short Reasoning

    Message:
    \"{message}\"

    Format:
    Emotion: <tone>
    Disorder: <diagnosis>
    Reasoning: <why>
    """
    response = model.generate_content([prompt])
    return response.text.strip()



# import google.generativeai as genai
# import os

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-pro")

# def analyze_message(message):
#     prompt = f"""
#     You are a compassionate mental health assistant.

#     Analyze the user message below and return:
#     1. Emotional Tone (sad, anxious, hopeful, etc.)
#     2. Likely Mental Health Concern (e.g., anxiety, depression, stress)
#     3. Short Reasoning

#     Message:
#     \"{message}\"

#     Format:
#     Emotion: <tone>
#     Disorder: <diagnosis>
#     Reasoning: <why>
#     """
#     response = model.generate_content([prompt])  # ✅ Must be passed as a list
#     return response.text.strip()
