-- this script creates a new database and a new user
-- creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';
-- granting select privilege to the new user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';
