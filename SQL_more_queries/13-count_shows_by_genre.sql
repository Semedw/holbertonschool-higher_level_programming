-- number of shows by genre
SELECT tv_genres.name, COUNT(tv_show_genres.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id;
