"""Модель номера."""

from dataclasses import dataclass


@dataclass
class Room:
    id: int
    room_number: str
    category: str
    capacity: int
    price_per_night: float
    status: str = "free"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Room) and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
