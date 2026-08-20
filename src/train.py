"""Train a fraud-risk model."""
from __future__ import annotations
import argparse
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from features import engineer_features


def train(path: str, output: str) -> None:
    df = engineer_features(pd.read_csv(path))
    target = "is_fraud"
    if target not in df:
        raise ValueError("CSV must contain is_fraud target")
    X, y = df.drop(columns=[target]), df[target]
    numeric = X.select_dtypes(include="number").columns
    categorical = X.select_dtypes(exclude="number").columns
    prep = ColumnTransformer([
        ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical),
    ])
    model = Pipeline([("prep", prep), ("classifier", RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42, n_jobs=-1))])
    from sklearn.model_selection import train_test_split
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, stratify=y, random_state=42)
    model.fit(Xtr, ytr)
    p = model.predict_proba(Xte)[:, 1]
    print(f"ROC-AUC: {roc_auc_score(yte, p):.4f}")
    print(classification_report(yte, model.predict(Xte)))
    joblib.dump(model, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--output", default="fraud_model.joblib")
    args = parser.parse_args()
    train(args.data, args.output)
