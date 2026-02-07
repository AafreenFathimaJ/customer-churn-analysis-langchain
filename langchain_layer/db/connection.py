import sqlite3
from pathlib import Path

BASE_DIR = Path(_file_).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "data" / "processed" / "enterprise_intelligence.db"


def get_connection():
    return sqlite3.connect(DB_PATH)