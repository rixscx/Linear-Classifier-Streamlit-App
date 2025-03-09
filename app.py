import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("diabetes_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit App UI
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        color: #333333;
    }
    .stApp {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .github-btn {
        display: flex;
        justify-content: right;
        margin-bottom: -20px;
    }
    </style>
""", unsafe_allow_html=True)

# GitHub Fork Button
st.markdown("""
<div class="github-btn">
    <a href="https://github.com/rixscx/Linear-Classifier-Streamlit-App/fork" target="_blank">
        <img src="https://img.shields.io/github/forks/rixscx/Linear-Classifier-Streamlit-App?style=social" alt="Fork me on GitHub">
    </a>
</div>
""", unsafe_allow_html=True)

# Title with emoji
st.title("🔬 Diabetes Prediction App")

st.write("Enter the details below to check the **likelihood of diabetes**.")

# Create input fields using st.columns() for better layout
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
        st.error("🚨 High Risk: The person **may have diabetes**.")
    else:
        st.success("✅ Low Risk: The person **is unlikely to have diabetes**.")

# Footer
st.markdown("---")
st.markdown("💡 *This AI-powered tool helps in predicting diabetes based on medical attributes.*")
