import sys
from os import path
from environs import Env

LOGGING_FILE = "flask.log"
LOGGING_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
DATA_FMT = '%y.%b.%d %H:%M:%S'

ENV_FILE = './.env'

if path.exists(ENV_FILE):
    envir = Env()
    envir.read_env()
else:
    print("Error .env file not found")
    sys.exit(1)

YOUTUBE_TOKEN = envir('YOUTUBE_TOKEN')
