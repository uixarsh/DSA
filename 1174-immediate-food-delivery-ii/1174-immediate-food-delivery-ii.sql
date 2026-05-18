/* Write your T-SQL query statement below */
WITH cte AS (
    SELECT customer_id, MIN(order_date) AS first_order
    FROM Delivery
    GROUP BY customer_id
)
SELECT ROUND(SUM(CASE WHEN order_date=customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(1), 2) AS immediate_percentage 
FROM Delivery d
INNER JOIN cte
ON cte.customer_id = d.customer_id AND cte.first_order = d.order_date;