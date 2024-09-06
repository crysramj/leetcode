/*
 
 Problem: 
 
 Write a solution to find the id and the name of active users.
 
 */
-- Write your PostgreSQL query statement below

WITH distinct_date_ids as (
    SELECT DISTINCT * 
    FROM logins
), 

base_data AS (
    SELECT  
        id,
        login_date,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY login_date ASC) AS num_con,
        login_date - (ROW_NUMBER() OVER (PARTITION BY id ORDER BY login_date ASC) || ' days')::interval AS consecutive_grouping_date
    FROM distinct_date_ids
)

SELECT DISTINCT
    base_data.id,
    accounts.name 
FROM base_data
LEFT JOIN accounts ON accounts.id = base_data.id
GROUP BY base_data.id, accounts.name, consecutive_grouping_date
HAVING COUNT(1) >= 5
ORDER BY base_data.id ASC;