import google.generativeai as genai
import pyttsx3
import time
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Try to initialize text-to-speech engine (optional)
try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    tts_available = True
    print("Text-to-speech initialized successfully")
except Exception as e:
    print(f"Text-to-speech not available: {e}")
    tts_available = False

THERAPEUTIC_PROMPT = """
You are Timothy ai assistant of emoticare, a text-based therapeutic assistant. Your role is to:
- Provide empathetic and supportive responses to the user
- Use a calm, warm tone in your language
- Ask thoughtful follow-up questions when appropriate
- Validate the user's feelings and experiences
- Practice active listening through your responses
- Offer gentle perspectives and coping strategies when helpful
- Avoid making medical diagnoses or prescribing treatments
- Prioritize user safety - suggest professional help when needed
- Keep responses concise and conversational (1-3 sentences)
- Respect the user's autonomy and perspective

User message: {query}
"""

class TherapyAssistant:
    def __init__(self):
        self.conversation_history = []

    def speak(self, text):
        print(f"Timothy: {text}")
        if tts_available:
            try:
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print(f"Speech error: {e}")

    def generate_therapeutic_response(self, query):
        try:
            context = ""
            if self.conversation_history:
                recent_history = self.conversation_history[-5:]
                for speaker, message in recent_history:
                    context += f"{speaker}: {message}\n"

            full_prompt = THERAPEUTIC_PROMPT.format(query=query)
            if context:
                full_prompt = f"Recent conversation:\n{context}\n\n{full_prompt}"

            print("Generating response...")
            model = genai.GenerativeModel("gemini-1.5-pro")
            response = model.generate_content(
                full_prompt,
                generation_config=genai.GenerationConfig(
                    max_output_tokens=150,
                    temperature=0.2,
                )
            )

            response_text = response.text
            self.conversation_history.append(("Timothy", response_text))
            return response_text
        except Exception as e:
            print(f"Response generation error: {e}")
            error_msg = f"I'm having trouble formulating a response right now. Could we try again in a moment? Technical details: {str(e)}"
            self.conversation_history.append(("Timothy", error_msg))
            return error_msg

    def chat_session(self):
        greeting = "Hello, I'm Timothy im an AI assistant from Emoticare. I'm here to listen and talk with you. How are you feeling today?"
        print(f"\nTimothy: {greeting}")
        self.conversation_history.append(("Timothy", greeting))
        if tts_available:
            self.speak(greeting)

        print("\n--- Chat Session Started ---")
        print("Type your messages and press Enter to send.")
        print("Type 'exit', 'quit', or 'bye' to end the session.\n")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye', 'end']:
                farewell = "It was good talking with you. Remember to take care of yourself. Goodbye for now."
                print(f"\nTimothy: {farewell}")
                self.conversation_history.append(("Timothy", farewell))
                if tts_available:
                    self.speak(farewell)
                break

            if not user_input:
                print("Please type a message.")
                continue

            self.conversation_history.append(("You", user_input))

            response = self.generate_therapeutic_response(user_input)
            if tts_available:
                self.speak(response)
            else:
                print(f"Timothy: {response}")

        print("\n--- Chat Session Ended ---")

def main():
    print("\n========================================")
    print("Timothy - Therapeutic Text Assistant")
    print("========================================\n")

    assistant = TherapyAssistant()

    print("Welcome to Timothy, your therapeutic chatbot.")
    print("You can type messages to Timothy, and he'll respond with")
    print("supportive, therapeutic answers.\n")

    assistant.chat_session()

    print("\nThank you for using Timothy. Take care!")

if __name__ == "__main__":
    main()