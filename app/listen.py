import speech_recognition as sr
import os
import time
from .speak import speak
r = sr.Recognizer()
m = sr.Microphone.list_microphone_names()[4] # Speakers (Realtek(R) Audio) is the 4 mictophone

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source, phrase_time_limit=3)

    q = input("Press q to stop").lower()
    speak(audio)


try:
    print("You said " + r.recognize_vosk(audio))
except sr.UnknownValueError:
    print("Unknown Value Error")
except sr.RequestError as e:
    print("Vosk Error {}".format(e))

