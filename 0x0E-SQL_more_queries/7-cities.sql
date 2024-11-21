-- This script creates the database hbtn_0d_usa and the table cities.
-- The table cities has a foreign key referencing the states table.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table cities if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique, auto-generated, not null, primary key
	state_id INT NOT NULL,                 -- Foreign key reference to states table
	name VARCHAR(256) NOT NULL,            -- Can't be null
	FOREIGN KEY (state_id) REFERENCES states(id)  -- Foreign key constraint
);
