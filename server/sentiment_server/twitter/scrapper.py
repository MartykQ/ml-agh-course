from typing import List

import requests

from server.sentiment_server.common.settings import TWITTER_BEARER_TOKEN


def get_user_id_from_name(username: str) -> str:
    url = f"https://api.twitter.com/2/users/by/username/{parse_username(username)}"
    headers = {'Authorization': f'Bearer {TWITTER_BEARER_TOKEN}'}

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return response.json()['data']['id']


def parse_username(username: str) -> str:
    return username.replace(" ", "")


def get_last_tweets_of_user(user_id: str) -> List[dict]:
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = {'Authorization': f'Bearer {TWITTER_BEARER_TOKEN}'}

    response = requests.request("GET", url, headers=headers)

    return response.json()['data']


def get_replies_to_tweet(tweet_id: str) -> List[dict]:
    url = f"https://api.twitter.com/2/tweets/search/recent?query=conversation_id:{tweet_id}&max_results=100"
    headers = {'Authorization': f'Bearer {TWITTER_BEARER_TOKEN}'}
    response = requests.request("GET", url, headers=headers)

    try:
        potential_response = response.json()['data']
        return potential_response
    except KeyError as err:
        raise EmptyTwitterReplies


def get_username_from_url(url: str) -> str:
    return url.split("twitter.com/")[1]


def get_last_replies_from_url(url: str) -> List[str]:
    username = get_username_from_url(url)
    uid = get_user_id_from_name(username)

    tweets = get_last_tweets_of_user(user_id=uid)

    for tweet in tweets:
        try:
            replies = get_replies_to_tweet(tweet['id'])
            return [r['text'].replace(f"@{username}", "") for r in replies]
        except EmptyTwitterReplies:
            pass

    return []


class EmptyTwitterReplies(Exception):
    pass
