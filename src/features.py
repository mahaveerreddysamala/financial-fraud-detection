"""Transaction feature engineering."""
from __future__ import annotations
import pandas as pd


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data.columns = [c.strip().lower().replace(" ", "_") for c in data.columns]
    if "amount" in data:
        data["log_amount"] = (data["amount"].clip(lower=0) + 1).apply(__import__("math").log)
    if "timestamp" in data:
        data["timestamp"] = pd.to_datetime(data["timestamp"], errors="coerce")
        data["hour"] = data["timestamp"].dt.hour
        data["day_of_week"] = data["timestamp"].dt.dayofweek
    if {"customer_id", "timestamp"}.issubset(data.columns):
        data = data.sort_values(["customer_id", "timestamp"])
        data["customer_txn_count"] = data.groupby("customer_id").cumcount() + 1
    return data
