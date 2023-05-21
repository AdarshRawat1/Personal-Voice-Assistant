import speech_recognition as sr
from googletrans import Translator


#listening function for hindi language
def listen(audio):
    r=sr.Recognizer()
    # with sr.Microphone() as source :
    #     print("listening...<hi-in>")
    #     r.pause_threshold=0.9
    #     r.energy_threshold=100
    #     audio= r.listen(source,0,4)

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
    print(f'you said : {data}.')
    return data

def Mic(audio):
    query=listen(audio)
    data = TranslateHindiToEnglish(query)
    return data


    

