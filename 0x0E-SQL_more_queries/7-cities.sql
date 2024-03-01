-- this script creates a new table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL
);
