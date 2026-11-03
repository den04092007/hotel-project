"""Бизнес-правила предметной области «Гостиница» (вариант 5)."""

from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Booking:
    guest_id: int
    room_id: int
    check_in: date
    check_out: date
    guest_age: int


def br_01_no_overlap(
    room_id: int, check_in: date, check_out: date, existing_bookings: List[Booking]
) -> bool:
    """BR-01: нет пересечения броней."""
    for b in existing_bookings:
        if b.room_id != room_id:
            continue
        if check_in < b.check_out and check_out > b.check_in:
            return False
    return True


def br_03_total_cost(
    nights: int, price_per_night: float, services_cost: float = 0.0
) -> float:
    """BR-03: стоимость = суток × тариф + услуги."""
    if nights < 0:
        raise ValueError("nights must be >= 0")
    if price_per_night < 0:
        raise ValueError("price_per_night must be >= 0")
    return round(nights * price_per_night + services_cost, 2)


def br_04_cancellation_fee(
    check_in: date, cancel_date: date, price_per_night: float
) -> float:
    """BR-04: штраф 50% при отмене < 24 ч."""
    hours_before = (check_in - cancel_date).total_seconds() / 3600
    if hours_before < 24:
        return round(price_per_night * 0.5, 2)
    return 0.0


def br_05_adult_required(guest_age: int, accompanied_by_adult: bool) -> bool:
    """BR-05: несовершеннолетний без взрослого — отказ."""
    return not (guest_age < 18 and not accompanied_by_adult)
