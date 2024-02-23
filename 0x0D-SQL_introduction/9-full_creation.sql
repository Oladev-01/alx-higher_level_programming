-- this script creates a new table called second_table
CREATE table IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- inserts the data after creating the table

INSERT INTO second_table(id, name, score)
VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(4, 'Bob', 14),
(5, 'George', 8);
