import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('HousingPredictor.joblib')

# Streamlit App
st.title("🏡 Housing Price Predictor")
st.write("Enter the details below to predict the house price:")

# Input fields for all 13 features
CRIM = st.number_input("Crime Rate (CRIM)", min_value=0.0, max_value=100.0, value=0.1)
ZN = st.number_input("Residential Land (ZN)", min_value=0.0, max_value=100.0, value=25.0)
INDUS = st.number_input("Non-Retail Business Acres (INDUS)", min_value=0.0, max_value=30.0, value=5.0)
CHAS = st.selectbox("Charles River (CHAS: 1 if next to river, 0 otherwise)", [0, 1])
NOX = st.number_input("Nitrogen Oxide Concentration (NOX)", min_value=0.0, max_value=1.0, value=0.5)
RM = st.number_input("Average Number of Rooms (RM)", min_value=1.0, max_value=10.0, value=6.0)
AGE = st.number_input("Proportion of Old Buildings (AGE)", min_value=0.0, max_value=100.0, value=50.0)
DIS = st.number_input("Distance to Employment Centers (DIS)", min_value=0.0, max_value=15.0, value=4.0)
RAD = st.number_input("Accessibility to Highways (RAD)", min_value=1, max_value=24, value=5)
TAX = st.number_input("Property Tax Rate (TAX)", min_value=0.0, max_value=1000.0, value=300.0)
PTRATIO = st.number_input("Pupil-Teacher Ratio (PTRATIO)", min_value=10.0, max_value=30.0, value=18.0)
B = st.number_input("Proportion of Black Population (B)", min_value=0.0, max_value=400.0, value=350.0)
LSTAT = st.number_input("Lower Status Population (LSTAT)", min_value=0.0, max_value=40.0, value=12.0)

# Predict button
if st.button("Predict Price"):
    features = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
    prediction = model.predict(features)[0]
    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")
