"""Сервис заселения/выселения."""

from repositories.stay_repo import StayRepository


class StayService:
    """Бизнес-логика проживаний."""

    def __init__(self, repo: StayRepository) -> None:
        self.repo = repo

    def list_stays(self) -> list:
        return self.repo.get_all()
