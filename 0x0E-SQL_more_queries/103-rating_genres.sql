SELECT tv_genres.name, SUM(tv_show_ratings.rating) AS rating
FROM tv_genres
JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
JOIN tv_show_ratings ON tv_shows_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
