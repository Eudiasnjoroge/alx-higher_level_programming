-- This script creates the table unique_id with a unique id column,
-- and ensures it has a default value of 1.

CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
