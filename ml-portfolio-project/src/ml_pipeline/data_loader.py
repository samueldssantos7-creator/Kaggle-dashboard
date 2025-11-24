import pandas as pd
import os

def load_data(data_type='raw'):
    """
    Load data from the specified directory (raw or processed).
    
    Parameters:
    data_type (str): The type of data to load ('raw' or 'processed').
    
    Returns:
    pd.DataFrame: The loaded dataset.
    """
    if data_type not in ['raw', 'processed']:
        raise ValueError("data_type must be either 'raw' or 'processed'")
    
    data_dir = os.path.join('data', data_type)
    
    # Assuming the data files are in CSV format
    data_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    if not data_files:
        raise FileNotFoundError(f"No CSV files found in the {data_type} directory.")
    
    # Load all data files into a single DataFrame
    data_frames = []
    for file in data_files:
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        data_frames.append(df)
    
    return pd.concat(data_frames, ignore_index=True)