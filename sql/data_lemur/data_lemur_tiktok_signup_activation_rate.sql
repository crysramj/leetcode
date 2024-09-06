--Tiktok: Activation Rate
WITH signups AS (
    SELECT
        email_id
    FROM
        texts
    WHERE
        signup_action = 'Confirmed'
)
SELECT
    ROUND(
        COUNT(signups.email_id)::DECIMAL / COUNT(emails.email_id)::DECIMAL,
        2
    ) AS confirm_rate
FROM
    emails
    LEFT JOIN signups ON signups.email_id = emails.email_id;