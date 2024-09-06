/*
 
 Problem: 
 
 Write a solution to:
 Find the name of the user who has rated the greatest number of movies.
 In case of a tie, return the lexicographically smaller user name.
 Find the movie name with the highest average rating in February 2020. 
 In case of a tie, return the lexicographically smaller movie name.
 
 
 */
-- Write your PostgreSQL query statement below
WITH user_with_greatest_num_movies AS (
    SELECT
        MovieRating.user_id,
        Users.name,
        COUNT(DISTINCT movie_id) AS num_movies
    FROM
        MovieRating
    LEFT JOIN Users ON Users.user_id = MovieRating.user_id
    GROUP BY
        MovieRating.user_id,
        Users.name
    ORDER BY
        num_movies DESC,
        Users.name ASC
    LIMIT
        1
),
movie_with_highest_avg_rating AS (
    SELECT
        MovieRating.movie_id,
        Movies.title,
        AVG(rating) AS avg_rating
    FROM
        MovieRating
    LEFT JOIN Movies ON Movies.movie_id = MovieRating.movie_id
    WHERE
        created_at BETWEEN '2020-02-01' AND '2020-02-28'
    GROUP BY
        MovieRating.movie_id,
        Movies.title
    ORDER BY
        avg_rating DESC,
        Movies.title ASC
    LIMIT
        1
)
SELECT
    name AS results
FROM
    user_with_greatest_num_movies
UNION ALL
SELECT
    title AS results
FROM
    movie_with_highest_avg_rating;