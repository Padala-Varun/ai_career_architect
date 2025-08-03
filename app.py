from agents import user_input_agent, job_trend_agent, skill_gap_agent, career_path_agent, brand_coach_agent, motivator_agent
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import time

# Page Configuration
st.set_page_config(
    page_title="AI Career Architect", 
    layout="wide",
    page_icon="🚀",
    initial_sidebar_state="expanded"
)

# Advanced CSS with animations and premium styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;900&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Global Styles with Advanced Theming */
    .main {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1b3a 25%, #2d1b69 50%, #0f0f23 100%);
        min-height: 100vh;
        overflow-x: hidden;
        position: relative;
    }
    
    /* Animated Background Particles */
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.1) 0%, transparent 50%);
        animation: backgroundShift 20s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes backgroundShift {
        0%, 100% { transform: scale(1) rotate(0deg); }
        33% { transform: scale(1.1) rotate(5deg); }
        66% { transform: scale(0.9) rotate(-5deg); }
    }
    
    .stApp {
        background: transparent;
    }
    
    /* Premium Header with Advanced Animations */
    .hero-header {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 30px;
        margin-bottom: 3rem;
        backdrop-filter: blur(20px);
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 0 40px rgba(120, 119, 198, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
        animation: heroGlow 8s ease-in-out infinite;
    }
    
    .hero-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.03), transparent);
        animation: shimmer 10s linear infinite;
        pointer-events: none;
    }
    
    @keyframes heroGlow {
        0%, 100% { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 0 40px rgba(120, 119, 198, 0.1); }
        50% { box-shadow: 0 25px 80px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 0 60px rgba(120, 119, 198, 0.2); }
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%); }
        100% { transform: translateX(100%) translateY(100%); }
    }
    
    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ffffff 0%, #a78bfa 30%, #06b6d4 70%, #ffffff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: 0 10px 30px rgba(167, 139, 250, 0.3);
        animation: titlePulse 4s ease-in-out infinite;
        letter-spacing: -0.02em;
        position: relative;
        z-index: 1;
    }
    
    @keyframes titlePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: rgba(255, 255, 255, 0.8);
        font-weight: 300;
        letter-spacing: 0.5px;
        margin-bottom: 0;
        animation: subtitleFade 3s ease-in-out infinite alternate;
        position: relative;
        z-index: 1;
    }
    
    @keyframes subtitleFade {
        0% { opacity: 0.8; }
        100% { opacity: 1; }
    }
    
    /* Premium Card System */
    .insight-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
        padding: 2.5rem;
        border-radius: 24px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin: 1.5rem 0;
        position: relative;
        overflow: hidden;
        transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    .insight-card::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #00f2fe);
        border-radius: 26px;
        z-index: -1;
        opacity: 0;
        transition: opacity 0.6s ease;
        background-size: 300% 300%;
        animation: gradientShift 8s ease infinite;
    }
    
    .insight-card:hover::before {
        opacity: 1;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .insight-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 40px 80px rgba(0, 0, 0, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            0 0 60px rgba(102, 126, 234, 0.3);
    }
    
    .card-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        position: relative;
    }
    
    .card-icon {
        font-size: 2.5rem;
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: iconBounce 2s ease-in-out infinite;
        filter: drop-shadow(0 4px 8px rgba(102, 126, 234, 0.3));
    }
    
    @keyframes iconBounce {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    /* Advanced Skill Badge System */
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 50px;
        margin: 0.4rem;
        font-size: 0.95rem;
        font-weight: 600;
        box-shadow: 
            0 8px 25px rgba(102, 126, 234, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
        overflow: hidden;
        cursor: pointer;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .skill-badge::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.6s;
    }
    
    .skill-badge:hover::before {
        left: 100%;
    }
    
    .skill-badge:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 
            0 15px 35px rgba(102, 126, 234, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }
    
    .missing-skill {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        box-shadow: 
            0 8px 25px rgba(255, 107, 107, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    .missing-skill:hover {
        box-shadow: 
            0 15px 35px rgba(255, 107, 107, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }
    
    /* Premium Timeline */
    .timeline-item {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.03) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 6px solid transparent;
        border-image: linear-gradient(45deg, #667eea, #764ba2, #f093fb) 1;
        backdrop-filter: blur(10px);
        position: relative;
        transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
        overflow: hidden;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 6px;
        height: 100%;
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        animation: progressGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes progressGlow {
        0% { box-shadow: 0 0 10px rgba(102, 126, 234, 0.5); }
        100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.8); }
    }
    
    .timeline-item:hover {
        transform: translateX(10px);
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.06) 100%);
    }
    
    .timeline-title {
        font-weight: 700;
        color: #ffffff;
        font-size: 1.3rem;
        margin-bottom: 0.8rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .timeline-date {
        color: rgba(255, 255, 255, 0.7);
        font-size: 1rem;
        margin-bottom: 0.8rem;
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* Premium Welcome Message */
    .welcome-message {
        background: linear-gradient(135deg, #00b894 0%, #00a085 50%, #00896b 100%);
        color: white;
        padding: 2rem;
        border-radius: 24px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 2rem 0;
        box-shadow: 
            0 20px 50px rgba(0, 184, 148, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
        animation: welcomePulse 6s ease-in-out infinite;
    }
    
    @keyframes welcomePulse {
        0%, 100% { transform: scale(1); box-shadow: 0 20px 50px rgba(0, 184, 148, 0.4); }
        50% { transform: scale(1.01); box-shadow: 0 25px 60px rgba(0, 184, 148, 0.6); }
    }
    
    /* Advanced Motivation Card */
    .motivation-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 50%, #ff9a9e 100%);
        padding: 2.5rem;
        border-radius: 24px;
        text-align: center;
        box-shadow: 
            0 20px 50px rgba(252, 182, 159, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
        animation: motivationFloat 8s ease-in-out infinite;
    }
    
    @keyframes motivationFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .motivation-text {
        font-size: 1.2rem;
        font-style: italic;
        color: #8b4513;
        font-weight: 500;
        text-shadow: 0 2px 4px rgba(255, 255, 255, 0.5);
        line-height: 1.6;
    }
    
    /* Premium Expandable Sections */
    .stExpander {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.03) 100%);
        border-radius: 16px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
    }
    
    .stExpander:hover {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.06) 100%);
        transform: translateY(-2px);
    }
    
    /* Advanced Text Styling */
    .content-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        line-height: 1.7;
        font-weight: 400;
    }
    
    .highlight-text {
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
    }
    
    /* Landing Page Premium Styling */
    .landing-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.03) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 4rem;
        text-align: center;
        position: relative;
        overflow: hidden;
        animation: landingFloat 10s ease-in-out infinite;
    }
    
    @keyframes landingFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-10px) rotate(0.5deg); }
        66% { transform: translateY(5px) rotate(-0.5deg); }
    }
    
    .cta-button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1.5rem 3rem;
        border-radius: 50px;
        display: inline-block;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .cta-button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 20px 50px rgba(102, 126, 234, 0.6);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title { font-size: 2.5rem; }
        .hero-subtitle { font-size: 1.1rem; }
        .insight-card { padding: 1.5rem; margin: 1rem 0; }
        .card-header { font-size: 1.4rem; }
    }
    
    /* Loading Animation */
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        border-top-color: #667eea;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2, #667eea);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section with Advanced Animations
st.markdown("""
<div class="hero-header">
    <h1 class="hero-title">🚀 AI Career Architect</h1>
    <p class="hero-subtitle">Transform your career journey with AI-powered insights and personalized roadmaps</p>
</div>
""", unsafe_allow_html=True)

