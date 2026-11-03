"""Репозиторий номеров."""

from models.room import Room


class RoomRepository:
    """Доступ к номерам в БД."""

    def __init__(self, conn) -> None:
        self.conn = conn

    def get_all(self) -> list[Room]:
        raise NotImplementedError

    def get_by_id(self, room_id: int) -> Room | None:
        raise NotImplementedError

    def add(self, room: Room) -> None:
        raise NotImplementedError
