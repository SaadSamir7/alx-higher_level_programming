-- 102-top_city.sql

-- Display the top 3 cities' temperatures during July and August, ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
WHERE MONTH(date) IN (7, 8) -- Filter for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;