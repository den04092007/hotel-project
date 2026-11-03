"""Модель проживания."""
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Stay:
    id: int
    guest_id: int
    room_id: int
    check_in_date: date
    check_out_date: Optional[date] = None
    total_amount: Optional[float] = None
    status: str = "active"
