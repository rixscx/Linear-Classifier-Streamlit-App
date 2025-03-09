import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="Diabetes Input Guide", page_icon="📘", layout="centered")

# Apply modern UI with sleek glass effect
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 0px 20px rgba(255, 69, 0, 0.5);
    }
    .info-container {
        background: rgba(255, 255, 255, 0.08);
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0px 0px 12px rgba(255, 69, 0, 0.5);
        backdrop-filter: blur(8px);
        text-align: left;
        margin-bottom: 18px;
    }
    .stTitle {
        color: #FF6347;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        text-shadow: 2px 2px 12px rgba(255, 99, 71, 0.8);
    }
    .stMarkdown {
        font-size: 17px;
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

# Information sections with local images and detailed descriptions
info_data = [
    ("Pregnancies", 
     "This represents the number of times a woman has been pregnant. Pregnancy is linked with temporary changes in glucose levels due to hormonal shifts. "
     "Women with multiple pregnancies may have a higher risk of developing gestational diabetes, which can increase the likelihood of type 2 diabetes later in life. "
     "For males, this value should be kept at 0.", 
     "pregnancies.png"),
    
    ("Glucose Level", 
     "Glucose is the main sugar found in blood and is the body’s primary energy source. The measurement here represents fasting blood glucose levels in mg/dL. "
     "A normal range is typically between 70-140 mg/dL. Higher levels may indicate insulin resistance or diabetes, while lower levels could point to hypoglycemia.", 
     "glucose.png"),
    
    ("Blood Pressure", 
     "Blood pressure measures the force of blood pushing against artery walls. The value recorded is systolic pressure (mm Hg), the higher number in a BP reading. "
     "A normal range is 80-120 mm Hg. Chronic high blood pressure (hypertension) is a risk factor for diabetes-related complications such as kidney damage and heart disease.", 
     "blood_pressure.png"),
    
    ("Skin Thickness", 
     "This measures the thickness of the skinfold at the triceps in millimeters (mm). It is an indicator of subcutaneous fat and is often used to estimate body fat percentage. "
     "Higher values suggest increased fat accumulation, which is associated with obesity and a higher risk of insulin resistance and type 2 diabetes.", 
     "skin_thickness.jpg"),
    
    ("Insulin Level", 
     "Insulin is a hormone produced by the pancreas that regulates blood sugar levels. The value here represents insulin levels in the blood, measured in µU/mL. "
     "A normal fasting insulin level ranges from 15-276 µU/mL. Low levels indicate type 1 diabetes or pancreatic dysfunction, while elevated levels suggest insulin resistance, "
     "a hallmark of type 2 diabetes.", 
     "insulin.png"),
    
    ("BMI (Body Mass Index)", 
     "BMI is a measure of body fat based on height and weight. It is calculated as weight (kg) divided by height (m²). "
     "A normal BMI ranges between 18.5-24.9. A BMI above 25 is considered overweight, and over 30 is classified as obese, both of which significantly increase the risk of diabetes. "
     "Maintaining a healthy BMI can lower the risk of insulin resistance and metabolic disorders.", 
     "bmi.png"),
    
    ("Diabetes Pedigree Function", 
     "This is a calculated value that estimates the genetic predisposition to diabetes. It is a score ranging from 0.0 to 2.5, with higher values indicating greater genetic risk. "
     "It considers family history and other hereditary factors influencing diabetes development. A higher score suggests a stronger likelihood of diabetes in individuals with a family history.", 
     "pedigree.png"),
    
    ("Age", 
     "Age is a significant factor in diabetes risk. As people get older, the risk of developing diabetes increases due to factors such as reduced insulin sensitivity and increased body fat. "
     "While diabetes can occur at any age, individuals over 45 are at higher risk. A healthy lifestyle can help delay or prevent age-related diabetes onset.", 
     "age.jpg")
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
        st.image(image_path, use_container_width=False, width=300, caption=f"{title} Representation")
    else:
        st.warning(f"⚠️ Image not found: {image_path}")

# Final health warning
st.markdown("""
    <br>
    <h2 style="color:#FF4500; text-align:center;">⚠️ If glucose, insulin, or BMI is high, consult a doctor.</h2>
""", unsafe_allow_html=True)
