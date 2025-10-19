from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image
image_path = "your_image.jpg"  # Replace with image filename
raw_image = Image.open(image_path).convert('RGB')

# Process image
inputs = processor(raw_image, return_tensors="pt")

# Generate caption
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

print(f"🖼️ Image Caption: {caption}")
