-- This script displays the top 3 cities by temperature during July and August,
-- ordered by average temperature in descending order.

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- Filter by July (7) and August (8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
