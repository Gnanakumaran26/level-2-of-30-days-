import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say("Hello! I am your voice calculator. Please say your calculation.")
engine.runAndWait()

# Recognizer instance
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said:", command)

            if "exit" in command.lower() or "stop" in command.lower():
                engine.say("Goodbye!")
                engine.runAndWait()
                break

            # Replace words with mathematical symbols
            command = command.replace("plus", "+")
            command = command.replace("minus", "-")
            command = command.replace("times", "*")
            command = command.replace("divided by", "/")
            command = command.replace("into", "*")

            result = eval(command)
            print("Result:", result)

            engine.say(f"The result is {result}")
            engine.runAndWait()

        except Exception as e:
            print("Sorry, I didn't catch that.", e)
            engine.say("Sorry, I didn’t understand. Please try again.")
            engine.runAndWait()
