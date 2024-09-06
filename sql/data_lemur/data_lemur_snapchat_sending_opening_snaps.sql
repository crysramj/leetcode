--Snapchat: Sending vs. Opening Snaps
WITH base_data AS (
    SELECT
        age_bucket,
        SUM(
            CASE
                WHEN activity_type = 'open' THEN time_spent
            END
        ) AS open_time,
        SUM(
            CASE
                WHEN activity_type = 'send' THEN time_spent
            END
        ) AS send_time,
        SUM(
            CASE
                WHEN activity_type IN ('send', 'open') THEN time_spent
            END
        ) AS open_spend_time
    FROM
        activities
    LEFT JOIN age_breakdown ON age_breakdown.user_id = activities.user_id
    GROUP BY
        age_bucket
)
SELECT
    age_bucket,
    ROUND(send_time / open_spend_time * 100, 2) AS send_perc,
    ROUND(open_time / open_spend_time * 100, 2) AS open_perc
FROM
    base_data;