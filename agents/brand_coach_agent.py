import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_branding(profile: dict, gap_data: dict):
    name = profile["name"]
    goal = profile["goal"]
    skills = ", ".join(profile["skills"])
    interests = ", ".join(profile["interests"])
    missing = ", ".join(gap_data["missing"]) if gap_data else ""

    prompt = f"""
You are a personal brand strategist. Help create branding content for this individual:

Name: {name}
Career Goal: {goal}
Current Skills: {skills}
Interests: {interests}
Skill Gaps: {missing}

Generate the following:
1. A strong LinkedIn Bio (3–4 lines)
2. A personal summary for the top of their resume
3. 2 branding tips or strategies
4. Optional: One idea for a personal portfolio project related to their goal
"""

    response = model.generate_content(prompt)
    return response.text
