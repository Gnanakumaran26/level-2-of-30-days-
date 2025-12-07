from transformers import pipeline

# Load summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# -------------------------------------
# Summarize normal text
# -------------------------------------
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=60, do_sample=False)
    return summary[0]['summary_text']


# -------------------------------------
# Summarize YouTube video (captions)
# -------------------------------------
def summarize_youtube(video_id):
    from youtube_transcript_api import YouTubeTranscriptApi

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([t["text"] for t in transcript])

        print("\n📌 Extracting captions...")
        summary = summarize_text(full_text)
        return summary

    except Exception as e:
        return f"Error fetching transcript: {e}"


# -------------------------------------
# Main Program
# -------------------------------------
while True:
    print("\n--- AI SUMMARIZER TOOL ---")
    print("1. Summarize Text")
    print("2. Summarize YouTube Video")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("\nPaste your long text here:\n")
        print("\n⏳ Summarizing, please wait...")
        print("\nSUMMARY:\n")
        print(summarize_text(text))

    elif choice == "2":
        link = input("Enter YouTube Video ID (Example: dQw4w9WgXcQ): ")
        print("\n⏳ Fetching and summarizing...")
        print("\nSUMMARY:\n")
        print(summarize_youtube(link))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
