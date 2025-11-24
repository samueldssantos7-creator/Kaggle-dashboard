from pathlib import Path
from joblib import dump
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from src.data import load_raw, yearly_agg
from src.features import prepare_regression_features

def main():
    df = load_raw()
    agg = yearly_agg(df, country_col="country", value_col="temp_mean")
    X, y, df_used = prepare_regression_features(agg)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([("model", RandomForestRegressor(n_estimators=200, n_jobs=-1, random_state=42))])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    print("R2:", r2_score(y_test, preds))
    print("RMSE:", mean_squared_error(y_test, preds, squared=False))
    Path("models").mkdir(exist_ok=True)
    dump(pipe, "models/regression_rf.joblib")
    print("Saved: models/regression_rf.joblib")

if __name__ == "__main__":
    main()