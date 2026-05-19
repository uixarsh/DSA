/* Write your T-SQL query statement below */
SELECT CASE WHEN COUNT(1) = 2 THEN MIN(salary) END AS SecondHighestSalary
FROM (
SELECT TOP 2 salary
FROM Employee
GROUP BY salary
ORDER BY salary DESC 
) AS resultant_data