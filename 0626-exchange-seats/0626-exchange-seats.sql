SELECT 
CASE 
    WHEN id % 2 <> 0 AND id <> total_seats THEN id+1
    WHEN id % 2 <> 0 and id = total_seats THEN id
    ELSE id-1 
END AS id, 
student
FROM Seat 
CROSS JOIN 
(
    SELECT COUNT(1) AS total_seats
    FROM Seat
) AS s
ORDER BY id;