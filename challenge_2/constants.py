from pathlib import Path

ROOT_DIR = Path().resolve().parent
SQL_DIR = ROOT_DIR / "challenge_2/sql"

AIRLINES_TABLE_NAME = 'aerolineas'
AIRPORTS_TABLE_NAME = 'aeropuertos'
MOVEMENTS_TABLE_NAME = 'movimientos'
FLIGHTS_REVIEWS_TABLE_NAME = 'vuelos'

TABLE_NAMES = [
    AIRLINES_TABLE_NAME,
    AIRPORTS_TABLE_NAME,
    MOVEMENTS_TABLE_NAME,
    FLIGHTS_REVIEWS_TABLE_NAME
]
