import streamlit as st

# Set page config
st.set_page_config(page_title="Understanding Diabetes Inputs", page_icon="📊", layout="centered")

st.title("📊 Understanding Diabetes Inputs")
st.write("""
This page explains each input parameter needed for diabetes prediction, along with methods to measure or calculate them.  
""")

st.markdown("## 🔍 **1. Pregnancies**")
st.write("""
- **Definition:** Number of times a person has been pregnant.
- **Why It Matters:** Higher pregnancies increase diabetes risk.
""")

st.markdown("## 🍬 **2. Glucose Level**")
st.write("""
- **Definition:** Blood sugar concentration (mg/dL).
- **Normal Range:** 70-99 mg/dL (Fasting).
- **How to Measure:** Use a **glucose meter** or lab test.
""")

st.markdown("## 💓 **3. Blood Pressure**")
st.write("""
- **Definition:** Pressure of circulating blood against artery walls.
- **Normal Range:** 90/60 - 120/80 mmHg.
- **How to Measure:** Use a **BP monitor**.
""")

st.markdown("## 🏋️ **4. BMI (Body Mass Index)**")
st.write("""
- **Formula:** `BMI = Weight (kg) / Height² (m²)`.
- **Healthy Range:** 18.5 - 24.9.
- **Why It Matters:** Higher BMI means increased diabetes risk.
""")

st.markdown("## 💉 **5. Insulin Level**")
st.write("""
- **Definition:** Amount of insulin in the blood (µU/mL).
- **Normal Range:** 2-25 µU/mL.
- **How to Measure:** Blood test.
""")

st.markdown("## 🧬 **6. Diabetes Pedigree Function**")
st.write("""
- **Definition:** Probability of diabetes based on family history.
- **Scale:** 0 (Low) - 2.5 (High).
""")

st.markdown("## 🎂 **7. Age**")
st.write("""
- **Diabetes risk increases after age 35.**
- **Younger individuals with high BMI and glucose are also at risk.**
""")

st.markdown("## 🏥 **When to Visit a Doctor?**")
st.write("""
- **🚨 If your Glucose is consistently over 140 mg/dL.**
- **🚨 If your BMI is above 30 (Obese category).**
- **🚨 If your Diabetes Prediction result is High Risk.**
- **🔍 Regular checkups can help in early detection and management.**
""")

st.markdown("### 🔙 [Go Back to Prediction](app.py)")
