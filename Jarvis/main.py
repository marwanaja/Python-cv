import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():

    #Salam sesuai arah waktu
    hour = int(datetime.datetime.now().hour)
    if hour >=6 and hour <12:
        speak("Good Morning Wan!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon Wan!")

    else:
        speak("Good evening")

    speak("Im Abi ready to services, how can i help you!?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)

        print("Say it again...")
        return "None"
    return query

if __name__ == '__main__':

   greetings()
   while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching in Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'play music' in query:
        webbrowser.open("spotify.com")

    elif 'open time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the times is {strTime}")

    elif 'i want to sleep' in query:
        speak("Good Night Sir")

    elif 'turn off' in query:
        os.system("shutdown /s /t 1")