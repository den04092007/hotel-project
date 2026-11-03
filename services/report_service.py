"""Сервис отчётов."""
from repositories.booking_repo import BookingRepository
from repositories.stay_repo import StayRepository


class ReportService:
    """Формирование отчётов."""

    def __init__(self, booking_repo: BookingRepository,
                 stay_repo: StayRepository) -> None:
        self.booking_repo = booking_repo
        self.stay_repo = stay_repo

    def occupancy_report(self) -> dict:
        raise NotImplementedError
