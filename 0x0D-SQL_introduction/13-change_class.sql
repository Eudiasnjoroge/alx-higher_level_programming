-- Remove all records with a score <= 5 from second_table
-- Only records with a score greater than 5 will remain

DELETE FROM second_table
WHERE score <= 5;
