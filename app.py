"""Точка входа приложения «Гостиница»."""

from flask import Flask

from core.config import Config


def create_app(config: type[Config] = Config) -> Flask:
    """Создаёт и настраивает приложение."""
    app = Flask(__name__)
    app.config.from_object(config)

    # Регистрация blueprints из модулей
    from bookings.routes import bp as bookings_bp
    from guests.routes import bp as guests_bp
    from payments.routes import bp as payments_bp
    from reports.routes import bp as reports_bp
    from rooms.routes import bp as rooms_bp
    from stays.routes import bp as stays_bp

    app.register_blueprint(rooms_bp)
    app.register_blueprint(guests_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(stays_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(reports_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
