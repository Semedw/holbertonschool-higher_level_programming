-- my genres
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id = (
	SELECT tv_show_genres.genre.id
	FROM tv_show_genre)
	
