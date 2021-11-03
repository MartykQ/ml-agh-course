from flask import Blueprint, jsonify, request
from server.sentiment_server.youtube.scraper import get_youtube_comments
api_routes = Blueprint('api_routes', __name__)


@api_routes.route("/youtube_comments", methods=['POST'])
def get_yt_comments():
    data = request.json
    yt_url = data['url']
    return jsonify(get_youtube_comments(yt_url))
