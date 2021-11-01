from flask import Blueprint, jsonify

status_routes = Blueprint('status_routes', __name__)


@status_routes.route('/status', methods=['GET'])
def status_route():
    return jsonify({
        'msg': 'Hello world!'
    }), 200
