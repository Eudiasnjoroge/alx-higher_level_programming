-- This script computes the average temperature in Fahrenheit for each city
-- and orders the cities by the average temperature in descending order.

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
