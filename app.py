import streamlit as st
import numpy as np

# Optional: load your trained model
# import joblib
# model = joblib.load("inflation_model.pkl")

st.title("Worldwide Inflation Predictor")

country = st.text_input("Enter country", "Kenya")
year = st.slider("Select year", 2000, 2050, 2025)

# Replace this with actual feature engineering + model prediction
# features = prepare_features(country, year)
# prediction = model.predict([features])[0]
prediction = np.random.uniform(2.0, 12.0)  # Dummy value for testing

st.write(f"Predicted inflation for **{country}** in **{year}**: **{prediction:.2f}%**")
