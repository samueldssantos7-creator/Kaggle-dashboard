from pathlib import Path
import pandas as pd
import pytest
from src.models import train_model, predict, evaluate_model

# Sample data for testing
def create_sample_data():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

# Test for training the model
def test_train_model():
    df = create_sample_data()
    model = train_model(df[['feature1', 'feature2']], df['target'])
    assert model is not None

# Test for making predictions
def test_predict():
    df = create_sample_data()
    model = train_model(df[['feature1', 'feature2']], df['target'])
    predictions = predict(model, df[['feature1', 'feature2']])
    assert len(predictions) == len(df)

# Test for evaluating the model
def test_evaluate_model():
    df = create_sample_data()
    model = train_model(df[['feature1', 'feature2']], df['target'])
    score = evaluate_model(model, df[['feature1', 'feature2']], df['target'])
    assert score >= 0  # Assuming score is a non-negative value