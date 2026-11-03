"""Модель платежа."""
from dataclasses import dataclass
from datetime import date


@dataclass
class Payment:
    id: int
    stay_id: int
    amount: float
    payment_date: date
    method: str
    status: str = "pending"
