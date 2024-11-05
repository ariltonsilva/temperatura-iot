CREATE TABLE temperature_readings (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50),
    temp_value FLOAT,
    reading_time TIMESTAMP
);


-- Inserir alguns dados de exemplo na tabela
INSERT INTO temperature_readings (device_id, temp_value, reading_time) VALUES
('sensor_1', 23.4, '2023-10-10 14:00:00'),
('sensor_2', 22.1, '2023-10-10 14:05:00'),
('sensor_1', 24.0, '2023-10-10 14:10:00'),
('sensor_2', 23.5, '2023-10-10 14:15:00');
