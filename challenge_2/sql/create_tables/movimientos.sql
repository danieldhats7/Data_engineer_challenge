DROP TABLE IF EXISTS movimientos CASCADE;

CREATE TABLE movimientos(
    id_movimiento SERIAL PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL);
