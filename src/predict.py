import pandas as pd
import joblib

def predict_example():
    model = joblib.load("models/sales_model.joblib")

    sample = pd.DataFrame({
        "cantidad": [3],
        "precio_unitario": [1500],
        "categoria": ["Bebidas"],
    })

    prediction = model.predict(sample)
    print("Predicted amount:", prediction[0])

if __name__ == "__main__":
    predict_example()
