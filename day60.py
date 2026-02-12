import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TASK_FILE = "tasks.txt"

# -------------------------------
# AI Function
# -------------------------------
def ask_ai(system_role, user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content


# -------------------------------
# Task Manager
# -------------------------------
def add_task(task):
    with open(TASK_FILE, "a") as f:
        f.write(f"{datetime.now()} - {task}\n")
    print("✅ Task added!")

def view_tasks():
    if not os.path.exists(TASK_FILE):
        print("No tasks yet.")
        return
    with open(TASK_FILE, "r") as f:
        print("\n--- Your Tasks ---")
        print(f.read())


# -------------------------------
# Features
# -------------------------------
def ai_chat():
    user_input = input("Ask AI anything: ")
    reply = ask_ai("You are a helpful assistant.", user_input)
    print("\nAI Reply:\n", reply)

def resume_analyzer():
    resume = input("Paste Resume: ")
    job = input("Paste Job Description: ")
    prompt = f"Compare resume with job description and give match %, missing skills and suggestions.\nResume:{resume}\nJob:{job}"
    reply = ask_ai("You are an HR expert.", prompt)
    print("\nAnalysis:\n", reply)

def code_reviewer():
    code = input("Paste your code: ")
    prompt = f"Review this code and give bugs, improvements and score.\n{code}"
    reply = ask_ai("You are a senior software engineer.", prompt)
    print("\nCode Review:\n", reply)

def interview_simulator():
    role = input("Role: ")
    level = input("Level: ")
    question = ask_ai("You are an interviewer.", f"Ask one {level} question for {role}.")
    print("\nInterview Question:\n", question)
    answer = input("\nYour Answer: ")
    feedback = ask_ai("You are a strict evaluator.", f"Evaluate this answer:\nQuestion:{question}\nAnswer:{answer}")
    print("\nFeedback:\n", feedback)


# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    while True:
        print("\n========== AI PRODUCTIVITY SUITE ==========")
        print("1. AI Chat")
        print("2. Task Manager")
        print("3. Resume Analyzer")
        print("4. Code Reviewer")
        print("5. Interview Simulator")
        print("6. Exit")
        print("===========================================")

        choice = input("Choose option: ")

        if choice == "1":
            ai_chat()
        elif choice == "2":
            sub = input("1. Add Task\n2. View Tasks\nChoose: ")
            if sub == "1":
                task = input("Enter task: ")
                add_task(task)
            elif sub == "2":
                view_tasks()
        elif choice == "3":
            resume_analyzer()
        elif choice == "4":
            code_reviewer()
        elif choice == "5":
            interview_simulator()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
