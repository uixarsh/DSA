/* Write your T-SQL query statement below */

SELECT ROUND(
(SELECT COUNT(1) * 1.0 AS players_who_logged_in_after_day
FROM Activity a1
INNER JOIN (
    SELECT player_id, MIN(event_date) AS first_day
    FROM Activity
    GROUP BY player_id
) AS a2
ON a1.player_id = a2.player_id AND DATEDIFF(DAY, a2.first_day, a1.event_date) = 1)
/ COUNT(DISTINCT player_id), 2) AS fraction
FROM Activity;