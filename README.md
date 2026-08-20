# Financial Fraud Detection

An end-to-end machine learning project for detecting suspicious financial transactions and prioritizing investigations.

## Business Goal

Fraud teams need to identify high-risk transactions quickly while controlling false positives. This project combines transaction behavior, merchant attributes, velocity features, and supervised classification to produce a fraud-risk score.

## Stack

- Python, Pandas, NumPy
- Scikit-learn
- SQL
- Matplotlib / Seaborn
- Joblib
- Pytest

## Workflow

1. Validate transaction data and remove duplicates.
2. Engineer transaction velocity and behavioral features.
3. Handle class imbalance using class-weighted models.
4. Train and compare Logistic Regression and Random Forest classifiers.
5. Evaluate ROC-AUC, precision, recall, F1, and precision-recall tradeoffs.
6. Generate a ranked investigation queue from predicted fraud probability.

## Repository Structure

```text
financial-fraud-detection/
├── data/README.md
├── src/
│   ├── __init__.py
│   ├── features.py
│   └── train.py
├── sql/fraud_monitoring.sql
├── tests/test_features.py
├── requirements.txt
└── README.md
```

## Key Metric

For fraud detection, accuracy alone is misleading because legitimate transactions usually outnumber fraudulent ones. The project therefore emphasizes **precision, recall, PR-AUC/ROC-AUC, and investigation capacity**.

## Data Safety

No real payment information is included. Use synthetic or properly de-identified data and never commit card numbers, account credentials, or other sensitive information.
