# this program run in online mode
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening ")
    speak("hello sir i am Jarvis how may i help you ")


def takecommand():
    # it take microphone input from the user and returns string output

    r = sr.Recognizer()  #recognizer is use to recognize the voice of the user``
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query} \n")

    except Exception as e:
        # print (e)
        print("say that again please....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shawvishal236@gmail.com', 'furtjzxmmwsulijyy')
    server.sendmail('shawvishal236@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

    wishme()
    while True:
        # if 1:
        query = takecommand().lower()
        # logic for executing takes based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoring to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  # or the next line
            # webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            search = takecommand()
            url = 'https://youtube.com/search?q=' + search
            webbrowser.open(url)
            speak("here is what i found for" + search)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takecommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.open(url)
            speak('Here is What I found for' + search)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'play music' in query:
            music_dir = 'D:\\non critical\\songs\\favourite songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
            print(strtime)

        elif 'open code' in query:
            codepath = "C:\\Users\\shawv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open pycharm' in query:
            cpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(cpath)

        elif 'email to ' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = "nihalshaw4@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry my friend. I am not able to send the email  ")

        elif 'quit' in query:
            exit()
