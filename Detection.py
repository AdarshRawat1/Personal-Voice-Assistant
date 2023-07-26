import os
import speech_recognition as sr
import keyboard 
from Body.cli_design import design_Detection

design_Detection()

def takeCommand():

    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 100
        audio = r.listen(source, 0, 3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        print("Say that again please...")
        return "None"
    return query.lower()

while True:
    wake_up=takeCommand()
    if 'wakeup' in wake_up or 'wake up' in wake_up:
        os.startfile(f'{os.getcwd()}\main.py')
        exit()
    if 'rewoke' in wake_up or 'revoke' in wake_up or 'reebook' in wake_up or 'rebook' in wake_up or 'reebok' in wake_up or 'reboot' in wake_up:
        keyboard.press('space')
        os.startfile(f'{os.getcwd()}\main.py')
        exit()
