/*
 
 Problem: 
 
 Write a solution to delete all duplicate emails, 
 keeping only one unique email with the smallest id.
 
 */
-- Write your PostgreSQL query statement below
WITH cte AS (
    SELECT
        id,
        email,
        ROW_NUMBER() OVER (
            PARTITION BY email
            ORDER BY id ASC
        ) AS row_num
    FROM
        person
)
DELETE FROM
    person
WHERE
    id IN (
        SELECT
            id
        FROM
            cte
        WHERE
            row_num > 1
    );