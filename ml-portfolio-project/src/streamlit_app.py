import streamlit as st
import pandas as pd
from ml_pipeline.data_loader import load_data
from ml_pipeline.preprocessing import preprocess_data
from ml_pipeline.features import create_features
from ml_pipeline.train import train_model
from ml_pipeline.predict import make_prediction

def main():
    st.title("Machine Learning Portfolio Project")
    
    st.sidebar.header("Data Loading")
    data_option = st.sidebar.selectbox("Select Data Type", ("Raw Data", "Processed Data"))
    
    if data_option == "Raw Data":
        data = load_data("raw")
    else:
        data = load_data("processed")
    
    st.write("Data Loaded:")
    st.dataframe(data)

    st.sidebar.header("Preprocessing")
    if st.sidebar.button("Preprocess Data"):
        processed_data = preprocess_data(data)
        st.write("Data Preprocessed:")
        st.dataframe(processed_data)

    st.sidebar.header("Feature Engineering")
    if st.sidebar.button("Create Features"):
        features = create_features(processed_data)
        st.write("Features Created:")
        st.dataframe(features)

    st.sidebar.header("Model Training")
    if st.sidebar.button("Train Model"):
        model = train_model(features)
        st.write("Model Trained Successfully!")

    st.sidebar.header("Make Predictions")
    input_data = st.sidebar.text_input("Enter input data for prediction:")
    if st.sidebar.button("Predict"):
        prediction = make_prediction(model, input_data)
        st.write("Prediction Result:")
        st.write(prediction)

if __name__ == "__main__":
    main()