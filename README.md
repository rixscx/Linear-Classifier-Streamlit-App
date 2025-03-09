# 🎯 Diabetes Prediction App using Logistic Regression

Welcome to the **Diabetes Prediction App**, a machine learning-powered web application designed to predict the likelihood of diabetes based on patient data. This project leverages a **Logistic Regression model** trained on the **Pima Indians Diabetes Dataset**, achieving an accuracy of approximately **76%**. The app is built with **Streamlit** and provides an interactive interface for predictions. 🚀

---

## 📋 Project Overview

This application uses the **Pima Indians Diabetes Database** to classify whether a person is diabetic based on input features such as **Glucose Level, BMI, Blood Pressure, and Age**. Users can enter relevant health parameters and receive a **prediction with probability scores**.

### 🔍 Key Highlights

- **Dataset**: Pima Indians Diabetes Database (Kaggle)
- **Model**: Logistic Regression (~76% accuracy)
- **Deployment**: Streamlit Cloud
- **Interactivity**: Accepts user input to generate real-time predictions

---

## 🚀 Features

✅ **Predicts diabetes status** (Diabetic or Not Diabetic) based on user input  
📊 **Displays probability scores** for each class  
📈 **Dataset visualization** (Glucose vs BMI scatter plot) *(optional)*  
🎨 **User-friendly UI** with modern animations and styling  
🌐 **Fully deployed and accessible online**  

---

## 📂 Folder Structure

```
Linear-Classifier-Streamlit-App/
├── app.py                      # Main Streamlit application
├── diabetes_model.pkl          # Trained Logistic Regression model
├── diabetes.csv                # Dataset (if included for visualization)
├── linear-classifier-streamlit.ipynb  # Jupyter Notebook for model training
├── requirements.txt            # Dependencies
├── README.md                   # Documentation file
├── images/                     # Image assets for UI
```

---

## 🛠️ Setup Instructions

### **Prerequisites**

- 🐍 **Python 3.12 or higher**
- 📦 **Git** (for cloning the repository)

### **Installation**

1️⃣ Clone the repository:

```bash
git clone https://github.com/rixscx/Linear-Classifier-Streamlit-App.git
cd Linear-Classifier-Streamlit-App
```

2️⃣ Create a virtual environment:

```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

4️⃣ Run the app locally:

```bash
streamlit run app.py
```

5️⃣ Open **[http://localhost:8501](http://localhost:8501)** in your browser.

---

## 🎮 Usage

1️⃣ **Enter values** for patient health metrics (Pregnancies, Glucose, BMI, Age, etc.).  
2️⃣ Click the **"🔍 Predict Diabetes"** button.  
3️⃣ View **prediction results and probability scores**.  
4️⃣ *(Optional)* Enable dataset visualization for additional insights.  

**Example Output:**

```
Prediction: "Diabetic" or "Not Diabetic"
Probability Scores:
 - Not Diabetic: 65%
 - Diabetic: 35%
```

---

## 🌐 Deployment

The app is **deployed on Streamlit Community Cloud** and updates automatically with changes from the main branch.

🔗 **Live App:** [Visit Here](https://github.com/rixscx/Linear-Classifier-Streamlit-App/tree/main)

To redeploy:

- Push updates to the **main branch**, and Streamlit Cloud will handle auto-deployment.

---

## 🤝 Contributing

We welcome contributions! If you have ideas to improve accuracy (e.g., using **Random Forest**) or enhancing the UI, feel free to submit a pull request.

### **Contribution Steps**

1️⃣ Fork the repository  
2️⃣ Create a new branch:

```bash
git checkout -b feature-branch
```

3️⃣ Commit your changes:

```bash
git commit -m "Add new feature"
```

4️⃣ Push to the branch:

```bash
git push origin feature-branch
```

5️⃣ Open a **Pull Request** 🎉  

---

## ⚠️ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details. 📜

---

## 🙏 Acknowledgments

🌟 **Dataset** sourced from **UCI Machine Learning Repository via Kaggle**  
🎉 **Streamlit Community** for the free deployment platform  
💻 **Guidance by Dr. Agughasi Victor Ikechukwu**  

---

## 📬 Contact

👤 **Author**: Manish P  
📧 **Email**: [manishp.73codestop@gmail.com](mailto:manishp.73codestop@gmail.com)  
🌐 **GitHub**: [@rixscx](https://github.com/rixscx)  

---

🚀 **Thank you for checking out this project! Happy coding!**

