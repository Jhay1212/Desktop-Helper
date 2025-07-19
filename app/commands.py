
import ctypes
import os 
import sys
from pydub import AudioSegment
from pydub.playback import play
import pygame as pg
import pathlib 
import ctypes
from random import choice

pg.init()
pg.mixer.init()

ALLOWERD_FILE_EXTENSIONS = {
    "music": (".mp3", ".wav", ".flac", ".aac"), 
    "wallpaper": (".jpeg", ".jpg", ".png")
}

root = os.path.abspath(os.sep)
root = os.path.join(root, "Users", "rjhay")
MUSIC_PATH = pathlib.Path(os.path.join(root, "Music"))
WALLPAPER_PATH = pathlib.Path(os.path.join(root, "OneDrive", "Pictures", 'wallpapers'))
print(WALLPAPER_PATH)


def all_items(path, pattern):
    """Get all files or sub directory in a path then return the files only acceptable in pattern"""
    items = path.rglob("*")
    print(items)
    valid_files = []
    for item in items:
        if item.is_file() and item.suffix in ALLOWERD_FILE_EXTENSIONS[pattern.lower()]:
            valid_files.append(str(item))
    return valid_files

MUSICS = all_items(MUSIC_PATH, "music")
WALLPAPERS = all_items(WALLPAPER_PATH, "wallpaper")

print(WALLPAPERS)
def change_wallpaper(wallpaper=None):
    wallpaper = wallpaper if wallpaper else choice(WALLPAPERS)
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        wallpaper,
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )

def play_music():
    # plays music from music folder 
    pg.mixer.music.load(choice(MUSICS))
    pg.mixer.music.play()   

    while pg.mixer.music.get_busy():
        pg.time.Clock().tick(10)

def set_an_alarm():
    pass

def ask_question():
    pass

change_wallpaper()