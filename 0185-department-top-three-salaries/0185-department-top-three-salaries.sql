/* Write your T-SQL query statement below */
WITH cte AS (
    SELECT d.name AS Department, 
    e.name as Employee, 
    e.salary AS Salary, 
    DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
FROM Employee e
INNER JOIN Department d
ON e.departmentId = d.id)
SELECT Department, Employee, Salary
FROM cte
WHERE rnk <= 3;