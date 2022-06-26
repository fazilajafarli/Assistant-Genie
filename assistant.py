import pyttsx3
import speech_recognition as sr
import requests
import datetime
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistant listening...")
        audio=r.listen(source)
        try:    
            query = r.recognize_google(audio)
            return query
        except:
            print("Please, say again")

