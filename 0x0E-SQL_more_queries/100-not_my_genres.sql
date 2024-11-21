-- Step 1: Find the genres linked to Dexter
-- Step 2: Select all genres except those linked to Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
       	SELECT genre_id
	FROM tv_show_genres
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;

