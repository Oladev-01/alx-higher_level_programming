-- this script generates a record as a result of a query
SELECT g.name AS genre, COUNT(a.show_id) AS number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres a ON g.id = a.genre_id
GROUP BY g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
