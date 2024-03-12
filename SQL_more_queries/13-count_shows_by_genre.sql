-- Script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT tv_genres.name AS 'genre', COUNT(*) AS `number_of_shows`
FROM tv_shows_genres LEFT JOIN tv_genres
ON tv_genres.id = tv_shows_genres.genre_id GROUP BY genre_id 
ORDER BY number_of_shows DESC;
