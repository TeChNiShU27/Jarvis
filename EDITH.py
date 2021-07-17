import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests as req
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

webbrowser.register('edge',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am Edith sir. Please tell me how may I help you.")

def option():
    opt=int(input('''Choose an option
    1. Voice
    2.Mannual
    '''))
    print("You choose: ",opt)
    return opt

def takeCommand():
    #it takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception:
        print("Say that again please.")
        return "None"
    return query


if __name__ in "__main__":
    wishMe()
    if option()==1:
        speak("Initiating voice command")
        speak("5")
        speak("4")
        speak("3")
        speak("2")
        speak("1")
        speak("Voice command initiated")
        while True:
            query = takeCommand().lower()

            #Logic for executing tasks based on query.
            if "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("Wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif "open youtube" in query:
                webbrowser.get("edge").open("youtube.com")

            elif "open google" in query:
                webbrowser.get("edge").open("google.com")

            elif "open stackoverflow" in query:
                webbrowser.get("edge").open("stackoverflow.com")

            elif "play music" in query:
                music_dir = "C:\\Users\\Nishu\\OneDrive\\Desktop\\MUSIC"
                songs = os.listdir(music_dir)
                i=random.randint(0,15)
                os.startfile(os.path.join(music_dir, songs[i]))

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif "open code" in query:
                codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif "bye" in query:
                speak("Thanks for your time sir.")
                exit()

    else:
        speak("Initiating manual command.")
        speak("5")
        speak("4")
        speak("3")
        speak("2")
        speak("1")
        speak("Manual command initiated")
        while True:
            query=input("Enter the query please: ")

            # Logic for the executing tasks based on query
            if "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("Wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif "open youtube" in query:
                webbrowser.get("edge").open("youtube.com")

            elif "open google" in query:
                webbrowser.get("edge").open("google.com")

            elif "open stackoverflow" in query:
                webbrowser.get("cedge").open("stackoverflow.com")

            elif "play music" in query:
                music_dir = "C:\\Users\\Nishu\\OneDrive\\Desktop\\MUSIC"
                songs = os.listdir(music_dir)
                i=random.randint(0,15)
                os.startfile(os.path.join(music_dir, songs[i]))

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif "open code" in query:
                codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif "bye" in query:
                speak("Thanks for your time sir.")
                exit()
