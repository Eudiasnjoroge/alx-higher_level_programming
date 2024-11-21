-- Convert the database hbtn_0c_0 to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Convert table first_table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Convert field name in first_table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Change the database character set and collation
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Change the table first_table character set and collation
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Change the column 'name' in first_table to UTF8 (utf8mb4, collation utf8mb4_unicode_ci)
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
