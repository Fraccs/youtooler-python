from pytest import raises
from youtooler import utils
from youtooler import exceptions

def test_get_secure_password() -> None:
    assert len(utils.get_secure_password(20)) == 20

def test_get_secure_password() -> None:
    with raises(exceptions.UnsecureLength):
        utils.get_secure_password(10)

def test_get_video_duration() -> None:
    videos = {
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ': 213,
        'https://www.youtube.com/watch?v=iik25wqIuFo': 8,
        'https://www.youtube.com/watch?v=rTgj1HxmUbg': 3644
    }

    for video in videos:
        assert utils.get_video_duration(video) == videos.get(video)

def test_get_video_duration() -> None:
    with raises(exceptions.DurationUnestablishedException):
        utils.get_video_duration('https://github.com/Fraccs/youtooler-python')

def test_get_video_title() -> None:
    videos = {
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ': 'Rick Astley - Never Gonna Give You Up (Official Music Video)',
        'https://www.youtube.com/watch?v=iik25wqIuFo': 'Rick roll, but with different link',
        'https://www.youtube.com/watch?v=rTgj1HxmUbg': 'Rick Astley Never gonna give you up 1 hour seamless loop'
    }

    for video in videos:
        assert utils.get_video_title(video) == videos.get(video)

def test_verify_youtube_url() -> None:
    videos = {
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ': True,
        'https://www.youtube.com/watch?v=notreal': False,
        'https://www.youtube.com/watch?v=rTgj1HxmUbg&t=10': False
    }

    for video in videos:
        assert utils.verify_youtube_url(video) == videos.get(video)
