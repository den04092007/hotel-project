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
