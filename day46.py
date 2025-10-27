import os
import pyttsx3
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)   # speaking speed
engine.setProperty('volume', 1.0) # volume level

def speak(text):
    """Convert text to speech"""
    print(f"🤖 AI: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone input and return recognized text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print(f"🗣️ You said: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn’t understand that.")
            return ""
        except sr.RequestError:
            speak("Speech service error.")
            return ""

def chat_with_gpt(prompt):
    """Send user prompt to OpenAI and get reply"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a smart and friendly AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        return f"Error: {e}"

# --- MAIN PROGRAM LOOP ---
speak("Hello! I’m your AI voice assistant. Say something, or say 'exit' to quit.")

while True:
    user_input = listen().lower()

    if not user_input:
        continue

    if "exit" in user_input or "quit" in user_input or "bye" in user_input:
        speak("Goodbye! Have a great day.")
        break

    reply = chat_with_gpt(user_input)
    speak(reply)
