# day40_ai_voice_caption_narrator.py
# AI Voice Caption Narrator – Combines Image Captioning + Voice Output

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pyttsx3
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice

# Create GUI window
root = tk.Tk()
root.title("AI Voice Caption Narrator")
root.geometry("600x650")
root.config(bg="#eef6f9")

# Title
title_label = tk.Label(root, text="AI Voice Caption Narrator", font=("Helvetica", 18, "bold"), bg="#eef6f9", fg="#003366")
title_label.pack(pady=10)

# Image display area
img_label = tk.Label(root, bg="#eef6f9")
img_label.pack(pady=10)

# Caption label
caption_label = tk.Label(root, text="", wraplength=500, font=("Arial", 12), bg="#eef6f9", fg="#111")
caption_label.pack(pady=15)

caption_text = ""

# Function to upload and generate caption
def upload_image():
    global caption_text
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        raw_image = Image.open(file_path).convert('RGB')
        img_display = raw_image.resize((400, 300))
        tk_image = ImageTk.PhotoImage(img_display)
        img_label.config(image=tk_image)
        img_label.image = tk_image

        # Generate caption
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)
        caption_text = processor.decode(out[0], skip_special_tokens=True)

        caption_label.config(text=f"🖼️ Caption: {caption_text}")

# Function to speak caption
def speak_caption():
    if caption_text:
        engine.say(caption_text)
        engine.runAndWait()
    else:
        engine.say("Please upload an image first.")
        engine.runAndWait()

# Buttons
upload_btn = tk.Button(root, text="Upload Image", command=upload_image, bg="#007ACC", fg="white", font=("Arial", 12, "bold"))
upload_btn.pack(pady=10)

speak_btn = tk.Button(root, text="Speak Caption", command=speak_caption, bg="#00B050", fg="white", font=("Arial", 12, "bold"))
speak_btn.pack(pady=10)

root.mainloop()
