from pathlib import Path
import pandas as pd
import streamlit as st
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.models import train_model, predict

# Set the title of the Streamlit app
st.title("Climate Change Machine Learning App")

# Load the dataset
DATA_PATH = Path("data/raw/Global_Climate_Change_Data_2020_2025.csv")
df = load_data(DATA_PATH)

# Display the dataset
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(df)

# Preprocess the data
df_processed = preprocess_data(df)

# Exploratory Analysis
st.subheader("Exploratory Data Analysis")
if st.checkbox("Show processed data"):
    st.write(df_processed)

# Model Training
if st.button("Train Model"):
    model = train_model(df_processed)
    st.success("Model trained successfully!")

# Prediction
st.subheader("Make Predictions")
input_data = st.text_input("Enter input data for prediction:")
if st.button("Predict"):
    prediction = predict(model, input_data)
    st.write(f"Prediction: {prediction}")