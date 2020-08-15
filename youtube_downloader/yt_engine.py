#  Copyright (c) Andrada Preda

from youtube_downloader.extras import *
import youtube_dl
import os


def get_videos_for_links(links_to_download):
    youtube_dl.YoutubeDL(ydl_opts_video).download(links_to_download)


def get_music_for_links(links_to_download):
    youtube_dl.YoutubeDL(ydl_opts_audio).download(links_to_download)


def get_audiobooks_for_links(links_to_download):
    youtube_dl.YoutubeDL(ydl_opts_audio).download(links_to_download)


def get_links():
    links = []
    print("Insert your youtube links, separated by ENTER. Type DONE when finished.")
    link = input("Insert a youtube link here: ")
    while link != "DONE" and link != "":
        links.append(link)
        link = input("Insert a youtube link here:")
    return links


def choose_default_directory(choice):
    if choice == 1:
        os.chdir(DEFAULT_VIDEOS)
    elif choice == 2:
        os.chdir(DEFAULT_MUSIC)
    elif choice == 3:
        os.chdir(DEFAULT_AUDIOBOOKS)
    else:
        pass


def pick_directory(choice):
    path = input("Where would you like to save your downloads? ")
    if path != "":
        if os.path.exists(path) is False:
            os.mkdir(path)
        os.chdir(path)
    else:
        choose_default_directory(choice)


def get_videos():
    links_to_download = get_links()
    pick_directory(1)
    get_videos_for_links(links_to_download)


def get_music():
    links_to_download = get_links()
    pick_directory(2)
    get_music_for_links(links_to_download)


def get_audiobooks():
    links_to_download = get_links()
    pick_directory(3)
    get_audiobooks_for_links(links_to_download)


if __name__ == '__main__':
    print("What would you like to download today? Please choose between the following:")

    for i in CHOICES:
        print("{0}. {1}".format(str(CHOICES.index(i) + 1), i))
    action = input()

    if action == "videos" or action == '1':
        get_videos()
    elif action == "music" or action == '2':
        get_music()
    elif action == "audiobooks" or action == '3':
        get_audiobooks()
    elif action == "nothing" or action == '4':
        pass

    print("Done! Have a great day!")
