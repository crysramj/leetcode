--FAANG: Stock Min-Max
WITH base_data AS (
    SELECT 
        ticker,
        TO_CHAR(date, 'Mon-YYYY') AS mth_format,
        open,
        RANK() OVER (PARTITION BY ticker ORDER BY open DESC) AS highest_open_rank,
        RANK() OVER (PARTITION BY ticker ORDER BY open ASC) AS lowest_open_rank
    FROM stock_prices 
    GROUP BY ticker, mth_format, open
)
SELECT 
    ticker, 
    MAX(CASE WHEN highest_open_rank = 1 THEN mth_format END) AS highest_mth,
    MAX(CASE WHEN highest_open_rank = 1 THEN open END) AS highest_open,
    MAX(CASE WHEN lowest_open_rank = 1 THEN mth_format END) AS lowest_mth,
    MAX(CASE WHEN lowest_open_rank = 1 THEN open END) AS lowest_open
FROM base_data
GROUP BY ticker;
