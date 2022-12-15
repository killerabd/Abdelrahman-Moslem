import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import pywhatkit 
from news import *
#import pyttsx3
from time import ctime 
from gtts import gTTS
import datetime


r = sr.Recognizer()
print(ctime())
def record_audio(ask = False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        if ask:
            Ga3far_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-us")
        except sr.UnknownValueError:
            Ga3far_speak('Sorry, I did not get that')
        except sr.RequestError:
            Ga3far_speak('sorry my service is down right now')
        return voice_data

def Ga3far_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def wishMe():
    hour = int(datetime.datetime.now().hour) #get The Time Now 
    if hour>= 0 and hour<12:
        Ga3far_speak("Good Morning Abdelrahman !")
  
    elif hour>= 12 and hour<18:
        Ga3far_speak("Good Afternoon Abdelrahman !")  
  
    else:
        Ga3far_speak("Good Evening Abdelrahman !") 
xxx=wishMe()
  


def respond(voice_data):
    if 'what is your name' in voice_data:
        Ga3far_speak('My name is rio')
        
    if 'what is the date and time' in voice_data:
        
        Ga3far_speak(time.ctime())
        #current_time = time.strftime("%H:%M:%S")
        #Ga3far_speak('The time is ' + current_time )
        
        
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Ga3far_speak('here is what I found for ' + search)
        
    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Ga3far_speak('here is the location of ' + location)
        
    if 'open download' in voice_data:
        os.startfile("C:/Users/ali/Downloads")
        
    if 'YouTube' in voice_data:
        x = record_audio('what do you want to search  in youtube')
        url = 'https://www.youtube.com/results?search_query=' + x
        webbrowser.get().open(url)
        
        
    if 'news' in voice_data:
        
        arr=news()
        for i in range(len(arr)):
            Ga3far_speak(arr[i])
         #   print(arr[i])
    
        
    
  
    if 'you can go to sleep now' in voice_data:
        Ga3far_speak('bye bye')
        exit()

time.sleep(1)
while 1:  
    Ga3far_speak('How can I help you?')
    voice_data = record_audio()
    respond(voice_data)