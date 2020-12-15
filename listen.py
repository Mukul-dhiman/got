import pyttsx3
# from pyttsx3.drivers import sapi5
engine = pyttsx3.init() 
# voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voices', voice_id) #1 for man 0 for girl

""" RATE"""
rate = engine.getProperty('rate')  
engine.setProperty('rate', 100)    


"""VOLUME"""
volume = engine.getProperty('volume')                           
engine.setProperty('volume',2.0)   

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import os
import sys

file_line = int(sys.argv[2])
path = os.getcwd()

file = "game_of_thrones/c"+str(sys.argv[1])+".txt"
print("reading: ",file)
with open(os.path.join(path, file), "r") as fp:
    cur = 0
    for line in fp:
        cur+=1
        print(cur)
        if(cur>=file_line):
            print(line)
            speak(line)