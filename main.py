import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
from time import ctime
import time
import wikipedia
import webbrowser
import os
import random
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class person:
    name = ''
    def setName(self, name):
        self.name = name

person_obj = person()

def there_exists(terms):
    query = takeCommand()
    for term in terms:
        if term in query:
            return True

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        speak("Unable to recognise your voice")
        return None

    return (query)

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour< 12:
        print("Good Morning")
        speak("Good Morning")
    elif hour>=12 and hour< 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")

asname = ("Mihir")

def username():
    print("Can I know your name?")
    speak("Can I know your name")
    name = takeCommand()
    print(f"Welcome {name}")
    speak(f"Welcome {name}")

    print(f"I am {asname}, your virtual assistant")
    speak(f"I am {asname}, your virtual assistant")
    print("How can I help you?")
    speak("How can I help you?")


if __name__ == '__main__':
    clear = os.system('cls')

    # This Function will clean any
    # command before execution of this python file

    clear
    greet()
    username()

    def respond():

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        #Greeting
        if there_exists(["hi","hey","hello"]):
            greeting = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
            fgreet = greeting[random.randint(0,len(greeting)-1)]
            speak(fgreet)

        #Name
        if there_exists(["what is your name","what's your name","tell me your name"]):
            speak(f"I'm a virtual assistant and My name is {asname}")

        #Greeting - 2
        if there_exists(["how are you", "how are you doing"]):
            speak(f"I'm very well, thanks for asking {person_obj.name}")

        #Greeting - 3
        if there_exists(['how are you','how do you do','wassup']):
            greet_2 = [f"I'm doing good, how about you? {person_obj.name}", f"everything fine, how about you? {person_obj.name}"]
            fgreet_2 = greet_2[random.randint(0,len(greet_2)-1)]
            speak(fgreet_2)

        #Time
        if there_exists(["what's the time", "tell me the time", "what time is it"]):
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = f'{hours} {minutes}'
            speak(time)

        #Wikipedia
        if there_exists(['Search for']):
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #Google
        if there_exists(["search google for"]) and 'youtube' not in query:
            search_term = query.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')

        #Youtube
        if there_exists(["youtube"]):
            search_term = query.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')

        #Joke
        if there_exists(["tell me joke","say a joke","tell one joke"]):
            speak(pyjokes.get_joke())

        #news
        if there_exists(["say News", "read news"]):
            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        #take note
        if there_exists("take a note", "note this"):
            speak("What should i write?")
            note = takeCommand()
            file = open('assistant.txt', 'w')
            speak("Should i include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        #show note
        if there_exists(['show me note',"show the note"]):
            speak("showing you the note")
            file = open("assistant.txt","r")
            print(file.read())
            speak(file.read(6))

        #calculate
        if there_exists(["calculate","add"]):
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        #expert-level queries
        if there_exists(["what is?","who is"]):
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        #Exit
        if there_exists(["exit", "quit", "goodbye"]):
            speak("going offline")
            exit()


time.sleep(1.0)

while(1.0):
    query = takeCommand()
    respond(query)



