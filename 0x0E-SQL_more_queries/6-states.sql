-- this script creates a new table and a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
