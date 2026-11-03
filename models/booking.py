"""Модель бронирования."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Booking:
    id: int
    guest_id: int
    room_id: int
    check_in_date: date
    check_out_date: date
    status: str = "active"
