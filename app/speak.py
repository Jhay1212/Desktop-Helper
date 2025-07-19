import pyttsx3 as pts

engine = pts.init()

def speak(words: str | list):
    words = words if type(words) == str else " ".join(words) 
    engine.say(words)
    engine.runAndWait()