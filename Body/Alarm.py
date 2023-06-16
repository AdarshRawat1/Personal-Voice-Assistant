from utils.speak import speak 

extractedTime=open("DataStore/alarm.txt",'rt')
time=extractedTime.read()
time=str(time)
extractedTime.close()
