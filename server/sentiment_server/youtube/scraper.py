import requests

from server.sentiment_server.common.settings import YOUTUBE_TOKEN


def get_youtube_comments(url: str, max_pages: int = 20) -> list:
    comments = []
    next_page = None
    video_id = get_video_id_from_url(url)
    for i in range(max_pages):
        query_url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={YOUTUBE_TOKEN}" \
                    f"&textFormat=plainText&part=snippet&videoId={video_id}&maxResults=100"
        if next_page:
            query_url += f"&pageToken={next_page}"

        res = requests.get(query_url).json()
        next_page_token = res.get('nextPageToken')
        if next_page_token:
            next_page = next_page_token
        else:
            comments.extend(unpack_comments(res))
            return comments

        comments.extend(unpack_comments(res))

    return comments


def get_video_id_from_url(url: str) -> str:
    return url.split("watch?v=")[1]


def unpack_comments(raw_res) -> list:
    return [item['snippet']['topLevelComment']['snippet']['textOriginal'] for item in raw_res.get('items')]
