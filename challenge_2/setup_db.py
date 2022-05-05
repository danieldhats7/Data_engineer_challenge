from constants import TABLE_NAMES, SQL_DIR
from cfg import DB_CONNSTR
from db_conn import DB_connection


def crete_tables():
    DB_connection(DB_CONNSTR, SQL_DIR).connection_db_for("create_tables", TABLE_NAMES)


def load_data():
    DB_connection(DB_CONNSTR, SQL_DIR).connection_db_for("load_data", TABLE_NAMES)


def setup_db():
    crete_tables()
    load_data()


if __name__ == "__main__":
    setup_db()
