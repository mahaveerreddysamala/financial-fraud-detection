import pandas as pd
from src.features import engineer_features


def test_amount_and_time_features():
    df = pd.DataFrame({"amount": [100.0], "timestamp": ["2026-01-05 14:30:00"]})
    result = engineer_features(df)
    assert "log_amount" in result
    assert result.loc[0, "hour"] == 14
    assert result.loc[0, "day_of_week"] == 0


def test_customer_velocity_counter():
    df = pd.DataFrame({"customer_id": [1, 1, 1], "timestamp": pd.date_range("2026-01-01", periods=3), "amount": [5, 6, 7]})
    result = engineer_features(df)
    assert result["customer_txn_count"].tolist() == [1, 2, 3]
