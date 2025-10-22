# day42_ai_image_story_generator.py
# AI Image Story Generator – Creates a short story from an image
# Author: YourName

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline

# Load AI models
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Text-generation model for storytelling
story_generator = pipeline("text-generation", model="gpt2")

# GUI setup
root = tk.Tk()
root.title("AI Image Story Generator")
root.geometry("650x700")
root.config(bg="#f0f9ff")

# Title
tk.Label(root, text="📖 AI Image Story Generator", font=("Helvetica", 18, "bold"), bg="#f0f9ff", fg="#003366").pack(pady=10)

# Image Display
img_label = tk.Label(root, bg="#f0f9ff")
img_label.pack(pady=10)

# Caption and Story Labels
caption_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12, "italic"), bg="#f0f9ff", fg="#333")
caption_label.pack(pady=10)

story_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12), bg="#f0f9ff", fg="#111")
story_label.pack(pady=10)

caption_text = ""
story_text = ""

# Upload and Generate
def upload_image():
    global caption_text, story_text
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        raw_image = Image.open(file_path).convert('RGB')
        img_display = raw_image.resize((400, 300))
        tk_image = ImageTk.PhotoImage(img_display)
        img_label.config(image=tk_image)
        img_label.image = tk_image

        # Step 1: Generate Caption
        inputs = caption_processor(raw_image, return_tensors="pt")
        out = caption_model.generate(**inputs)
        caption_text = caption_processor.decode(out[0], skip_special_tokens=True)
        caption_label.config(text=f"🖼️ Caption: {caption_text}")

        # Step 2: Generate Story
        prompt = f"Write a short creative story about this scene: {caption_text}. Story:"
        story_output = story_generator(prompt, max_length=80, num_return_sequences=1, temperature=0.8)
        story_text = story_output[0]['generated_text']
        story_label.config(text=f"📖 Story:\n{story_text}")

# Button
upload_btn = tk.Button(root, text="Upload Image & Generate Story", command=upload_image, bg="#007ACC", fg="white", font=("Arial", 12, "bold"))
upload_btn.pack(pady=20)

root.mainloop()
