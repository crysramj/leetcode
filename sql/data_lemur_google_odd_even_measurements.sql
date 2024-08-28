--Google: Odd Even Measurements
WITH base_data AS (
    SELECT 
        measurement_id, 
        measurement_value,
        measurement_time,
        ROW_NUMBER() OVER (PARTITION BY measurement_time::date ORDER BY measurement_time ASC) % 2 AS even_odd
    FROM 
        measurements
)
SELECT 
    measurement_time::date AS measurement_day,
    SUM(CASE WHEN even_odd = 1 THEN measurement_value END) AS odd_sum,
    SUM(CASE WHEN even_odd = 0 THEN measurement_value END) AS even_sum
FROM 
    base_data
GROUP BY 
    measurement_time::date
ORDER BY 
    measurement_time::date ASC;