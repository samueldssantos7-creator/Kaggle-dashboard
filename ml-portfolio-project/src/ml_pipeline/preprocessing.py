def preprocess_data(df):
    # Handle missing values
    df.fillna(df.mean(), inplace=True)
    
    # Scale features
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))
    
    # Create a new DataFrame with scaled features
    scaled_df = pd.DataFrame(scaled_features, columns=df.select_dtypes(include=['float64', 'int64']).columns)
    
    # Concatenate with non-numeric columns
    processed_df = pd.concat([scaled_df, df.select_dtypes(exclude=['float64', 'int64'])], axis=1)
    
    return processed_df