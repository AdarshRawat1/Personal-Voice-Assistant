#make alarm https://www.youtube.com/watch?v=rgGDTO8g2Pg
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import pywhatkit #for google search
import pyautogui #for shortcut
import speedtest
from time import sleep

from Body.listen import Mic
from Body.speak import speak
# from Body.task import task

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


def takeCommand(t = 4):
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 100
        print(f"Listening ... <{lang}>")
        audio = r.listen(source, 0, t)
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
        query=query.lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Searching Wikipedia...")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'bing' in query:
            query= query.replace("bing","")
            query= query.replace("search","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(0)
            pyautogui.press("Enter")

        elif 'google' in query or 'search' in query.lower():
            query=str(query.replace("google",""))
            query=str(query.replace("search",""))
            pywhatkit.search(query)
            
        elif 'how far is' in query:
            query=str(query.replace("google",""))
            query=str(query.replace("search",""))
            pywhatkit.search(f"{query} Graphic Era Hill University")
        
        elif 'on youtube' in query or 'play a video' in query:
            query=query.replace("youtube","")
            query=query.replace("play","")
            web=f"https://www.youtube.com/results?search_query={query}"
            speak("This is what I found on Youtube")
            webbrowser.open(web)
        
        # Youtube Commands
        elif 'pause' in query:
            pyautogui.press('k')
            speak("Video Paused")

        elif 'resume' in query or 'play' in query:
            pyautogui.press('k')
            speak("Video Played")

        elif 'mute video' in query:
            pyautogui.press('m')
            speak("Video Muted")

        elif 'volume up' in query:
            pyautogui.press("up", presses=5)

        elif 'volume down' in query:
            pyautogui.press('down',presses=5)

        #Opening Sites

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'gpt' in query:
            webbrowser.open("chat.openai.com")

        #Browser control 
        elif 'open new tab' in query :
            pyautogui.hotkey("ctrl","t")
        
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl','f4')

        # #Window Control 
        elif 'show task' in query :
            pyautogui.hotkey('win','tab')
        
        elif 'list task' in query:
            pyautogui.hotkey('ctrl','shift','esc')

        elif 'close window' in query :
            pyautogui.hotkey('alt','f4')
 
        elif 'new desktop' in query:
            pyautogui.hotkey('ctrl','win','d')

        elif 'change layout' in query or 'snap layout' in query :
            pyautogui.hotkey('win','z')

     #Functionality 
        elif 'open clipboard' in query or 'open clip board' in query:
            pyautogui.hotkey('win','prtscr')
 
        elif 'internet speed' in query or 'speed test' in query:
            speak("Please wait ! while I calculate upload and download speed")
            wifi= speedtest.Speedtest()
            upload_speed=float(f'{wifi.upload()/(1024*1024):.2f}')   # 1MB = 1024 * 1024 bytes
            download_speed=float(f'{wifi.download()/(1024*1024):.2f}')
            
            print(f"Wifi Download Speed > {download_speed} ")
            print(f"Wifi upload Speed > {upload_speed}")
            speak(f"Wifi Download Speed > {download_speed} MB")
            speak(f"Wifi upload Speed > {upload_speed} MB")

        elif 'take a screenshot' in query or 'capture screenshot' in query or 'take screenshot' in query:
            speak("Sir, tell me the name of this screenshot file")
            name=takeCommand().lower()
            speak("Sir, Please hold the screen . I'll be taking a screenshot")
            img=pyautogui.screenshot()
            img.save(f'ScreenShot/{name}.png')
            speak("I am done sir, Screenshot is saved in ScreenShot folder")


        #Date ,time and day
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            date=datetime.datetime.today()
            speak(date)

        elif 'day' in query :
            day= datetime.datetime.now().strftime("%A")
            speak(f"Sir today it is {day}")

        #Opening Applications 
        elif 'open' in query:
            query= query.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(0.2)
            pyautogui.press("Enter")

        #Sending Whatsapp message 
        elif 'send message' in query:
            query= query.replace("send message to","")
            pyautogui.press("super")
            pyautogui.typewrite("whatsapp")
            sleep(0.2)
            pyautogui.press("Enter")
            sleep(0.2)
            pyautogui.hotkey("ctrl","f")
            pyautogui.typewrite(f"{query}")
            sleep(0.4)
            pyautogui.press("down")

            sleep(0.1)
            pyautogui.press("Enter")
            speak("Sir, What should the message be?")
            msg=takeCommand(10).lower()
            pyautogui.typewrite(msg)
            sleep(0.1)
            pyautogui.press("Enter")
            speak("message sent")

        #Switching Language
        elif 'switch language' in query or 'change language' in query or 'भाषा बदलें' in query:
            if lang == 'en-in':
                lang = 'hi-in'
                speak("अभिवादन, मैं आपकी निजी सहायक, बताइये मैं आपकी क्या मदद कर सकती हूं",Voice_ID_Hindi)
            else:
                lang = 'en-in'
                speak('Using English as mode of communication',Voice_ID_English)

        elif "exit" in query.lower() or "sleep" in query.lower() or "so ja" in query.lower() or 'take a break' in query:
            if lang =='en-in':
                speak('I will be signing off sir , shutting down in 3, 2, 1...... beep',Voice_ID_English)
            else:
                speak('अपना ध्यान रखिए म जा रही हूं। उम्मीद है आप मुझे पुन सेवा का अवसर देंगे',Voice_ID_Hindi)
            exit()


