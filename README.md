# Retail-sales Machine Learning regression pipeline
End-to-end machine learning pipeline for retail sales amount prediction using tabular data, feature preprocessing, and model evaluation.

Sales Amount Prediction — End-to-End Machine Learning Pipeline
## Author

Isabel Feraudo
Full-Stack Developer - Machine Learning Oriented

## Project Overview

This project implements an end-to-end Machine Learning pipeline to predict the total sales amount of a retail transaction line using structured tabular data.
The model learns relationships between quantity, unit price, and product category to estimate transaction value and support data-driven business decisions.
This repository demonstrates production-style ML practices including data preprocessing, model comparison, pipelines, evaluation metrics, and reproducible experimentation.

## Machine Learning Features Demonstrated

✔ Data cleaning and feature engineering
✔ Tabular regression modeling
✔ Scikit-learn preprocessing pipelines
✔ Categorical encoding with OneHotEncoder
✔ Model comparison (Linear Regression vs Random Forest)
✔ Train/Test split methodology
✔ Evaluation using MAE, RMSE and R²
✔ Reproducible workflow
✔ Model-ready structure for deployment

## Dataset Description

The dataset simulates a retail sales system with relational structure:
Customers
Products (with category)
Sales transactions
Transaction details
Target variable:
Total Amount = Quantity × Unit Price
Features used:
Quantity
Unit Price
Product Category

## Installation

Clone repository:
git clone https://github.com/YOUR_USERNAME/sales-amount-prediction-ml-pipeline.git
cd sales-amount-prediction-ml-pipeline

Create virtual environment:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

## Usage

unning the Full ML Pipeline
Run the complete workflow (training, evaluation, and prediction):
python run_pipeline.py
This script will:
Load and preprocess data
Train the model with cross-validation
Save the best model
Evaluate performance
Generate a sample prediction

## Running Individual Components

### Train model only:
python src/train.py

### Evaluate trained model:
python src/evaluate.py

### Run prediction example:
python src/predict.py

## Project Structure
sales-amount-prediction-ml-pipeline/
│
├── data/                # Raw datasets
├── notebooks/           # Exploratory analysis
├── src/                 # ML pipeline modules
├── models/              # Saved models
├── run_pipeline.py      # End-to-end execution script
├── requirements.txt
└── README.md

## Results

Random Forest Regressor achieved the best predictive performance, capturing non-linear relationships between price, quantity, and category.

Key insight:
Sales amount is primarily driven by price and quantity, while product category provides additional predictive signal.

## Future Improvements

Hyperparameter optimization with cross-validation
Feature importance analysis
Model persistence and loading
API deployment with FastAPI
Interactive dashboard with Streamlit
MLOps pipeline integration

## Tech Stack

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn

## Portfolio Context

This project is part of my Machine Learning portfolio focused on real-world business prediction problems using structured data and reproducible pipelines.
