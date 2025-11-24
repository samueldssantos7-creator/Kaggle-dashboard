import pytest
from src.ml_pipeline.data_loader import load_data
import os

def test_load_data_raw():
    raw_data_path = os.path.join('data', 'raw')
    data = load_data(raw_data_path)
    assert data is not None
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_load_data_processed():
    processed_data_path = os.path.join('data', 'processed')
    data = load_data(processed_data_path)
    assert data is not None
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_load_data_invalid_path():
    invalid_path = 'invalid/path'
    with pytest.raises(FileNotFoundError):
        load_data(invalid_path)