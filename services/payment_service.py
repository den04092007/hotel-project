"""Сервис платежей."""
from repositories.payment_repo import PaymentRepository


class PaymentService:
    """Бизнес-логика платежей."""

    def __init__(self, repo: PaymentRepository) -> None:
        self.repo = repo

    def list_payments(self) -> list:
        return self.repo.get_all()
