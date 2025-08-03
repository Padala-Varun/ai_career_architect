import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

def inspire(profile):
    name = profile["name"]
    goal = profile["goal"]

    prompt = f"""
Act as a friendly motivator for someone named {name} working toward becoming a {goal}.

Return:
1. An inspiring quote
2. One motivational message in 2–3 sentences
3. A healthy daily habit or mindset they should adopt
"""

    response = model.generate_content(prompt)
    return response.text
