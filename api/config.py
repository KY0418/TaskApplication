from dotenv import load_dotenv
load_dotenv()

import os

DB_PASS = os.getenv('DB_PASS')
DB = os.getenv('DB')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')
STAFF_ID = os.getenv('STAFF_ID')