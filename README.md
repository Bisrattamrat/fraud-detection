# Fraud Detection Project

## Business Problem

Adey Innovations seeks to improve fraud detection across e-commerce and banking transactions.

## Datasets

- Fraud_Data.csv
- creditcard.csv
- IpAddress_to_Country.csv

## Interim-1 Progress

Completed:

- Data Cleaning
- Missing Value Analysis
- Duplicate Detection
- Exploratory Data Analysis
- Class Imbalance Analysis
- Feature Engineering
- Time Since Signup Feature
- Hour Of Day Feature
- Day Of Week Feature
- Transaction Frequency Feature
- IP Address Conversion
- Fraud Pattern Investigation

## Class Imbalance Strategy

SMOTE will be used during model training to address severe class imbalance while preserving legitimate transaction information.
## Reproducible Pipeline Improvements

Following reviewer feedback, the project was refactored to improve maintainability and reproducibility.

Enhancements include:

- Separation of exploratory notebooks from production code.
- Creation of reusable preprocessing functions in src/data_preprocessing.py.
- Creation of reusable feature engineering functions in src/feature_engineering.py.
- Added basic error handling for dataset loading.
- Improved repository structure to support future modeling and SHAP explainability tasks.

These improvements prepare the project for model training, evaluation, explainability, and collaboration.