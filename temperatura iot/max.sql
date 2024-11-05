CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(reading_time) AS data, MAX(temp_value) AS temp_max, MIN(temp_value) AS temp_min
FROM temperature_readings
GROUP BY DATE(reading_time);
