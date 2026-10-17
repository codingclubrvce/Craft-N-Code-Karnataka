import os
from pathlib import Path

# Base directories
BACKEND_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BACKEND_DIR / "app"
TEMPLATES_DIR = BACKEND_DIR / "templates"
FIXTURES_DIR = BACKEND_DIR / "fixtures"

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BACKEND_DIR / 'storymath.db'}")
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://127.0.0.1:3000,*"
    ).split(",")
    if origin.strip()
]

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
