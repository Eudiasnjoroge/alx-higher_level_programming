-- Step 1: Identify the genre_id for Comedy
-- Step 2: Find all shows that are not linked to the Comedy genre
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id != (SELECT id FROM tv_genres WHERE name = 'Comedy')
   OR tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title;
