from constants import SQL_DIR
from cfg import DB_CONNSTR
from db_conn import DB_connection
import click


@click.command()
@click.argument("number", type=click.Choice(["1", "2", "3", "4"]))
def query(number):
    df_rs = DB_connection(DB_CONNSTR, SQL_DIR).db_query(f"query_{number}")
    print(df_rs)


if __name__ == "__main__":
    query()
