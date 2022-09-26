from dotenv import load_dotenv, find_dotenv
from os import getenv
from pathlib import Path
import envkey

dotenv_path = Path('.env')
load_dotenv(find_dotenv(raise_error_if_not_found=False))

# Tokens do Facebook
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
AD_ACCOUNT_ID = getenv('AD_ACCOUNT_ID')
APP_SECRET = getenv('APP_SECRET')
APP_ID = getenv('APP_ID')

# Acesso para Postgres
DBNAME = getenv("DBNAME")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
HOST = getenv("HOST")

# Token do Google
CLIENT_CUSTOMER_ID = getenv('CLIENT_CUSTOMER_ID')
DEVELOPER_TOKEN = getenv('DEVELOPER_TOKEN')
REFRESH_TOKEN = getenv('REFRESH_TOKEN')
CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')
USE_PROTO_PLUS = getenv('USE_PROTO_PLUS')
LOGIN_CUSTOMER_ID = getenv('LOGIN_CUSTOMER_ID')
