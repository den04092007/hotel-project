"""Сервис номеров."""
from repositories.room_repo import RoomRepository


class RoomService:
    """Бизнес-логика номеров."""

    def __init__(self, repo: RoomRepository) -> None:
        self.repo = repo

    def list_rooms(self) -> list:
        return self.repo.get_all()
