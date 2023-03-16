-- Creates the user user_0d_1 with all privileges
CREAT USER
	IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	NO *.*
	TO 'user_0d_1'@'localhost';
