-- 103-max_state.sql

-- Display the max temperature of each state, ordered by State name
SELECT state, MAX(temperature) AS max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;