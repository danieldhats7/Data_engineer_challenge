from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd


class DB_connection:
    def __init__(self, DB_CONNSTR, SQL_DIR):
        self.engine = create_engine(DB_CONNSTR)
        self.SQL_DIR = SQL_DIR

    def connection_db_for(self, conn_type: str, sql_file_names) -> None:
        """connection to data base for crate tables or load data

        Args:
            conn_type (str): type of connection [create_tables, load_data]
            sql_file_names (list(str)): list of sql files names
        """

        with self.engine.connect() as con:
            for file in sql_file_names:
                with open(self.SQL_DIR / f"{conn_type}/{file}.sql") as f:
                    query = text(f.read())
                con.execute(query)
                print(f"{file}.sql for {conn_type} executed!")
        print(f"{conn_type} finished!")

    def db_query(self, sql_file) -> pd.DataFrame:
        """query to data base

        Args:
            sql_file (str): name of sql file

        Returns:
            pd.DataFrame: result of query
        """

        with self.engine.connect() as con:
            with open(self.SQL_DIR / f"querys/{sql_file}.sql") as f:
                query = text(f.read())
            rs = con.execute(query)
        return pd.DataFrame(rs.fetchall())
