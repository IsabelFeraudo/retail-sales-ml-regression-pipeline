# retail-sales-ml-regression-pipeline
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

Project Structure
sales-amount-prediction-ml-pipeline/
│
├── data/                # Raw datasets
├── notebooks/           # Exploratory analysis and modeling
├── src/                 # Reusable ML pipeline code
├── models/              # Trained models
├── figures/             # Generated visualizations
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

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

Run the notebook:

notebooks/aurelion_sales_model.ipynb


The pipeline will:

Load and merge datasets

Clean and transform features

Train multiple regression models

Evaluate performance

Generate predictions

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
