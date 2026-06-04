-- Total Funds
SELECT COUNT(*) FROM dim_fund;

-- Average NAV
SELECT AVG(nav) FROM fact_nav;

-- Top 10 NAV Values
SELECT * FROM fact_nav
ORDER BY nav DESC
LIMIT 10;

-- Transaction Count
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Total Investment Amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- Best 1 Year Return
SELECT MAX(return_1yr_pct)
FROM fact_performance;

-- Best 3 Year Return
SELECT MAX(return_3yr_pct)
FROM fact_performance;

-- Best 5 Year Return
SELECT MAX(return_5yr_pct)
FROM fact_performance;

-- Total NAV Records
SELECT COUNT(*)
FROM fact_nav;