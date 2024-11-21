-- List the number of records with the same score in second_table
-- Results should display the score and the number of records for that score
-- The results should be ordered by the number of records (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
