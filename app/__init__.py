import os, pathlib
import vosk
import pyttsx3 as pyt
from .speak import speak
speak("Hello, I Am Vosk. Your AI Assistant. How can I Help you.")


BASEDIR  = pathlib.Path(__file__).parent
