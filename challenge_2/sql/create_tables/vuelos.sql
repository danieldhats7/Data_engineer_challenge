DROP TABLE IF EXISTS vuelos CASCADE;

CREATE TABLE vuelos(
    id_aerolinea INTEGER REFERENCES aerolineas (id_aerolinea),
    id_aeropuerto INTEGER REFERENCES aeropuertos (id_aeropuerto),
    id_movimiento INTEGER REFERENCES movimientos (id_movimiento),
    dia DATE NOT NULL);
