import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 AI Assistant: Hello! Type 'exit' anytime to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("🤖 AI Assistant: Goodbye!")
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can use gpt-4 if available
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    ai_reply = response.choices[0].message.content
    print(f"🤖 AI Assistant: {ai_reply}\n")
