# Climate Change Machine Learning Project

This project aims to analyze and predict climate change trends using machine learning techniques. The dataset used for this project is the Global Climate Change Data from 2020 to 2025.

## Project Structure

```
climate-change-ml-app
├── data
│   └── raw
│       └── Global_Climate_Change_Data_2020_2025.csv
├── notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
├── src
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── models.py
│   └── utils.py
├── app
│   ├── main.py
│   └── pages
│       ├── 01_Exploratory_Analysis.py
│       └── 02_Model_Prediction.py
├── tests
│   ├── __init__.py
│   ├── test_data_loader.py
│   └── test_models.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Make sure you have Python 3.7 or higher installed. You will also need to install the required packages listed in `requirements.txt`.

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd climate-change-ml-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the Streamlit application, navigate to the `app` directory and execute the following command:

```
streamlit run main.py
```

This will start the Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

### Notebooks

The project includes Jupyter notebooks for data exploration, feature engineering, and model training:

- **01_data_exploration.ipynb**: Explore the dataset and visualize data distributions.
- **02_feature_engineering.ipynb**: Create and transform features for modeling.
- **03_model_training.ipynb**: Train machine learning models and evaluate their performance.

### Testing

Unit tests are included in the `tests` directory. You can run the tests using:

```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Dataset: Global Climate Change Data (2020-2025)
- Libraries: Pandas, Scikit-learn, Streamlit, etc.