"""Подключение к БД."""
import sqlite3
from contextlib import contextmanager


@contextmanager
def get_connection(db_path: str = "hotel.db"):
    """Контекстный менеджер для соединения с SQLite."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
