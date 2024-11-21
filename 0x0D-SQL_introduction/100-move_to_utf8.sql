-- This script converts the `hbtn_0c_0` database, `first_table` table, and `name` field to UTF8 (utf8mb4).
-- The collation will be set to utf8mb4_unicode_ci for better compatibility.

-- Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the `first_table` table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the `name` field in `first_table` to utf8mb4
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
