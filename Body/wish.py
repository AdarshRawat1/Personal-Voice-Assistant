import datetime
from utils.speak import speak
from Controls.control import Voice_ID_English
from Controls.control import Voice_ID_Hindi 

def wishMe(lang):
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
