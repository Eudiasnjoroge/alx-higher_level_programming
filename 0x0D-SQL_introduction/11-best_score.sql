-- List all records of second_table with score >= 10, ordered by score (top first)
-- Display both score and name (in this order)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
