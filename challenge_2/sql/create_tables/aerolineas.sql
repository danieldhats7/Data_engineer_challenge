DROP TABLE  IF EXISTS  aerolineas CASCADE;

CREATE TABLE aerolineas (
    id_aerolinea SERIAL PRIMARY KEY,
    nombre_aerolinea VARCHAR(50) NOT NULL);
