-- number of shows by genre
SELECT tv_genre.title, COUNT(tv_genre.id) as number_of_shows
FROM tv_genre
JOIN tv_show_genres ON tv_genre_id = tv_show_genres.genre_id;
