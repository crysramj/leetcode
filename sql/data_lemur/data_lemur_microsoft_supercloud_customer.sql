--Microsoft: Supercloud Customer
WITH base_data AS (
    SELECT 
        customer_id,
        SUM(CASE WHEN product_category = 'Analytics' THEN 1 ELSE 0 END) AS analytics,
        SUM(CASE WHEN product_category = 'Containers' THEN 1 ELSE 0 END) AS containers,
        SUM(CASE WHEN product_category = 'Compute' THEN 1 ELSE 0 END) AS compute
    FROM
        customer_contracts
    LEFT JOIN products ON products.product_id = customer_contracts.product_id
    GROUP BY
        customer_id
)
SELECT
    customer_id
FROM
    base_data
WHERE
    analytics = 1
    AND containers = 1
    AND compute = 1;