-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating

SELECT name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
JOIN tv_shows ON tv_shows_genres.show_id = tv_shows.id
GROUP BY name
ORDER BY rating_sum DESC;