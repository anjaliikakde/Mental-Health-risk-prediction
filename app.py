import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('model.pkl')

# App title and intro
st.set_page_config(page_title="Mental Health Predictor", layout="centered")
st.title("Mental Health Prediction App")

st.markdown("""
Welcome! This app predicts the likelihood of requiring a mental health checkup based on your responses.

Fill out the form below and click **Predict** to see the result.
""")

st.markdown("---")
st.header("📋 Personal & Workplace Details")

# Organize inputs with columns for better UX
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10.0, max_value=100.0, value=25.0, step=1.0)
    gender = st.radio("Gender", ["Male", "Other", "Female"], index=0)
    family_history = st.radio("Any family history of mental illness?", ["No", "Yes"], index=0)
    remote_work = st.radio("Do you work remotely?", ["No", "Yes"], index=0)
    tech_company = st.radio("Do you work in a tech company?", ["No", "Yes"], index=0)
    no_employees = st.selectbox("Company size", [
        "1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"
    ])

with col2:
    work_interfere = st.selectbox("Does mental health interfere with work?", [
        "Never", "Rarely", "Sometimes", "Often"
    ])
    benefits = st.radio("Are mental health benefits provided?", ["No", "Yes"], index=0)
    care_options = st.radio("Are care options available at work?", ["No", "Yes", "Not sure"], index=0)
    wellness_program = st.radio("Is there a wellness program?", ["No", "Yes"], index=0)
    seek_help = st.radio("Does your company encourage seeking help?", ["No", "Yes"], index=0)
    anonymity = st.radio("Is anonymity protected when seeking help?", ["No", "Yes"], index=0)

st.markdown("---")
st.header("👥 Work Environment")

col3, col4 = st.columns(2)

with col3:
    leave = st.selectbox("How easy is it to take mental health leave?", [
        "Very difficult", "Somewhat difficult", "Somewhat easy", "Very easy"
    ])
    mh_consequence = st.radio("Are there negative consequences of talking about mental health?", ["No", "Yes"], index=0)
    ph_consequence = st.radio("Are there consequences for physical health issues?", ["No", "Yes"], index=0)

with col4:
    coworkers = st.radio("Can you talk to your coworkers?", ["No", "Some of them", "Yes"], index=1)
    supervisor = st.radio("Can you talk to your supervisor?", ["No", "Some of them", "Yes"], index=1)
    mental_vs_physical = st.radio("Is mental health treated equally to physical health?", ["No", "Yes"], index=1)

# One-hot encode the inputs to match the model
def encode_inputs():
    data = {
        'age': age,
        'gender_male': 1 if gender == "Male" else 0,
        'gender_other': 1 if gender == "Other" else 0,
        'family_history_Yes': 1 if family_history == "Yes" else 0,
        'work_interfere_Never': int(work_interfere == "Never"),
        'work_interfere_Often': int(work_interfere == "Often"),
        'work_interfere_Rarely': int(work_interfere == "Rarely"),
        'work_interfere_Sometimes': int(work_interfere == "Sometimes"),
        'no_employees_100-500': int(no_employees == "100-500"),
        'no_employees_26-100': int(no_employees == "26-100"),
        'no_employees_500-1000': int(no_employees == "500-1000"),
        'no_employees_6-25': int(no_employees == "6-25"),
        'no_employees_More than 1000': int(no_employees == "More than 1000"),
        'remote_work_Yes': 1 if remote_work == "Yes" else 0,
        'tech_company_Yes': 1 if tech_company == "Yes" else 0,
        'benefits_No': 1 if benefits == "No" else 0,
        'benefits_Yes': 1 if benefits == "Yes" else 0,
        'care_options_Not sure': int(care_options == "Not sure"),
        'care_options_Yes': int(care_options == "Yes"),
        'wellness_program_No': 1 if wellness_program == "No" else 0,
        'wellness_program_Yes': 1 if wellness_program == "Yes" else 0,
        'seek_help_No': 1 if seek_help == "No" else 0,
        'seek_help_Yes': 1 if seek_help == "Yes" else 0,
        'anonymity_No': 1 if anonymity == "No" else 0,
        'anonymity_Yes': 1 if anonymity == "Yes" else 0,
        'leave_Somewhat difficult': int(leave == "Somewhat difficult"),
        'leave_Somewhat easy': int(leave == "Somewhat easy"),
        'leave_Very difficult': int(leave == "Very difficult"),
        'leave_Very easy': int(leave == "Very easy"),
        'mental_health_consequence_No': 1 if mh_consequence == "No" else 0,
        'mental_health_consequence_Yes': 1 if mh_consequence == "Yes" else 0,
        'phys_health_consequence_No': 1 if ph_consequence == "No" else 0,
        'phys_health_consequence_Yes': 1 if ph_consequence == "Yes" else 0,
        'coworkers_Some of them': int(coworkers == "Some of them"),
        'coworkers_Yes': int(coworkers == "Yes"),
        'supervisor_Some of them': int(supervisor == "Some of them"),
        'supervisor_Yes': int(supervisor == "Yes"),
        'mental_vs_physical_No': 1 if mental_vs_physical == "No" else 0,
        'mental_vs_physical_Yes': 1 if mental_vs_physical == "Yes" else 0,
    }
    return pd.DataFrame([data], columns=model.feature_names_in_)

# Prediction
st.markdown("---")
if st.button("🚀 Predict"):
    input_df = encode_inputs()
    prediction = model.predict(input_df)[0]
    if prediction == 0:
        st.success("✅ No immediate mental health support predicted.\n\nKeep taking care of your mental well-being!")
    else:
        st.error("⚠️ You may benefit from professional mental health support.\n\nPlease consider reaching out to a therapist or counselor.")

