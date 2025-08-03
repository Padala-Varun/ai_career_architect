import datetime
import streamlit as st
import plotly.express as px

def build_roadmap(role: str):
    role = role.lower()
    now = datetime.datetime.now()

    if "data scientist" in role:
        stages = [
            {"title": "Learning Foundations", "duration_months": 6, "focus": "Python, ML, SQL, Statistics"},
            {"title": "Junior Data Scientist", "duration_months": 12, "focus": "Projects, Model Building, EDA"},
            {"title": "Mid-Level DS", "duration_months": 18, "focus": "NLP, GenAI, Production Pipelines"},
            {"title": "Senior DS / Lead", "duration_months": 24, "focus": "Team Leadership, MLOps, Strategy"}
        ]
    elif "frontend" in role:
        stages = [
            {"title": "Learn Frontend Basics", "duration_months": 4, "focus": "HTML, CSS, JavaScript"},
            {"title": "React Developer", "duration_months": 10, "focus": "React, APIs, Tailwind"},
            {"title": "Senior Frontend Dev", "duration_months": 18, "focus": "Architecture, Testing, Perf Optimization"},
            {"title": "Frontend Lead / UI Architect", "duration_months": 24, "focus": "System Design, Team Management"}
        ]
    else:
        stages = [
            {"title": "Understand AI/LLMs", "duration_months": 6, "focus": "Prompting, LLMs, Market Trends"},
            {"title": "AI Product Specialist", "duration_months": 12, "focus": "MVPs, Stakeholders, Roadmapping"},
            {"title": "AI Product Manager", "duration_months": 18, "focus": "Data Strategy, Metrics, GenAI Tools"},
            {"title": "Senior PM / Director", "duration_months": 24, "focus": "Team Building, Vision, GTM"}
        ]

    # Compute start/end dates
    date_cursor = now
    for stage in stages:
        stage["start"] = date_cursor
        stage["end"] = date_cursor + datetime.timedelta(days=30 * stage["duration_months"])
        date_cursor = stage["end"]
    return stages

def visualize(stages):
    fig = px.timeline(
        stages,
        x_start="start",
        x_end="end",
        y="title",
        color="title",
        hover_data=["focus"]
    )
    fig.update_layout(title="🚀 Career Roadmap Timeline", showlegend=False)
    st.plotly_chart(fig)
