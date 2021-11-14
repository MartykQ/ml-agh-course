from flask import Blueprint, jsonify, request

from model.predict import predict
from server.sentiment_server.ibm_watson.predicotr import translate_and_perdict
from server.sentiment_server.twitter.scrapper import get_last_replies_from_url
from server.sentiment_server.youtube.scraper import get_youtube_comments

api_routes = Blueprint('api_routes', __name__)


@api_routes.route("/single", methods=['POST'])
def single():
    data = request.json
    text = data['text']
    return jsonify({
        "text": text,
        "label": predict(text)
    })


@api_routes.route("/ibm_single", methods=['POST'])
def ibm_single():
    data = request.json
    text = data['text']
    return jsonify({
        "text": text,
        "label": translate_and_perdict([text])[0]['label']
    })


@api_routes.route("/youtube_comments", methods=['POST'])
def get_yt_comments():
    data = request.json
    yt_url = data['url']

    predicted_data = []
    comments = get_youtube_comments(yt_url)[:100]
    for comment in comments:
        predicted_data.append({"text": comment, "label": predict(comment)})

    return jsonify(predicted_data)


@api_routes.route("/tweets", methods=['POST'])
def get_tweets():
    data = request.json
    tw_url = data['url']

    predicted_data = []
    tw_replies = get_last_replies_from_url(tw_url)[:100]
    for reply in tw_replies:
        predicted_data.append({"text": reply, "label": predict(reply)})

    return jsonify(predicted_data)


@api_routes.route("/ibm_youtube_comments", methods=['POST'])
def ibm_get_yt_comments():
    data = request.json
    yt_url = data['url']
    comments = get_youtube_comments(yt_url)[:15]
    return jsonify(translate_and_perdict(comments))


@api_routes.route("/ibm_tweets", methods=['POST'])
def ibm_get_tweets():
    data = request.json
    tw_url = data['url']
    tw_replies = get_last_replies_from_url(tw_url)[:15]
    return jsonify(translate_and_perdict(tw_replies))
