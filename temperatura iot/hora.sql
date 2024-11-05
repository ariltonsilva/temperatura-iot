CREATE VIEW leituras_por_hora AS
SELECT DATE_PART('hour', reading_time) AS hora, COUNT(*) AS contagem
FROM temperature_readings
GROUP BY DATE_PART('hour', reading_time);