--Uber: User's Third Transaction
WITH base_data AS (
    SELECT
        user_id,
        spend,
        transaction_date,
        RANK() OVER (
            PARTITION BY user_id
            ORDER BY transaction_date ASC
        ) AS row_num
    FROM
        transactions
)
SELECT
    user_id,
    spend,
    transaction_date
FROM
    base_data
WHERE
    row_num = 3;