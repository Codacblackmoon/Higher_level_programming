-- converts hbtn_0c_)=0 database to utf8
-- table: first_table to utf8
-- field: name to utf8

ALTER DATABASE htbn_0c_0 CHARCTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT to CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
