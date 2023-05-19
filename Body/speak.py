import pyttsx3  # pip install pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)  # used to change the pace of voice

def speak(audio,voice_id=1):
    engine.setProperty('voice', voices[voice_id].id)
    engine.say(audio)
    engine.runAndWait()