import faiss
import pickle
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# Load Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Load vector index and data
with open("retriever/vectorizer.pkl", "rb") as f:
    vectorizer: TfidfVectorizer = pickle.load(f)

index = faiss.read_index("retriever/faiss_index.idx")
with open("data/job_trends.json", "r") as f:
    job_data = json.load(f)

def retrieve_job_trends(goal: str):
    query_vec = vectorizer.transform([goal]).toarray().astype("float32")
    _, I = index.search(query_vec, 1)
    matched = job_data[I[0][0]]

    # Gemini Summary
    prompt = f"""Act as a career advisor. Given the following role and skill trend, summarize key insights:
    
    Role: {matched["role"]}
    Skills: {matched["skills"]}
    Market Trends: {matched["trends"]}

    Provide a short summary of:
    - Top in-demand skills
    - Why this role is trending
    - Suggested focus areas for newcomers
    """
    response = model.generate_content(prompt)
    return response.text
