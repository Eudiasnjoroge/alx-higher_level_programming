-- This script lists all genres and the number of shows linked to each genre from the hbtn_0d_tvshows database.
-- Results are sorted by the number of shows linked, in descending order.

SELECT tv_genres.genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.genre
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
