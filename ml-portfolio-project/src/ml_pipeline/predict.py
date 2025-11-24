def make_prediction(model, input_data):
    """
    Make predictions using the trained model.

    Parameters:
    model: The trained machine learning model.
    input_data: The data for which predictions are to be made.

    Returns:
    predictions: The predicted values.
    """
    predictions = model.predict(input_data)
    return predictions