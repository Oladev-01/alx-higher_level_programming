-- this script displays a record as a result of a query
SELECT g.name
FROM tv_genres g
JOIN tv_show_genres k ON g.id = k.genre_id
JOIN tv_shows s ON k.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
