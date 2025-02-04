# Diabetes Prediction System

## Overview
This project is a **Diabetes Prediction System** built using **Streamlit** and **Machine Learning**. It loads a trained model from a **pickle (.pkl) file** and provides an interactive interface to predict whether a person is diabetic based on input parameters.

## Features
- User-friendly interface using **Streamlit**
- Predicts diabetes based on user input
- Uses a pre-trained machine learning model saved as a **pickle file**

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip (Python package manager)

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not available, manually install dependencies:
   ```bash
   pip install streamlit streamlit-option-menu pickle5
   ```

4. **Ensure the trained model file (`diabetes.pkl`) is available**
   - Place the `diabetes.pkl` file in the same directory as the script.
   - If the file is missing, train and save a new model before running the application.

## Running the Application
Start the Streamlit app using:
```bash
streamlit run app.py
```
This will open a web interface where you can input details and get a diabetes prediction.

## Usage
- Enter values for the required parameters (Pregnancies, Glucose, Blood Pressure, etc.).
- Click the **Diabetes Test Result** button.
- The app will predict whether the person is diabetic or not.

## Troubleshooting
- If the application fails to start, ensure that all dependencies are installed correctly.
- If the `diabetes.pkl` model file is missing, train and save a new model.
- Check for any error messages in the terminal for further debugging.

## License
This project is licensed under the MIT License.

---

