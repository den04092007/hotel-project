"""Сервис расчёта стоимости."""

from business_rules import br_03_total_cost


class PricingService:
    """Расчёт стоимости проживания."""

    def calculate(
        self, nights: int, price_per_night: float, services_cost: float = 0.0
    ) -> float:
        return br_03_total_cost(nights, price_per_night, services_cost)
