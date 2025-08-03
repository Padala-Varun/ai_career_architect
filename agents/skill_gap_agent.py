import streamlit as st
import plotly.graph_objects as go

def analyze(user_skills: list, required_skills_text: str):
    # Normalize and extract skills
    required_skills = [s.strip().lower() for s in required_skills_text.split(",") if s.strip()]
    user_skills = [s.strip().lower() for s in user_skills]

    matched = [skill for skill in required_skills if skill in user_skills]
    missing = [skill for skill in required_skills if skill not in user_skills]

    return {
        "matched": matched,
        "missing": missing,
        "required": required_skills,
        "user": user_skills
    }

def visualize_gap(gap_data: dict):
    labels = gap_data["required"]
    user_score = [1 if skill in gap_data["user"] else 0 for skill in labels]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=user_score,
        theta=labels,
        fill='toself',
        name='Your Skill Coverage',
        line=dict(color="royalblue")
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1])
        ),
        showlegend=True,
        title="🧠 Skill Coverage Radar"
    )

    st.plotly_chart(fig)
