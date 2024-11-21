-- This script creates the table force_name with id and name columns,
-- ensuring that name can't be null. It doesn't fail if the table already exists.

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);

