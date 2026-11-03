"""Роуты для проживаний."""

from flask import Blueprint, jsonify

bp = Blueprint("stays", __name__, url_prefix="/stays")


@bp.get("/")
def list_stays():
    return jsonify({"stays": []})
