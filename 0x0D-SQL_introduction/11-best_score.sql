-- this scripts list score and name with scores >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
