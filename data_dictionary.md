# Data Dictionary

## fund_master
- amfi_code : Unique fund identifier
- scheme_name : Mutual fund scheme name
- fund_house : AMC/Fund house
- category : Fund category

## nav_history
- amfi_code : Fund identifier
- date : NAV date
- nav : Net Asset Value

## investor_transactions
- investor_id : Investor identifier
- transaction_date : Date of transaction
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction amount

## scheme_performance
- return_1yr_pct : 1 year return
- return_3yr_pct : 3 year return
- return_5yr_pct : 5 year return
- expense_ratio_pct : Expense ratio