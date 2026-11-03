"""Тесты для бизнес-правил гостиницы."""

from datetime import date, timedelta

import pytest

from business_rules import (
    Booking,
    br_01_no_overlap,
    br_03_total_cost,
    br_04_cancellation_fee,
    br_05_adult_required,
)


def test_br_01_no_overlap_returns_true_when_no_overlap():
    today = date(2026, 11, 2)
    existing = [Booking(1, 101, today, today + timedelta(days=2), 30)]
    assert (
        br_01_no_overlap(
            101, today + timedelta(days=2), today + timedelta(days=4), existing
        )
        is True
    )


def test_br_01_no_overlap_returns_false_when_overlap():
    today = date(2026, 11, 2)
    existing = [Booking(1, 101, today, today + timedelta(days=3), 30)]
    assert (
        br_01_no_overlap(
            101, today + timedelta(days=1), today + timedelta(days=4), existing
        )
        is False
    )


def test_br_03_total_cost():
    assert br_03_total_cost(3, 2500.0, 500.0) == 8000.0


def test_br_03_total_cost_negative_nights_raises():
    with pytest.raises(ValueError):
        br_03_total_cost(-1, 2500.0)


def test_br_04_cancellation_fee_less_than_24h():
    today = date(2026, 11, 2)
    fee = br_04_cancellation_fee(today + timedelta(hours=12), today, 2500.0)
    assert fee == 1250.0


def test_br_04_cancellation_fee_more_than_24h():
    today = date(2026, 11, 2)
    fee = br_04_cancellation_fee(today + timedelta(days=2), today, 2500.0)
    assert fee == 0.0


def test_br_05_adult_required_minor_without_adult():
    assert br_05_adult_required(16, accompanied_by_adult=False) is False


def test_br_05_adult_required_minor_with_adult():
    assert br_05_adult_required(16, accompanied_by_adult=True) is True


def test_br_05_adult_required_adult():
    assert br_05_adult_required(25, accompanied_by_adult=False) is True
