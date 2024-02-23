-- this script displays the number of records of data with the same 
-- score in the database
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
