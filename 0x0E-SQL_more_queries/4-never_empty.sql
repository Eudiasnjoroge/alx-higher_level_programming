-- This script creates the table id_not_null with id and name columns,
-- ensuring that id defaults to 1. The script doesn't fail if the table already exists.

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
