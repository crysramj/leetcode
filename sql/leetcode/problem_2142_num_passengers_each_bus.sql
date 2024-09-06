-- Write your PostgreSQL query statement below
WITH bus_times AS (
    SELECT
        bus_id,
        arrival_time,
        COALESCE(
            LAG(arrival_time) OVER (ORDER BY arrival_time ASC),
            0
        ) AS prior_time
    FROM buses
    ORDER BY arrival_time ASC
),
arrival_times_per_passenger AS (
    SELECT
        passengers.passenger_id,
        passengers.arrival_time AS passenger_arrival_time,
        bus_times.bus_id,
        bus_times.arrival_time,
        RANK() OVER (
            PARTITION BY passenger_id
            ORDER BY bus_times.arrival_time ASC
        ) AS arrival_time_rank
    FROM passengers
    LEFT JOIN bus_times
        ON passengers.arrival_time <= bus_times.arrival_time
        AND passengers.arrival_time >= bus_times.prior_time
),
arrival_times_per_passenger_agg AS (
    SELECT
        bus_id,
        COUNT(
            CASE 
                WHEN arrival_time_rank = 1 THEN bus_id 
            END
        ) AS passengers_cnt
    FROM arrival_times_per_passenger
    WHERE arrival_time_rank = 1
    GROUP BY bus_id
)
SELECT 
    buses.bus_id,
    COALESCE(
        arrival_times_per_passenger_agg.passengers_cnt,
        0
    ) AS passengers_cnt
FROM buses
LEFT JOIN arrival_times_per_passenger_agg
    ON arrival_times_per_passenger_agg.bus_id = buses.bus_id
ORDER BY buses.bus_id ASC;