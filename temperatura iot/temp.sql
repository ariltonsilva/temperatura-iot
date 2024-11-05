CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temp_value) AS avg_temp
FROM temperature_readings
GROUP BY device_id;