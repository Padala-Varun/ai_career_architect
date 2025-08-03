import plotly.express as px
import streamlit as st

def show_career_timeline(stages):
    fig = px.timeline(
        x_start=[s["start"] for s in stages],
        x_end=[s["end"] for s in stages],
        y=[s["title"] for s in stages],
        color=[s["category"] for s in stages]
    )
    st.plotly_chart(fig)
