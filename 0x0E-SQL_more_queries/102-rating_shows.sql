-- Lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating

SELECT title, SUM(rating) AS rating_sum
FROM tv_shows
GROUP BY title
ORDER BY rating_sum DESC;