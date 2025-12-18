import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------------
# GUI Window
# -------------------------------
root = tk.Tk()
root.title("AI Chat Assistant")
root.geometry("600x650")
root.config(bg="#0f172a")

# -------------------------------
# Title
# -------------------------------
title = tk.Label(
    root,
    text="🤖 AI Chat Assistant",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=10)

# -------------------------------
# Chat Area
# -------------------------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=70,
    height=25,
    font=("Consolas", 11),
    bg="#020617",
    fg="white"
)
chat_area.pack(padx=10, pady=10)
chat_area.config(state=tk.DISABLED)

# -------------------------------
# Input Area
# -------------------------------
user_input = tk.Entry(
    root,
    font=("Arial", 13),
    width=45
)
user_input.pack(side=tk.LEFT, padx=10, pady=10)

# -------------------------------
# Functions
# -------------------------------
def send_message():
    msg = user_input.get()
    if msg.strip() == "":
        return

    user_input.delete(0, tk.END)
    time = datetime.now().strftime("%H:%M")

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You [{time}]: {msg}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    get_ai_reply(msg)

def get_ai_reply(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content
        time = datetime.now().strftime("%H:%M")

        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"AI [{time}]: {reply}\n\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)

    except Exception as e:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Error: {e}\n")
        chat_area.config(state=tk.DISABLED)

# -------------------------------
# Buttons
# -------------------------------
send_btn = tk.Button(
    root,
    text="Send",
    font=("Arial", 12, "bold"),
    width=10,
    command=send_message,
    bg="#2563eb",
    fg="white"
)
send_btn.pack(side=tk.RIGHT, padx=10)

# Enter key shortcut
root.bind("<Return>", lambda event: send_message())

# -------------------------------
# Start App
# -------------------------------
root.mainloop()
