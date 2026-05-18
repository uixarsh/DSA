/* Write your T-SQL query statement below */


SELECT s1.product_id, first_year, quantity, price
FROM Sales s1
INNER JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) s2
ON s1.product_id = s2.product_id AND s1.year = s2.first_year;