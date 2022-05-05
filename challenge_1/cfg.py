from decouple import AutoConfig
from pathlib import Path

ROOT_DIR = Path().resolve().parent

config = AutoConfig(ROOT_DIR)

URL = config("URL")
