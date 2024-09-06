/*
 
 Problem: 
 
 Write a solution to find the second highest salary from the Employee table. 
 If there is no second highest salary, return null.
 
 */
-- Write your PostgreSQL query statement below
WITH cte AS (
    SELECT
        id,
        salary,
        DENSE_RANK() OVER (
            ORDER BY salary DESC
        ) AS salary_rank
    FROM
        employee
)
SELECT
    CASE
        WHEN COUNT(*) < 1 THEN NULL
        ELSE MAX(salary)
    END AS SecondHighestSalary
FROM
    cte
WHERE
    salary_rank = 2;