import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os

from Body.listen import Mic
from Body.speak import speak

Voice_ID_English=int(3)
Voice_ID_Hindi=int(1)

def wishMe():
    if (lang == 'en-in'):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning! Sir",Voice_ID_English)

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon! Sir",Voice_ID_English)

        else:
            speak("Good Evening! Sir",Voice_ID_English)
        speak("I am P27 Your personal Assistant. Please tell me how may I help you",Voice_ID_English)
    else:
        speak("अभिवादन, मैं आपकी निजी सहायक, बताइये मैं आपकी क्या मदद कर सकती हूं",Voice_ID_Hindi)


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 100
        print(f"Listening ... <{lang}>")
        audio = r.listen(source, 0, 4)
    try:
        if lang=='hi-in':
            query=Mic(audio)
        else:
            print("Recognising..")
            query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        return "None"
    return query.lower()


if __name__ == "__main__":
    lang = 'en-in'
    wishMe()
    while True:
        # if 1:
        query = takeCommand()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Searching Wikipedia...")
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'take a break' in query:
            speak("ok sir , you can call me anytime")
            speak("Just say Alfa to get my assistent")
            break

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'gpt' in query:
            webbrowser.open("chat.openai.com")

        elif 'play music' in query:
            music_dir = '"C:\\Users\\Alfa\\Music"'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "A:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open dev c' in query:
            codePath = "A:\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)

        elif 'switch language' in query or 'change language' in query or 'भाषा बदलें' in query:
            if lang == 'en-in':
                lang = 'hi-in'
                speak("अभिवादन, मैं आपकी निजी सहायक, बताइये मैं आपकी क्या मदद कर सकती हूं",Voice_ID_Hindi)
            else:
                lang = 'en-in'
                speak('Using English as mode of communication',Voice_ID_English)

        elif "exit" in query.lower() or "sleep" in query.lower() or "so ja" in query.lower():
            if lang =='en-in':
                speak('I will be signing off sir , shutting down in 3, 2, 1...... beep',Voice_ID_English)
            else:
                speak('अपना ध्यान रखिए म जा रही हूं। उम्मीद है आप मुझे पुन सेवा का अवसर देंगे',Voice_ID_Hindi)
            exit()

