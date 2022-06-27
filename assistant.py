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
        print("Genie listening...")
        audio=r.listen(source)
        try:    
            query = r.recognize_google(audio)
            return query
        except:
            print("I didn't hear you well, master.")

while True:
    query = command().lower()
    if 'name' in query:
        speak("Hello! My name is Genie, master!")
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M')
        speak(f"It's {time}")
    elif 'who is' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    elif 'what is' in query:
        query = query.replace('what is',"")
        speak(wikipedia.summary(query,2))
    elif 'news' in query:
            def trendnews(): 
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                page = requests.get(url).json() 
                article = page["articles"] 
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                for i in range(len(results)): 
                    print(i + 1, results[i]) 
                speak("Here are the top trending news...")
                speak("Do yo want me to read?")
                reply = command().lower()
                reply = str(reply)
                if reply == "yes":
                    speak(results)
                else:
                    speak('ok!')
                    pass
            trendnews() 



    elif "bye" in query:
        speak("Bye-bye master!")
        break
    else:
        speak("I don't understand what you are saying, master.")