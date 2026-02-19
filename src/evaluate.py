import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
from src.data_loader import load_data

def evaluate_model():
    df = load_data()

    X = df[["cantidad", "precio_unitario", "categoria"]]
    y = df["importe"]

    model = joblib.load("models/sales_model.joblib")

    preds = model.predict(X)

    mae = mean_absolute_error(y, preds)
    rmse = np.sqrt(mean_squared_error(y, preds))

    print("MAE:", mae)
    print("RMSE:", rmse)
