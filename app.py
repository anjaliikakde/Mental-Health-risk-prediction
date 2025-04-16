import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('model.pkl')

# Title of the app
st.title("Mental Health Prediction App")

st.markdown("""
Welcome! Use this app to predict mental health outcomes based on various input features.
Simply fill in the details below, and click **Predict** to see the result.
""")

# Feature Inputs
st.header("Input Features")
age = st.number_input("Age", value=0.0)
gender_male = st.radio("Gender Male", [0, 1], index=0)
gender_other = st.radio("Gender Other", [0, 1], index=0)
family_history_Yes = st.radio("Family History", [0, 1], index=0)
work_interfere_Never = st.radio("Work Interfere Never", [0, 1], index=0)
work_interfere_Often = st.radio("Work Interfere Often", [0, 1], index=0)
work_interfere_Rarely = st.radio("Work Interfere Rarely", [0, 1], index=0)
work_interfere_Sometimes = st.radio("Work Interfere Sometimes", [0, 1], index=0)
no_employees_100_500 = st.radio("No Employees 100-500", [0, 1], index=0)
no_employees_26_100 = st.radio("No Employees 26-100", [0, 1], index=0)
no_employees_500_1000 = st.radio("No Employees 500-1000", [0, 1], index=0)
no_employees_6_25 = st.radio("No Employees 6-25", [0, 1], index=0)
no_employees_More_than_1000 = st.radio("No Employees More than 1000", [0, 1], index=0)
remote_work_Yes = st.radio("Remote Work", [0, 1], index=0)
tech_company_Yes = st.radio("Tech Company", [0, 1], index=0)
benefits_No = st.radio("Benefits No", [0, 1], index=0)
benefits_Yes = st.radio("Benefits Yes", [0, 1], index=0)
care_options_Not_sure = st.radio("Care Options Not Sure", [0, 1], index=0)
care_options_Yes = st.radio("Care Options Yes", [0, 1], index=0)
wellness_program_No = st.radio("Wellness Program No", [0, 1], index=0)
wellness_program_Yes = st.radio("Wellness Program Yes", [0, 1], index=0)
seek_help_No = st.radio("Seek Help No", [0, 1], index=0)
seek_help_Yes = st.radio("Seek Help Yes", [0, 1], index=0)
anonymity_No = st.radio("Anonymity No", [0, 1], index=0)
anonymity_Yes = st.radio("Anonymity Yes", [0, 1], index=0)
leave_Somewhat_difficult = st.radio("Leave Somewhat Difficult", [0, 1], index=0)
leave_Somewhat_easy = st.radio("Leave Somewhat Easy", [0, 1], index=0)
leave_Very_difficult = st.radio("Leave Very Difficult", [0, 1], index=0)
leave_Very_easy = st.radio("Leave Very Easy", [0, 1], index=0)
mental_health_consequence_No = st.radio("Mental Health Consequence No", [0, 1], index=0)
mental_health_consequence_Yes = st.radio("Mental Health Consequence Yes", [0, 1], index=0)
phys_health_consequence_No = st.radio("Physical Health Consequence No", [0, 1], index=0)
phys_health_consequence_Yes = st.radio("Physical Health Consequence Yes", [0, 1], index=0)
coworkers_Some_of_them = st.radio("Coworkers Some of Them", [0, 1], index=0)
coworkers_Yes = st.radio("Coworkers Yes", [0, 1], index=0)
supervisor_Some_of_them = st.radio("Supervisor Some of Them", [0, 1], index=0)
supervisor_Yes = st.radio("Supervisor Yes", [0, 1], index=0)
mental_vs_physical_No = st.radio("Mental vs Physical No", [0, 1], index=0)
mental_vs_physical_Yes = st.radio("Mental vs Physical Yes", [0, 1], index=0)

# Combine inputs into a DataFrame
input_features = pd.DataFrame({
    'age': [age],
    'gender_male': [gender_male],
    'gender_other': [gender_other],
    'family_history_Yes': [family_history_Yes],
    'work_interfere_Never': [work_interfere_Never],
    'work_interfere_Often': [work_interfere_Often],
    'work_interfere_Rarely': [work_interfere_Rarely],
    'work_interfere_Sometimes': [work_interfere_Sometimes],
    'no_employees_100-500': [no_employees_100_500],
    'no_employees_26-100': [no_employees_26_100],
    'no_employees_500-1000': [no_employees_500_1000],
    'no_employees_6-25': [no_employees_6_25],
    'no_employees_More than 1000': [no_employees_More_than_1000],
    'remote_work_Yes': [remote_work_Yes],
    'tech_company_Yes': [tech_company_Yes],
    'benefits_No': [benefits_No],
    'benefits_Yes': [benefits_Yes],
    'care_options_Not sure': [care_options_Not_sure],
    'care_options_Yes': [care_options_Yes],
    'wellness_program_No': [wellness_program_No],
    'wellness_program_Yes': [wellness_program_Yes],
    'seek_help_No': [seek_help_No],
    'seek_help_Yes': [seek_help_Yes],
    'anonymity_No': [anonymity_No],
    'anonymity_Yes': [anonymity_Yes],
    'leave_Somewhat difficult': [leave_Somewhat_difficult],
    'leave_Somewhat easy': [leave_Somewhat_easy],
    'leave_Very difficult': [leave_Very_difficult],
    'leave_Very easy': [leave_Very_easy],
    'mental_health_consequence_No': [mental_health_consequence_No],
    'mental_health_consequence_Yes': [mental_health_consequence_Yes],
    'phys_health_consequence_No': [phys_health_consequence_No],
    'phys_health_consequence_Yes': [phys_health_consequence_Yes],
    'coworkers_Some of them': [coworkers_Some_of_them],
    'coworkers_Yes': [coworkers_Yes],
    'supervisor_Some of them': [supervisor_Some_of_them],
    'supervisor_Yes': [supervisor_Yes],
    'mental_vs_physical_No': [mental_vs_physical_No],
    'mental_vs_physical_Yes': [mental_vs_physical_Yes],
}, columns=model.feature_names_in_)

    
# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_features)  # Ensure `prediction` is defined here
    if prediction[0] == 0:
        st.info("The prediction suggests no immediate need for a mental health checkup. However, maintaining mental wellness is important. If you're feeling stressed or uncertain, consider consulting a professional.")
    else:
        st.warning("The prediction suggests you might benefit from a mental health checkup. Please consider reaching out to a healthcare professional for guidance.")
