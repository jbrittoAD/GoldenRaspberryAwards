from flask import Blueprint, jsonify
from models import db, Movie
from services.user_service import get_producers_with_intervals

main_bp = Blueprint('main', __name__)

@main_bp.route('/producers', methods=['GET'])
def max_interval():
    result = get_producers_with_intervals(db.session)
    return jsonify(result)

