from pathlib import Path
import pandas as pd
import logging

def setup_logging(log_file: str):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def log_dataframe_info(df: pd.DataFrame, name: str):
    logging.info(f"DataFrame '{name}' loaded with shape: {df.shape}")
    logging.info(f"Columns: {list(df.columns)}")
    logging.info(f"Missing values:\n{df.isna().sum()}")

def save_plot(figure, filename: str):
    figure.savefig(filename)
    logging.info(f"Plot saved as: {filename}")

def load_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    log_dataframe_info(df, Path(file_path).name)
    return df

def display_dataframe(df: pd.DataFrame, nrows: int = 5):
    return df.head(nrows)