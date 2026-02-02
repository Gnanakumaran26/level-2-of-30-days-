import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code(code, language="Python"):
    prompt = f"""
You are a senior software engineer and code reviewer.

Review the following {language} code and provide:
1. Bugs or errors
2. Security issues (if any)
3. Performance improvements
4. Clean code suggestions
5. Overall code quality score (out of 10)

CODE:
{code}

Return in this format:
- Bugs:
- Security Issues:
- Performance:
- Code Style:
- Final Score:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a strict but helpful senior code reviewer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    print("🧑‍💻 AI CODE REVIEWER\n")

    print("Paste your code below (press ENTER when done):\n")
    user_code = input()

    print("\n⏳ Reviewing code...\n")
    result = review_code(user_code)

    print("📋 CODE REVIEW RESULT\n")
    print(result)
