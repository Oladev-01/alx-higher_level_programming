-- this script displays record as a result of a query
SELECT s.title, k.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres k ON s.id = k.show_id
WHERE k.genre_id IS NULL
ORDER BY s.title, k.genre_id;
