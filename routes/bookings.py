"""Роуты для бронирований."""
from flask import Blueprint, jsonify

bp = Blueprint("bookings", __name__, url_prefix="/bookings")


@bp.get("/")
def list_bookings():
    return jsonify({"bookings": []})
