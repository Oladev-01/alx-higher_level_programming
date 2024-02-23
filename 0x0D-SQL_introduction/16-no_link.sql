-- this script list the records of the table with exception of name that have no value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
