import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_PATH = "database.db"
    OWNER_EMAIL = os.getenv("OWNER_EMAIL")
    APP_PASSWORD = os.getenv("APP_PASSWORD")
    BASE_URL = os.getenv("BASE_URL")