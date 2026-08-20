# Architecture

```text
Transactions
    |
    v
Validation + feature engineering
    |
    v
Train/test split
    |
    v
Fraud classification model
    |
    +--> Precision / Recall / PR-AUC
    |
    v
Risk score + decision threshold
```

Fraud detection is evaluated with class-imbalance-aware metrics. The threshold should be selected using business costs for false positives and false negatives rather than accuracy alone.

Use synthetic or de-identified transaction data only.
