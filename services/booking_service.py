"""Сервис бронирований."""
from repositories.booking_repo import BookingRepository


class BookingService:
    """Бизнес-логика бронирований."""

    def __init__(self, repo: BookingRepository) -> None:
        self.repo = repo

    def list_bookings(self) -> list:
        return self.repo.get_all()
