"""Модель гостя."""
from dataclasses import dataclass
from datetime import date


@dataclass
class Guest:
    id: int
    full_name: str
    phone: str
    email: str
    passport_data: str
    birth_date: date
