import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    return ""

def get_user_profile():
    st.title("🎯 AI Career Architect")
    st.subheader("👤 Let's get to know you")

    name = st.text_input("Your Name")
    goal = st.text_input("Your Career Goal (e.g., Data Scientist)")
    skills = st.text_area("List your current skills (comma-separated)")
    interests = st.text_area("List your interests (comma-separated)")
    resume_file = st.file_uploader("📄 Upload your resume (PDF optional)", type=["pdf"])

    if st.button("Submit"):
        resume_text = extract_text_from_pdf(resume_file) if resume_file else ""
        return {
            "name": name,
            "goal": goal,
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "interests": [i.strip() for i in interests.split(",") if i.strip()],
            "resume_text": resume_text
        }
    return None
