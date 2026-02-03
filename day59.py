import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(role, level):
    prompt = f"""
You are a professional technical interviewer.

Ask ONE interview question for:
Role: {role}
Level: {level}

Only give the question.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an experienced technical interviewer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


def evaluate_answer(question, answer):
    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:
1. Correctness
2. Missing points
3. Communication clarity
4. Score out of 10
5. Improvement suggestion

Return in clean bullet points.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a strict interview evaluator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# -------------------------------
# MAIN PROGRAM
# -------------------------------
if __name__ == "__main__":
    print("\n🎤 AI INTERVIEW SIMULATOR 🎤\n")

    role = input("Enter Role (Python / Data Science / AI / CS): ")
    level = input("Enter Level (Beginner / Intermediate / Advanced): ")

    print("\n🧠 Interview Question:\n")
    question = ask_question(role, level)
    print(question)

    answer = input("\n✍️ Your Answer:\n")

    print("\n⏳ Evaluating your answer...\n")
    feedback = evaluate_answer(question, answer)

    print("📊 INTERVIEW FEEDBACK\n")
    print(feedback)

    print("\n✅ Interview simulation completed.")
