from pathlib import Path
import pandas as pd
import pytest
from src.data_loader import load_and_inspect

CSV_PATH = Path("data/raw/Global_Climate_Change_Data_2020_2025.csv")

def test_load_and_inspect():
    # Test if the data is loaded correctly
    df = load_and_inspect(CSV_PATH, nrows=5)
    
    # Check if the DataFrame is not empty
    assert not df.empty, "DataFrame is empty"
    
    # Check if the shape of the DataFrame is as expected
    expected_shape = (5, len(df.columns))  # Assuming we expect 5 rows and the correct number of columns
    assert df.shape[0] == expected_shape[0], f"Expected {expected_shape[0]} rows, got {df.shape[0]}"
    
    # Check if the columns are loaded correctly
    assert "Year" in df.columns, "'Year' column is missing in the DataFrame"
    assert "Temperature" in df.columns, "'Temperature' column is missing in the DataFrame"

def test_file_not_found():
    # Test if FileNotFoundError is raised for a non-existent file
    with pytest.raises(FileNotFoundError):
        load_and_inspect(Path("non_existent_file.csv"))