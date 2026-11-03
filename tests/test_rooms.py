"""Тесты для модуля rooms."""
from models.room import Room


def test_room_creation():
    room = Room(1, "101", "standard", 2, 2500.0)
    assert room.id == 1
    assert room.room_number == "101"
    assert room.status == "free"
