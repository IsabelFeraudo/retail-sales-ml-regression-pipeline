from src.train import train_model
from src.evaluate import evaluate_model
from src.predict import predict_example

def run_pipeline():
    print("\nTRAINING MODEL")
    train_model()

    print("\nEVALUATING MODEL")
    evaluate_model()

    print("\nRUNNING SAMPLE PREDICTION")
    predict_example()

    print("\nPipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
