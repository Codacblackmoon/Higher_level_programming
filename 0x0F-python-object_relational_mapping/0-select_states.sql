-- Create states table in hbtn_0e_0_usa with some date
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS STATES (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizone"), ("Texas"), ("New YORK"), ("Nevada");
