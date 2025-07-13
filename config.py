from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    'driver': os.getenv('DRIVER'),
    'server': os.getenv('SERVER'),
    'database': os.getenv('DATABASE'),
    'trusted_connection': os.getenv('TRUSTED_CONNECTION', 'no').lower() == 'yes',
    'username': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD'),
}