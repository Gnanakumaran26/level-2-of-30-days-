import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load AI model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Create main window
root = tk.Tk()
root.title("AI Image Caption Generator")
root.geometry("600x600")
root.config(bg="#eaf4fc")

# Title label
title_label = tk.Label(root, text="AI Image Caption Generator", font=("Helvetica", 18, "bold"), bg="#eaf4fc", fg="#003366")
title_label.pack(pady=10)

# Display image
img_label = tk.Label(root, bg="#eaf4fc")
img_label.pack(pady=10)

# Caption label
caption_label = tk.Label(root, text="", wraplength=500, font=("Arial", 12), bg="#eaf4fc", fg="#111")
caption_label.pack(pady=10)

# Function to select image
def upload_image():
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
        caption = processor.decode(out[0], skip_special_tokens=True)
        caption_label.config(text=f"🖼️ Caption: {caption}")

# Button
browse_button = tk.Button(root, text="Upload Image", command=upload_image, bg="#007ACC", fg="white", font=("Arial", 12, "bold"))
browse_button.pack(pady=20)

root.mainloop()
