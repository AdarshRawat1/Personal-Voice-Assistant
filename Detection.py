import os
import speech_recognition as sr

def takeCommand():

    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        r.energy_threshold = 100
        audio = r.listen(source, 0, 3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        print("Say that again please...")
        return "None"
    return query

while True:
    wake_up=takeCommand()
    if 'wakeup' in wake_up or 'wake up' in wake_up:
        os.startfile(f'{os.getcwd()}\main.py')
    else :
        print('nothing...')
