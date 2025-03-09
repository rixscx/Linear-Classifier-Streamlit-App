import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("diabetes_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Set page configuration
st.set_page_config(page_title="Diabetes Prediction", page_icon="⚕️", layout="centered")

# Apply dark crimson red theme with seamless hover effects
st.markdown("""
    <style>
    /* Background and Text */
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
    /* Title Styling */
    .stTitle {
        color: #8B0000;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(139, 0, 0, 0.8);
        transition: 0.3s ease-in-out;
    }
    .stTitle:hover {
        text-shadow: 2px 2px 15px rgba(255, 0, 0, 0.9);
    }
    /* Buttons */
    .stButton>button {
        background-color: #8B0000;
        color: black;
        font-size: 18px;
        padding: 12px;
        border-radius: 5px;
        transition: all 0.3s ease-in-out;
        font-weight: bold;
        width: 100%;
        border: none;
        box-shadow: 0px 0px 10px rgba(139, 0, 0, 0.6);
    }
    .stButton>button:hover {
        background-color: #660000;
        color: white;
        transform: scale(1.05);
        box-shadow: 0px 0px 20px rgba(255, 0, 0, 0.8);
    }
    /* Input Fields */
    input[type="number"] {
        background-color: #222;
        color: #8B0000;
        border-radius: 5px;
        border: 1px solid #8B0000;
        padding: 8px;
        transition: 0.3s ease-in-out;
    }
    input[type="number"]:hover, input[type="number"]:focus {
        border: 1px solid #ff0000;
        box-shadow: 0px 0px 10px rgba(255, 0, 0, 0.7);
        transform: scale(1.02);
    }
    /* Fork Button - Proper Alignment and Styling */
    .github-btn {
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: #111;
        padding: 10px 15px;
        border-radius: 8px;
        box-shadow: 0px 0px 10px rgba(139, 0, 0, 0.6);
        transition: 0.3s ease-in-out;
    }
    .github-btn:hover {
        transform: scale(1.1);
        box-shadow: 0px 0px 15px rgba(255, 0, 0, 0.9);
    }
    .github-btn a {
        color: #8B0000;
        font-size: 16px;
        font-weight: bold;
        text-decoration: none;
    }
    .github-btn a:hover {
        color: #ff0000;
    }
    </style>
""", unsafe_allow_html=True)

# GitHub Fork Button (Enhanced)
st.markdown("""
<div class="github-btn">
    <a href="https://github.com/rixscx/Linear-Classifier-Streamlit-App/fork" target="_blank">
        🚀 Fork this Project
    </a>
</div>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="stTitle">Diabetes Prediction AI</h1>', unsafe_allow_html=True)

st.markdown('<p class="stMarkdown">Fill in the details below to predict the likelihood of diabetes.</p>', unsafe_allow_html=True)

# Input layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=120, step=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140, value=70, step=1)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20, step=1)

with col2:
    insulin = st.number_input("Insulin Level", min_value=0, max_value=500, value=80, step=1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=25.0, step=0.1)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
    age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)

# Prediction Button
if st.button("🔍 Predict Diabetes"):
    # Prepare input data
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])

    # Predict
    prediction = model.predict(input_data)
    
    # Display result with emoji
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error("🚨 **High Risk:** The person **may have diabetes**.")
    else:
        st.success("✅ **Low Risk:** The person **is unlikely to have diabetes**.")
