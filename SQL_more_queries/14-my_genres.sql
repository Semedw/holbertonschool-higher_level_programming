-- my genres
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_genres.name ASC;
