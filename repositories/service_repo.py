"""Репозиторий дополнительных услуг."""
from models.additional_service import AdditionalService


class ServiceRepository:
    """Доступ к дополнительным услугам в БД."""

    def __init__(self, conn) -> None:
        self.conn = conn

    def get_all(self) -> list[AdditionalService]:
        raise NotImplementedError

    def add(self, service: AdditionalService) -> None:
        raise NotImplementedError
