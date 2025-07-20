import speech_recognition as sr
import os
import time
from .speak import speak
import spacy

nlp = spacy.load("en_core_web_sm")
def detect_sentence(sentences):
    about_sentence = nlp(sentences)
    sentence = list(about_sentence.sents)
    
r = sr.Recognizer()
m = sr.Microphone.list_microphone_names()[4] # Speakers (Realtek(R) Audio) is the 4 mictophone
text = ""
with sr.Microphone() as source:
   
    print("Say Something:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        speak(text)  # 
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; check your internet connection. Error: {e}")