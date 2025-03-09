import streamlit as st
import os

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
        margin-bottom: 20px;
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
    .image-caption {
        text-align: center;
        font-size: 14px;
        color: #b0b0b0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="stTitle">Understanding Input Values</h1>', unsafe_allow_html=True)

# Define the local path for images
IMAGE_DIR = "Images"

# Information sections with local images
info_data = [
    ("Pregnancies", "Number of times a woman has been pregnant. For males, keep it at 0.", "pregnancies.png"),
    ("Glucose Level", "Blood sugar concentration measured in mg/dL. Normal range: 70-140.", "glucose.png"),
    ("Blood Pressure", "Systolic blood pressure (mm Hg). Normal: 80-120.", "blood_pressure.png"),
    ("Skin Thickness", "Triceps skin fold thickness (mm), indicating body fat percentage.", "skin_thickness.png"),
    ("Insulin Level", "Insulin in blood (µU/mL). Normal range: 15-276.", "insulin.png"),
    ("BMI", "Body Mass Index (kg/m²). Normal: 18.5-24.9.", "bmi.png"),
    ("Diabetes Pedigree Function", "A score indicating genetic diabetes risk (0.0-2.5).", "pedigree.png"),
    ("Age", "Age in years. Higher age increases diabetes risk.", "age.png")
]

# Display sections dynamically
for title, description, image_name in info_data:
    image_path = os.path.join(IMAGE_DIR, image_name)

    st.markdown(f"""
    <div class="info-container">
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if the image exists before displaying it
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True, caption=f"{title} Representation")
    else:
        st.warning(f"⚠️ Image not found: {image_path}")

# Final health warning
st.markdown("""
    <br>
    <h2 style="color:#FF4500; text-align:center;">⚠️ If glucose, insulin, or BMI is high, consult a doctor.</h2>
""", unsafe_allow_html=True)
