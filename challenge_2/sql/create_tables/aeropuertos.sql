DROP TABLE IF EXISTS aeropuertos CASCADE;

CREATE TABLE aeropuertos (
    id_aeropuerto SERIAL PRIMARY KEY,
    nombre_aeropuerto VARCHAR(50) NOT NULL);
