-- this script displays a record as a result of a query
-- Using a subquery to get the genre id for Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;