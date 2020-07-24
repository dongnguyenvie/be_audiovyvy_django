import os

post = {
    'TYPE_OPTIONS': [
        (1, 'post'),
        (2, 'video'),
        (3, 'audio'),
        (4, 'image'),
        (5, 'other')
    ]
}

menu = {
    'TYPE_OPTIONS': [
        (1, 'header'),
        (2, 'sidebar-default'),
        (3, 'footer'),
        (4, 'main-nav'),
        (5, 'detail')
    ]
}

CACHE_TIME_TTL = os.getenv("CACHE_TIME_TTL") or 60 * 60

TOP_WATCHING_STORY_KEY = "TOP_WATCHING_STORY_KEY"

WS_POPULAR_AUDIO_GROUP = "WS_POPULAR_AUDIO_GROUP"