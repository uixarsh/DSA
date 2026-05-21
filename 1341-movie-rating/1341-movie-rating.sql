/* Write your T-SQL query statement below */
WITH 
top_user AS (
    SELECT TOP 1 u.name AS results
    FROM MovieRating mr
    INNER JOIN Users u
    ON mr.user_id = u.user_id
    GROUP BY u.name
    ORDER BY COUNT(1) DESC, u.name ASC
),
top_movie AS (
    SELECT TOP 1 m.title AS results
    FROM Movies m
    INNER JOIN MovieRating mr
    ON m.movie_id = mr.movie_id
    WHERE created_at >= '2020-02-01' AND created_at < '2020-03-01'
    GROUP BY title
    ORDER BY AVG(rating * 1.0) DESC, m.title ASC
)
SELECT * FROM top_user
UNION ALL
SELECT * FROM top_movie;