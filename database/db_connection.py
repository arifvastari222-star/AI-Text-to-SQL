import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

BASE_DIR = Path(__file__).resolve().parent.parent

env_path = BASE_DIR / ".env"

print("Looking for .env at:")
print(env_path)

load_dotenv(env_path)

print("HOST =", os.getenv("DB_HOST"))
print("DB =", os.getenv("DB_NAME"))
print("USER =", os.getenv("DB_USER"))
print("PASSWORD LENGTH =", len(os.getenv("DB_PASSWORD")))

def get_connection():

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return conn