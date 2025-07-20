import pygame as pg
from dotenv import dotenv_values

from random import choice
import ctypes
import pathlib 
import os 
import google.generativeai as genai


config = dotenv_values(".env")
API_KEY=config['GEMINI_SECRETKEY']
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
models = genai.list_models()

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


def all_items(path, pattern):
    """Get all files or sub directory in a path then return the files only acceptable in pattern"""
    items = path.rglob("*")
    valid_files = []
    for item in items:
        if item.is_file() and item.suffix in ALLOWERD_FILE_EXTENSIONS[pattern.lower()]:
            valid_files.append(str(item))
    return valid_files

MUSICS = all_items(MUSIC_PATH, "music")
WALLPAPERS = all_items(WALLPAPER_PATH, "wallpaper")

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
    """"" 
    Plays music and let it play for the duration of the muisc used for 
    """
    pg.mixer.music.load(choice(MUSICS))
    pg.mixer.music.play()   

    while pg.mixer.music.get_busy():
        pg.time.Clock().tick(10)

def set_an_alarm():
    pass

def ask_question(question):
    chat = model.start_chat()
    response = model.generate_content(question)
    return response.text

def open_app(app):
    pass