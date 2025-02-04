import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreak',
                   layout='wide',
                   page_icon='🩺')

# Load the model
model_path = "diabetes.pkl"

if not os.path.exists(model_path):
    st.error(f"Error: Model file '{model_path}' not found! Please train and save the model first.")
    st.stop()

with open(model_path, "rb") as file:
    diabetes_model = pickle.load(file)

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Diseases Outbreak System', ['Diabetes Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'person'], default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
    with col2:
        glucose = st.number_input('Glucose Level', min_value=0.0, step=0.1)
    with col3:
        blood_pressure = st.number_input('Blood Pressure Value', min_value=0.0, step=0.1)
    with col1:
        skin_thickness = st.number_input('Skin Thickness Value', min_value=0.0, step=0.1)
    with col2:
        insulin = st.number_input('Insulin Level', min_value=0.0, step=0.1)
    with col3:
        bmi = st.number_input('BMI Value', min_value=0.0, step=0.1)
    with col1:
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, step=0.01)
    with col2:
        age = st.number_input('Age of the Person', min_value=0, step=1)

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)
