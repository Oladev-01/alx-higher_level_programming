-- this script displays a record as a result of a query
SELECT title
FROM tv_shows
WHERE id NOT IN (
SELECT show_id FROM tv_show_genres WHERE genre_id = (
SELECT id FROM tv_genres WHERE name='Comedy'
))
ORDER BY tv_shows.title ASC;
