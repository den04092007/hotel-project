"""Роуты для отчётов."""
from flask import Blueprint, jsonify

bp = Blueprint("reports", __name__, url_prefix="/reports")


@bp.get("/")
def list_reports():
    return jsonify({"reports": []})
