from pathlib import Path
import pandas as pd
import streamlit as st
from src.data_loader import load_data
from src.models import load_model

# Load the model
model = load_model('path_to_your_trained_model.pkl')  # Update with the actual model path

# Load the data
data_path = Path("data/raw/Global_Climate_Change_Data_2020_2025.csv")
data = load_data(data_path)

# Streamlit app layout
st.title("Climate Change Prediction App")
st.write("This app predicts climate change metrics based on user input.")

# User input for prediction
st.sidebar.header("User Input Features")

def user_input_features():
    # Create input fields for the features used in the model
    # Example: replace 'feature1', 'feature2' with actual feature names
    feature1 = st.sidebar.number_input("Feature 1", min_value=0.0, max_value=100.0, value=50.0)
    feature2 = st.sidebar.number_input("Feature 2", min_value=0.0, max_value=100.0, value=50.0)
    # Add more features as needed
    data = {
        'feature1': feature1,
        'feature2': feature2,
        # Add more features here
    }
    return pd.DataFrame(data, index=[0])

input_data = user_input_features()

# Make prediction
if st.sidebar.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction)