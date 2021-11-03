import sys
from os import path
from environs import Env

LOGGING_FILE = "flask.log"
LOGGING_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
DATA_FMT = '%y.%b.%d %H:%M:%S'

ENV_FILE = './.env'

envir = Env()
envir.read_env()

YOUTUBE_TOKEN = envir('YOUTUBE_TOKEN')
