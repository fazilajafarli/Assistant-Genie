import pyttsx3
import speech_recognition as sr
import requests
import datetime
import os
import wikipedia
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wikipedia.set_lang("en")

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jinn listening...")
        audio=r.listen(source)
        try:    
            query = r.recognize_google(audio)
            return query
        except:
            print("Didn't hear well, say again")

while True:
    query = command().lower()
    if 'name' in query:
        speak("Hello! My name is Jinn, and what is your name?")
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M')
        speak(f"It's {time}")
    elif 'who is' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    elif 'what is' in query:
        query = query.replace('what is',"")
        speak(wikipedia.summary(query,2))
    elif "bye" in query:
        speak("Have a nice day! ")
        break
    else:
        speak("I don't understand what you are saying")