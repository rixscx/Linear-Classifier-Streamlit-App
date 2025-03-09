import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model
with open("diabetes_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("🔬 Diabetes Prediction App")

st.sidebar.header("Enter Patient Data")
pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, 1)
glucose = st.sidebar.number_input("Glucose", 0, 200, 110)
blood_pressure = st.sidebar.number_input("Blood Pressure", 0, 140, 70)
skin_thickness = st.sidebar.number_input("Skin Thickness", 0, 100, 20)
insulin = st.sidebar.number_input("Insulin", 0, 900, 79)
bmi = st.sidebar.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.sidebar.number_input("Age", 18, 100, 30)

# Create input dataframe
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
input_df = pd.DataFrame(input_data, columns=['Pregnancies', 'Glucose', 'BloodPressure', 
                                             'SkinThickness', 'Insulin', 'BMI', 
                                             'DiabetesPedigreeFunction', 'Age'])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)
    result = "🟢 No Diabetes" if prediction[0] == 0 else "🔴 Diabetes Detected"
    st.write(f"## Prediction: {result}")
 
