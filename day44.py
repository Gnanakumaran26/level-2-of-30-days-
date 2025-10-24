import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()
engine.say("Hello! I am your personal assistant.")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except:
            speak("Sorry, I didn't catch that.")
            return ""

while True:
    speak("How can I help you?")
    query = listen()

    if "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in query:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open github" in query:
        webbrowser.open("https://github.com")
        speak("Opening GitHub")

    elif "play music" in query:
        music_folder = "C:/Users/YourName/Music"
        songs = os.listdir(music_folder)
        os.startfile(os.path.join(music_folder, songs[0]))
        speak("Playing music")

    elif "exit" in query or "stop" in query or "bye" in query:
        speak("Goodbye! Have a great day.")
        break

    else:
        speak("Sorry, I don’t know that command.")
