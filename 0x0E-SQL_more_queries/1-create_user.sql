-- This script creates the MySQL user 'user_0d_1' if it doesn't exist already,
-- grants all privileges to the user, and sets the user's password.

-- Check if the user exists, and if not, create it
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;
