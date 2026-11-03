"""Репозиторий платежей."""
from models.payment import Payment


class PaymentRepository:
    """Доступ к платежам в БД."""

    def __init__(self, conn) -> None:
        self.conn = conn

    def get_all(self) -> list[Payment]:
        raise NotImplementedError

    def add(self, payment: Payment) -> None:
        raise NotImplementedError
