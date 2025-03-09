import streamlit as st

# Set page configuration
st.set_page_config(page_title="Diabetes Input Guide", page_icon="📘", layout="centered")

# Apply modern UI with neon-glass effect
st.markdown("""
    <style>
    body {
        background-color: #0d0d0d;
        color: #e0e0e0;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #141414;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 0px 20px rgba(139, 0, 0, 0.5);
    }
    .info-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        text-align: left;
    }
    .stTitle {
        color: #FF4500;
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(255, 69, 0, 0.8);
    }
    .stMarkdown {
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="stTitle">Understanding Input Values</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="info-container">
    <h3>Pregnancies</h3>
    <p>Number of times a woman has been pregnant. For males, keep it at 0.</p>
    
    <h3>Glucose Level</h3>
    <p>Blood sugar concentration measured in mg/dL. Normal range: 70-140.</p>
    
    <h3>Blood Pressure</h3>
    <p>Systolic blood pressure (mm Hg). Normal: 80-120.</p>
    
    <h3>Skin Thickness</h3>
    <p>Triceps skin fold thickness (mm), indicating body fat percentage.</p>
    
    <h3>Insulin Level</h3>
    <p>Insulin in blood (µU/mL). Normal range: 15-276.</p>
    
    <h3>BMI</h3>
    <p>Body Mass Index (kg/m²). Normal: 18.5-24.9.</p>
    
    <h3>Diabetes Pedigree Function</h3>
    <p>A score indicating genetic diabetes risk (0.0-2.5).</p>
    
    <h3>Age</h3>
    <p>Age in years. Higher age increases diabetes risk.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <br>
    <h2 style="color:#FF4500; text-align:center;">⚠️ If glucose, insulin, or BMI is high, consult a doctor.</h2>
""", unsafe_allow_html=True)
