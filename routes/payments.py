"""Роуты для платежей."""

from flask import Blueprint, jsonify

bp = Blueprint("payments", __name__, url_prefix="/payments")


@bp.get("/")
def list_payments():
    return jsonify({"payments": []})
