import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor

from src.data_loader import load_data
from src.preprocessing import build_preprocessor

def train_model():
    df = load_data()

    X = df[["cantidad", "precio_unitario", "categoria"]]
    y = df["importe"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline(
        steps=[
            ("preprocess", build_preprocessor()),
            ("model", RandomForestRegressor(random_state=42)),
        ]
    )

    param_grid = {
        "model__n_estimators": [100, 300],
        "model__max_depth": [None, 10, 20],
    }

    grid = GridSearchCV(
        pipeline,
        param_grid,
        cv=5,
        scoring="r2",
        n_jobs=-1,
    )

    grid.fit(X_train, y_train)

    joblib.dump(grid.best_estimator_, "models/sales_model.joblib")

    print("Best parameters:", grid.best_params_)
    print("Model saved to models/sales_model.joblib")

if __name__ == "__main__":
    train_model()
