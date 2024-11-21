-- This script creates the database hbtn_0d_usa and the table states.
-- It ensures the database and table are created only if they don't already exist.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique, auto-generated, not null, primary key
	name VARCHAR(256) NOT NULL          -- Can't be null
);
