from pathlib import Path
import pandas as pd
import streamlit as st

# Define the path to the CSV file
CSV_PATH = Path("data/raw/Global_Climate_Change_Data_2020_2025.csv")

def load_data():
    """Load the climate change data from the CSV file."""
    if not CSV_PATH.exists():
        st.error(f"File not found: {CSV_PATH}")
        return None
    df = pd.read_csv(CSV_PATH)
    return df

def display_data_overview(df):
    """Display an overview of the dataset."""
    st.header("Dataset Overview")
    st.write("Dimensions:", df.shape)
    st.write("Columns:", list(df.columns))
    st.write("Data Types:", df.dtypes)
    st.write("Missing Values:", df.isna().sum())
    st.write("Sample Data:")
    st.dataframe(df.head())

def main():
    """Main function to run the Streamlit app."""
    st.title("Exploratory Data Analysis of Climate Change Data")
    
    df = load_data()
    if df is not None:
        display_data_overview(df)

if __name__ == "__main__":
    main()