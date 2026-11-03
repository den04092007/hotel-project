"""Модель дополнительной услуги."""

from dataclasses import dataclass


@dataclass
class AdditionalService:
    id: int
    name: str
    price: float
