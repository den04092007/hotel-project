"""Роуты для номеров."""
from flask import Blueprint, jsonify

bp = Blueprint("rooms", __name__, url_prefix="/rooms")


@bp.get("/")
def list_rooms():
    return jsonify({"rooms": []})
