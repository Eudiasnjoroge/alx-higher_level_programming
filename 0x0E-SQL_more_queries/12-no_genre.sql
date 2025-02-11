-- This script lists all shows without a linked genre from the hbtn_0d_tvshows database.
-- Results are sorted by tv_shows.title.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
