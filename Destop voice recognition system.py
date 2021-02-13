import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[2].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Friday Sir. Please tell me how may I help you")


def takeCommand():
    #it takes microphone input from the user and return string as an output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: \n", query)

    except Exception as e:
        #print(e) for printing error in voice recognition
        print("Please! Say it again")
        return "None"  # Here, None is string not none use in python
    return query


if __name__ == "__main__":
    #speak("Satyam is good boy")
    wishme()
    while True:
        query = takeCommand().lower()
    #Logics for executing task based on query
    if 'wikipedia' in query:
        speak("Searching Wikipedia....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=3)
        speak("According to wikipedia.")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
    elif 'open twitter' in query:
        webbrowser.open("twitter.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackover.com")

    elif 'play music' in query:
        music_dir = 'E:\\Music\\Music\\1. Best\\English Songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[2]))
    
    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Sir, the time is ", strtime)

    elif 'open practical' in query:
        practicalPath = "C:\\Users\\hp\\Desktop\\Practical"
        os.startfile(practicalPath)