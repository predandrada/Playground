#  Copyright (c) Andrada Preda

from youtube_downloader.logger import MyLogger

DEFAULT_VIDEOS = ""
DEFAULT_MUSIC = ""
DEFAULT_AUDIOBOOKS = ""


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts_video = {}


ydl_opts_audio = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

CHOICES = [
    "videos",
    "music",
    "audiobooks",
    "nothing"
]
