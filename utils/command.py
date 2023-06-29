import speech_recognition as sr  # pip install speechRecognition
from utils.listen import Mic
import Controls.control as ctr

def takeCommand(t = 5):
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 100
        print(f"Listening ... <{ctr.lang}>")
        audio = r.listen(source, 0, t)
    try:
        if ctr.lang=='hi-in':
            query=Mic(audio)
        else:
            print("Recognising..")
            query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        return "None"
    return query.lower()
