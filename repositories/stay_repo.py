"""Репозиторий проживаний."""
from models.stay import Stay


class StayRepository:
    """Доступ к проживаниям в БД."""

    def __init__(self, conn) -> None:
        self.conn = conn

    def get_all(self) -> list[Stay]:
        raise NotImplementedError

    def get_by_id(self, stay_id: int) -> Stay | None:
        raise NotImplementedError

    def add(self, stay: Stay) -> None:
        raise NotImplementedError
