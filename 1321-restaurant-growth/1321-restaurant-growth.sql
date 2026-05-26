/* Write your T-SQL query statement below */
WITH q1 AS (
        SELECT visited_on,
            SUM(amount) AS sale_that_day
        FROM Customer
        GROUP BY visited_on),
    q2 AS (SELECT visited_on,
                SUM(sale_that_day) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
                ROUND(AVG(sale_that_day*1.0) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount,
                ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
            FROM q1)
SELECT visited_on,
        amount,
        average_amount
FROM q2
WHERE rn >= 7;