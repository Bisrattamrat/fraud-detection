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

These improvements prepare the project for model training, evaluation, explainability, and collaboration.- Fraud detection capability
- Robustness
- Interpretability
- Generalization ability

Random Forest was selected as the preferred model because it achieved stronger fraud detection performance.

---

11. Model Persistence

The selected model was saved using Joblib.

Saved Model:

models/random_forest.pkl

This allows future deployment without retraining.

---

12. Challenges Encountered

Challenges included:

- Class imbalance
- Feature selection
- Model tuning
- Dataset size
- Environment setup issues

These challenges were addressed using SMOTE, model optimization, and reproducible workflows.

---

13. Conclusion

Task 2 successfully completed:

- Data preparation
- Stratified train-test split
- SMOTE balancing
- Logistic Regression training
- Random Forest training
- Hyperparameter tuning
- Cross Validation
- Model comparison
- Model persistence

The next phase will focus on model explainability using SHAP, feature importance analysis, and business recommendations.