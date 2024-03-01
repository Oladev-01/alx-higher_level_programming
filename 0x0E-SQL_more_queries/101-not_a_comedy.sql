-- this script displays a record as a result of a query
-- Using a subquery to get the genre id for Comedy
SELECT tv_shows.title 
FROM tv_shows
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy' AND tv_show_genres.show_id = tv_shows.id
)
ORDER BY tv_shows.title ASC;
