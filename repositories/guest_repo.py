"""Репозиторий гостей."""
from models.guest import Guest


class GuestRepository:
    """Доступ к гостям в БД."""

    def __init__(self, conn) -> None:
        self.conn = conn

    def get_all(self) -> list[Guest]:
        raise NotImplementedError

    def get_by_id(self, guest_id: int) -> Guest | None:
        raise NotImplementedError

    def add(self, guest: Guest) -> None:
        raise NotImplementedError
