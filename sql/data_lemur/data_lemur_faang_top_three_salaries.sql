--FAANG: Top Three Salaries
WITH base_data AS (
    SELECT
        department.department_name,
        employee.name,
        employee.salary,
        DENSE_RANK() OVER (
            PARTITION BY employee.department_id
            ORDER BY employee.salary DESC
        ) AS department_salary_rank
    FROM
        employee
    LEFT JOIN department ON department.department_id = employee.department_id
)
SELECT
    department_name,
    name,
    salary
FROM
    base_data
WHERE
    department_salary_rank <= 3
ORDER BY
    department_name ASC,
    salary DESC,
    name ASC;