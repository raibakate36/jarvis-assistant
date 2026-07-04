import pyttsx3
from threading import Thread

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def reply(text):
    Thread(target=speak, args=(text,), daemon=True).start()
    return text