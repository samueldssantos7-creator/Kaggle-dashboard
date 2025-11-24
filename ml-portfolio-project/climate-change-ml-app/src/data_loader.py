from pathlib import Path
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)

def get_data() -> pd.DataFrame:
    file_path = Path(__file__).resolve().parent.parent / 'data' / 'raw' / 'Global_Climate_Change_Data_2020_2025.csv'
    return load_data(file_path)