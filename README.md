# [Mental Health Prediction in Tech Employees Using Logistic Regression]()

This project aims to predict whether a tech employee is likely to suffer from mental health issues based on their responses to a survey. We use **Logistic Regression**, a simple yet powerful classification algorithm, to build our prediction model.

---

## Table of Contents

- [Overview](#overview)
- [Logistic Regression](#what-is-logistic-regression)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Steps Involved](#steps-involved)
- [How to Run](#how-to-run)
- [Results](#results)
- [Conclusion](#conclusion)

## Overview

Mental health is a serious concern in the tech industry. In this project, we analyze survey data and build a model that can help in predicting whether an employee is likely to face mental health issues at work.


## Logistic Regression

**Logistic Regression** is a statistical method used for binary classification problems — where the output is either **Yes or No**, **True or False**, **1 or 0**.

Unlike Linear Regression (which predicts continuous values), Logistic Regression predicts the **probability** that a given input belongs to a particular category. It uses a special function called the **sigmoid function** to map predicted values between 0 and 1.

In this project, Logistic Regression helps us classify if a person is **likely** or **not likely** to experience mental health issues based on features like age, gender, workplace support, etc.

## Dataset

- The dataset used in this project is taken from a mental health survey conducted among tech employees.
- Features include: age, gender, family history of mental illness, work interference, benefits at workplace, etc.
- Target variable: **Is the person likely to have mental health issues?** (Yes/No)

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn (Logistic Regression, Model Evaluation)
- Matplotlib / Seaborn (for visualizations)


## Steps Involved

1. **Data Cleaning** – Handling missing values and fixing inconsistent entries.
2. **Exploratory Data Analysis (EDA)** – Understanding patterns and relationships.
3. **Feature Encoding** – Converting categorical data to numeric form.
4. **Model Training** – Using Logistic Regression for binary classification.
5. **Model Evaluation** – Accuracy, Precision, Recall, Confusion Matrix, ROC Curve.


## How to Run

1. Clone this repository  
   `git clone https://github.com/anjaliikakde/mental-health-prediction.git`
2. Install required libraries  
   `pip install -r requirements.txt`

3. Run the notebook.
4. Run the streamlite app
   `streamlit run app.py`


## Results

- The Logistic Regression model gave an accuracy of around **84%** (replace with your result).
- Important features influencing predictions included **family history**, **workplace support**, and **previous diagnosis**.

## Conclusion

This project highlights the importance of mental health awareness in the tech industry and demonstrates how basic machine learning techniques can be used to support early prediction and prevention efforts.
