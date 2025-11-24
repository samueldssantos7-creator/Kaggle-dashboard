from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    # Fill missing numerical values with the mean
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    
    # Fill missing categorical values with the mode
    cat_cols = df.select_dtypes(include=[object]).columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = handle_missing_values(df)
    
    # Define categorical and numerical columns
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=[object]).columns.tolist()
    
    # Create a preprocessing pipeline
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, num_cols),
            ('cat', categorical_transformer, cat_cols)
        ]
    )
    
    # Apply the transformations
    df_processed = preprocessor.fit_transform(df)
    
    return pd.DataFrame(df_processed)