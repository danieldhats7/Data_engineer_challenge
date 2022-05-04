from decouple import AutoConfig
from constants import ROOT_DIR

config = AutoConfig(search_path=ROOT_DIR)

USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
PORT = config('PORT')
DATABASE = config('DATABASE')

DB_CONNSTR = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

