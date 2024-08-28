--FAANG: Second Highest Salary
WITH base_data AS (
    SELECT
        employee_id,
        salary,
        RANK() OVER (
            ORDER BY salary DESC
        ) AS rank
    FROM
        employee
)
SELECT
    salary
FROM
    base_data
WHERE
    rank = 2;