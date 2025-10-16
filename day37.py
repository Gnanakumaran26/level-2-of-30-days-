from transformers import pipeline

# Load pre-trained sentiment-analysis model
sentiment_model = pipeline("sentiment-analysis")

# Take input
text = input("Enter a sentence: ")

# Predict sentiment
result = sentiment_model(text)

# Display result
print(f"\nText: {text}")
print(f"Sentiment: {result[0]['label']}")
print(f"Confidence: {result[0]['score']:.2f}")
