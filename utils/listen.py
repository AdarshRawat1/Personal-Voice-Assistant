import speech_recognition as sr
from googletrans import Translator


#listening function for hindi language
def listen(audio):
    r=sr.Recognizer()
    try :
        print ("Recognising..")
        query= r.recognize_google(audio, language='hi-in')       

    except:
        return "Say Again"
    
    query= str(query).lower()
    return query 

#Translation of query into english
def TranslateHindiToEnglish(text):
    line=str(text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    return data

def Mic(audio):
    query=listen(audio)
    print("translating..")
    data = TranslateHindiToEnglish(query)
    return data
