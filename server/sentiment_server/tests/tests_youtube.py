from server.sentiment_server.youtube.scraper import get_video_id_from_url, get_youtube_comments


def test_get_youtube_comments():
    coms = get_youtube_comments("https://www.youtube.com/watch?v=cqdVBhPp_xk")
    assert len(coms) > 0


def test_get_id_from_url():
    assert get_video_id_from_url("https://www.youtube.com/watch?v=Rv8m8lZtsxM") == "Rv8m8lZtsxM"
