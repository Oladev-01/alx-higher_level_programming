-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;

USE hbtn_0e_100_usa;

SELECT cities.id, cities.name FROM states;

SELECT * FROM cities;

SELECT cities.id, states.name, cities.name FROM cities JOIN states where cities.id=states.id