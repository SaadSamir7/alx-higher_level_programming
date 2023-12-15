-- 15-same_score_count.sql

-- List the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;