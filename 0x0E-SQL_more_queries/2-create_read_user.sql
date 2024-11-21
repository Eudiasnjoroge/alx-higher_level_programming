-- This script creates the database hbtn_0d_2 if it doesn't already exist,
-- creates the user user_0d_2 with a password, grants SELECT privilege on the database,
-- and ensures the script doesn't fail if the database or user already exists.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the hbtn_0d_2 database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
