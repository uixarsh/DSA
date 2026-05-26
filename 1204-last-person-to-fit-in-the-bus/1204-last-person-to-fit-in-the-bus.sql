/* Write your T-SQL query statement below */
WITH cte AS (
        SELECT *,
                SUM(weight) OVER (ORDER BY turn) AS rolling_wt
        FROM Queue)
SELECT TOP 1 person_name
FROM cte
WHERE rolling_wt <= 1000
ORDER BY turn DESC;