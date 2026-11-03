"""Точка входа приложения «Гостиница»."""
from flask import Flask

from config import Config


def create_app(config: type[Config] = Config) -> Flask:
    """Создаёт и настраивает приложение."""
    app = Flask(__name__)
    app.config.from_object(config)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
