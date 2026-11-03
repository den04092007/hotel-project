"""Роуты для гостей."""
from flask import Blueprint, jsonify

bp = Blueprint("guests", __name__, url_prefix="/guests")


@bp.get("/")
def list_guests():
    return jsonify({"guests": []})
