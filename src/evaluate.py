import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from src.data_loader import load_data

def evaluate_model():
    df = load_data()

    X = df[["cantidad", "precio_unitario", "categoria"]]
    y = df["importe"]

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = joblib.load("models/sales_model.joblib")
    preds = model.predict(X_test)

    print("MAE:", mean_absolute_error(y_test, preds))
    print("RMSE:", mean_squared_error(y_test, preds, squared=False))
    print("R2:", r2_score(y_test, preds))

if __name__ == "__main__":
    evaluate_model()
