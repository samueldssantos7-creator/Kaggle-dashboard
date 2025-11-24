# Machine Learning Portfolio Project

This project is a comprehensive machine learning portfolio that demonstrates the entire workflow from data loading to model training and evaluation. It includes a Streamlit application for interactive data visualization and model predictions.

## Project Structure

- **data/**
  - **raw/**: Contains the raw data files used for the machine learning project.
  - **processed/**: Holds the processed data files that are ready for modeling.

- **notebooks/**
  - **01-data-exploration.ipynb**: A Jupyter notebook for exploring the dataset, visualizing data distributions, and understanding relationships between features.
  - **02-modeling.ipynb**: A Jupyter notebook for building and evaluating machine learning models using the processed data.

- **src/**
  - **streamlit_app.py**: The main entry point for the Streamlit application. It loads the data, displays visualizations, and allows users to interact with the machine learning model.
  - **ml_pipeline/**: Contains the machine learning pipeline modules.
    - **data_loader.py**: Functions for loading data from the raw and processed directories.
    - **preprocessing.py**: Functions for preprocessing the data, such as handling missing values and scaling features.
    - **features.py**: Functions for feature engineering.
    - **train.py**: Functions for training the machine learning model.
    - **model.py**: Defines the model architecture and includes functions for saving and loading the model.
    - **predict.py**: Functions for making predictions with the trained model.
  - **utils/**: Contains utility functions.
    - **metrics.py**: Functions for evaluating model performance.
    - **visualization.py**: Functions for visualizing data and model results.

- **models/**: Directory to store trained models.

- **tests/**: Contains unit tests for the project.
  - **test_data_loader.py**: Unit tests for the data loading functions.
  - **test_model.py**: Unit tests for the model training and prediction functions.

- **requirements.txt**: Lists the dependencies required for the project.

- **pyproject.toml**: Used for project configuration and dependency management.

- **.gitignore**: Specifies files and directories that should be ignored by version control.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ml-portfolio-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run src/streamlit_app.py
   ```

## Overview

This project aims to provide a clear and structured approach to building machine learning models, from data exploration to deployment. The use of Streamlit allows for an interactive experience, making it easier to visualize data and understand model predictions.