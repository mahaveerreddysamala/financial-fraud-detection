-- Daily monitoring view for transaction risk operations.
SELECT
    CAST(transaction_time AS DATE) AS transaction_date,
    merchant_category,
    COUNT(*) AS transactions,
    SUM(amount) AS total_amount,
    SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) AS fraud_count,
    ROUND(AVG(CASE WHEN is_fraud = 1 THEN 1.0 ELSE 0.0 END), 4) AS fraud_rate
FROM transactions
GROUP BY CAST(transaction_time AS DATE), merchant_category
ORDER BY transaction_date DESC, fraud_rate DESC;