# Get user input
profile = user_input_agent.get_user_profile()

if profile:
    # Animated Welcome Message
    st.markdown(f"""
    <div class="welcome-message">
        🎉 Welcome aboard, {profile['name']}! Let's architect your dream career together
        <div style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">
            Initializing your personalized career intelligence...
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state["profile"] = profile
    
    # Create columns for premium layout
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        # Job Market Insights with Premium Styling
        st.markdown("""
        <div class="insight-card">
            <div class="card-header">
                <span class="card-icon">📊</span>
                <span>Job Market Intelligence</span>
            </div>
        """, unsafe_allow_html=True)
        
        with st.spinner("Analyzing market trends..."):
            trend_summary = job_trend_agent.retrieve_job_trends(profile["goal"])
        
        st.markdown(f'<div class="content-text">{trend_summary}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Advanced Skill Gap Analysis
        st.markdown("""
        <div class="insight-card">
            <div class="card-header">
                <span class="card-icon">🧠</span>
                <span>AI-Powered Skill Analysis</span>
            </div>
        """, unsafe_allow_html=True)

        # Determine required skills based on goal
        if "data scientist" in profile["goal"].lower():
            required_skills = "Python, Machine Learning, SQL, Deep Learning, Data Visualization, NLP, GenAI"
        elif "frontend" in profile["goal"].lower():
            required_skills = "React, TypeScript, REST APIs, Tailwind, Webpack"
        else:
            required_skills = "LLMs, Prompt Engineering, Roadmapping, Stakeholder Communication, Product Metrics"

        with st.spinner("Computing skill gaps..."):
            gap_data = skill_gap_agent.analyze(profile["skills"], required_skills)
        
        # Display matched skills with animations
        if gap_data['matched']:
            st.markdown('<p class="highlight-text" style="font-weight: 700; font-size: 1.1rem; margin-bottom: 1rem;">✅ Your Power Skills:</p>', unsafe_allow_html=True)
            skills_html = ''.join([f'<span class="skill-badge">{skill}</span>' for skill in gap_data['matched']])
            st.markdown(f'<div style="margin-bottom: 2rem;">{skills_html}</div>', unsafe_allow_html=True)
        
        # Display missing skills with premium styling
        if gap_data['missing']:
            st.markdown('<p class="highlight-text" style="font-weight: 700; font-size: 1.1rem; margin-bottom: 1rem;">🎯 Growth Opportunities:</p>', unsafe_allow_html=True)
            missing_skills_html = ''.join([f'<span class="skill-badge missing-skill">{skill}</span>' for skill in gap_data['missing']])
            st.markdown(f'<div style="margin-bottom: 2rem;">{missing_skills_html}</div>', unsafe_allow_html=True)

        with st.spinner("Generating visualizations..."):
            skill_gap_agent.visualize_gap(gap_data)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Premium Career Roadmap
        st.markdown("""
        <div class="insight-card">
            <div class="card-header">
                <span class="card-icon">📈</span>
                <span>Personalized Career Trajectory</span>
            </div>
        """, unsafe_allow_html=True)

        with st.spinner("Building your roadmap..."):
            path = career_path_agent.build_roadmap(profile["goal"])
            career_path_agent.visualize(path)

        st.markdown('<h4 class="highlight-text" style="font-size: 1.4rem; margin: 2rem 0 1.5rem 0;">🧩 Strategic Milestones:</h4>', unsafe_allow_html=True)
        
        for i, stage in enumerate(path):
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-title">Phase {i+1}: {stage['title']}</div>
                <div class="timeline-date">{stage['start'].date()} → {stage['end'].date()}</div>
                <div class="content-text">{stage['focus']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Premium Brand Strategy
        st.markdown("""
        <div class="insight-card">
            <div class="card-header">
                <span class="card-icon">🎨</span>
                <span>Brand Strategy</span>
            </div>
        """, unsafe_allow_html=True)

        with st.spinner("Crafting your brand..."):
            brand_text = brand_coach_agent.generate_branding(profile, gap_data)
        
        st.markdown(f'<div class="content-text">{brand_text}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Advanced Motivation Section
        st.markdown("""
        <div class="motivation-card">
            <div style="font-size: 2rem; margin-bottom: 1.5rem;">🌟</div>
        """, unsafe_allow_html=True)
        
        with st.spinner("Generating motivation..."):
            motivation = motivator_agent.inspire(profile)
        
        st.markdown(f'<div class="motivation-text">"{motivation}"</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Premium Expandable Sections
    st.markdown('<div style="margin-top: 3rem;"></div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2, gap="large")
    
    with col3:
        with st.expander("📄 LinkedIn Bio Optimization", expanded=False):
            bio = f"""
            <div class="content-text">
            🚀 <strong>{profile['goal']} | Transforming Ideas into Impact</strong><br><br>
            
            Passionate technologist with expertise in <span class="highlight-text">{', '.join(gap_data['matched'][:3]) if gap_data['matched'] else 'emerging technologies'}</span>. 
            Currently expanding skills in <span class="highlight-text">{', '.join(gap_data['missing'][:2]) if gap_data['missing'] else 'cutting-edge technologies'}</span> 
            to drive innovation in the tech industry.<br><br>
            
            💡 <em>"Building the future, one line of code at a time"</em><br><br>
            
            #TechCareer #Innovation #AI #CareerGrowth
            </div>
            """
            st.markdown(bio, unsafe_allow_html=True)
    
    with col4:
        with st.expander("🎯 Resume Summary Generator", expanded=False):
            summary = f"""
            <div class="content-text">
            <strong>Dynamic {profile['goal']} Professional</strong><br><br>
            
            Results-driven technology professional with strong foundation in <span class="highlight-text">{', '.join(gap_data['matched'][:4]) if gap_data['matched'] else 'core technologies'}</span>. 
            Demonstrated ability to learn and adapt quickly, currently advancing expertise in 
            <span class="highlight-text">{', '.join(gap_data['missing'][:3]) if gap_data['missing'] else 'emerging technologies'}</span> 
            to stay ahead of industry trends.<br><br>
            
            <strong>Key Strengths:</strong><br>
            • Technical proficiency and continuous learning mindset<br>
            • Problem-solving and analytical thinking<br>
            • Passion for innovation and technology advancement<br>
            • Strong foundation for {profile['goal'].lower()} role
            </div>
            """
            st.markdown(summary, unsafe_allow_html=True)

else:
    # Premium Landing Page
    st.markdown("""
    <div class="landing-card">
        <div style="font-size: 5rem; margin-bottom: 2rem; animation: iconBounce 3s ease-in-out infinite;">🎯</div>
        <h2 style="color: #ffffff; margin-bottom: 1.5rem; font-size: 2.5rem; font-weight: 700;">
            Ready to Architect Your Dream Career?
        </h2>
        <p class="content-text" style="font-size: 1.2rem; margin-bottom: 3rem; max-width: 600px; margin-left: auto; margin-right: auto;">
            Unlock your potential with AI-powered career insights, personalized skill gap analysis, 
            and a custom roadmap designed specifically for your success journey.
        </p>
        <div class="cta-button">
            👆 Complete the form above to begin your transformation
        </div>
    </div>
    """, unsafe_allow_html=True)