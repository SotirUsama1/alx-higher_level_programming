-- displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending).
SELECT city, avg(value) AS 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg(value) DESC;