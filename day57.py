import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an AI Resume Analyzer.

TASKS:
1. Analyze the resume.
2. Compare it with the job description.
3. Calculate skill match percentage.
4. List missing skills.
5. Give improvement suggestions.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return output in this format:
- Skill Match Percentage:
- Matched Skills:
- Missing Skills:
- Suggestions:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert HR and AI resume evaluator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    print("📄 AI RESUME ANALYZER 📄\n")

    print("Paste your RESUME text (end with ENTER):")
    resume = input("\nResume:\n")

    print("\nPaste JOB DESCRIPTION text:")
    job_desc = input("\nJob Description:\n")

    print("\n⏳ Analyzing Resume...\n")
    result = analyze_resume(resume, job_desc)

    print("📊 ANALYSIS RESULT\n")
    print(result)
