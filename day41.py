# day41_multilingual_caption_narrator.py
# AI Multilingual Caption Narrator – Caption + Translate + Speak
# Author: YourName

import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import pyttsx3
from googletrans import Translator
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize models
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
translator = Translator()
engine = pyttsx3.init()

engine.setProperty('rate', 160)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice

# GUI setup
root = tk.Tk()
root.title("AI Multilingual Caption Narrator")
root.geometry("650x700")
root.config(bg="#f0f9ff")

# Title
tk.Label(root, text="🌍 AI Multilingual Caption Narrator", font=("Helvetica", 18, "bold"), bg="#f0f9ff", fg="#003366").pack(pady=10)

# Image Display
img_label = tk.Label(root, bg="#f0f9ff")
img_label.pack(pady=10)

# Caption Label
caption_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12), bg="#f0f9ff", fg="#111")
caption_label.pack(pady=10)

translated_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12, "italic"), bg="#f0f9ff", fg="#007700")
translated_label.pack(pady=10)

caption_text = ""
translated_text = ""

# Language Dropdown
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

tk.Label(root, text="Choose Language:", bg="#f0f9ff", font=("Arial", 12, "bold")).pack()
lang_var = tk.StringVar(value="English")
lang_menu = ttk.Combobox(root, textvariable=lang_var, values=list(languages.keys()), state="readonly", font=("Arial", 12))
lang_menu.pack(pady=5)

# Upload & Generate Caption
def upload_image():
    global caption_text, translated_text
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        raw_image = Image.open(file_path).convert('RGB')
        img_display = raw_image.resize((400, 300))
        tk_image = ImageTk.PhotoImage(img_display)
        img_label.config(image=tk_image)
        img_label.image = tk_image

        # Generate Caption
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)
        caption_text = processor.decode(out[0], skip_special_tokens=True)
        caption_label.config(text=f"🖼️ Caption: {caption_text}")

        # Clear translation text
        translated_label.config(text="")

# Translate Caption
def translate_caption():
    global translated_text
    if caption_text:
        lang_code = languages[lang_var.get()]
        translated = translator.translate(caption_text, dest=lang_code)
        translated_text = translated.text
        translated_label.config(text=f"🌐 Translated ({lang_var.get()}): {translated_text}")
    else:
        translated_label.config(text="⚠️ Please generate a caption first!")

# Speak Caption
def speak_caption():
    text_to_speak = translated_text if translated_text else caption_text
    if text_to_speak:
        engine.say(text_to_speak)
        engine.runAndWait()
    else:
        engine.say("Please upload an image and generate caption first.")
        engine.runAndWait()

# Buttons
tk.Button(root, text="Upload Image", command=upload_image, bg="#007ACC", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(root, text="Translate Caption", command=translate_caption, bg="#FF9900", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(root, text="Speak Caption", command=speak_caption, bg="#00B050", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

root.mainloop()
