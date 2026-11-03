"""Конфигурация приложения."""

import os


class Config:
    """Базовая конфигурация."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///hotel.db")
    TESTING = False
