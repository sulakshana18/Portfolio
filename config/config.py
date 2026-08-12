import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "portfolio.db"
SECRET_KEY = os.environ.get("SECRET_KEY", "sulakshana-portfolio-secret-key")
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
