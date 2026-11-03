"""Репозиторий бронирований."""

from models.booking import Booking


class BookingRepository:
    """Доступ к бронированиям в БД."""

    def __init__(self, conn) -> None:
        self.conn = conn

    def get_all(self) -> list[Booking]:
        raise NotImplementedError

    def get_by_id(self, booking_id: int) -> Booking | None:
        raise NotImplementedError

    def add(self, booking: Booking) -> None:
        raise NotImplementedError
