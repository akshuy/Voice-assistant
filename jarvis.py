import datetime
from http import server
import scipy as sp
import wikipedia
import os
import speech_recognition as sr
import smtplib
import pyttsx3
import webbrowser

engine = pyttsx3.init('sapi5')  # sapi5 is use to get inbuilt voices in windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good moening ")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening ")
    speak("i'm jarvi girl sir . plese tell me how may i help you")

def takeCommand():  # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print("say that again plese... ")
        return "None"
    return query


if __name__ == "__main__":
    wishme()


    while True:
        Query = takeCommand().lower()
        #  logic for executing task based on Query
        if 'wikipedia' in Query:
            speak('searching wikikpedia...')
            Query = Query.replace("wikipedia", "")
            results = wikipedia.summary(Query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
       
        elif "youtube" in Query:
            webbrowser.open("youtube.com")
       
        elif "google" in Query:
            webbrowser.open("google.com")
        
        elif "open stack overflow" in Query:
            webbrowser.open("stackoverflow.com")

        elif "cricket score" in Query:
            webbrowser.open(
                "https://www.cricbuzz.com/cricket-match/live-scores")

        elif "i am tired" in Query:
            speak("you need to straigh tashrif ")

        elif "music" in Query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in Query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S:")
            speak(f"sir the time is {strTime}")

        elif "code" in Query:
            code_path = "C:\\Users\\aim to coad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "rte portal" in Query:
            webbrowser.open("https://rajpsp.nic.in/PSP2/Home/schoollogin.aspx")

        elif "yourself" in Query:
            speak("my self jarvi and i was built by developer akshay sharma on the date: 18/07/2022. in bagru (narwariya) say thanks to him becouse his hardwork built and also update me ")

        elif "whatsapp" in Query:
            whatsapp_path = "C:\\Users\\aim to coad\\OneDrive\\Desktop\\whatsapp"

        elif "akshay is a bad" in Query:
            speak("don't call akshay like that in front of me otherwise i will uninstall my self from your device!")    

        elif "how are you" in Query:
            speak("i'm good hope you also great")    

     
        elif "what are you doing" in Query:
            speak("i'm just wakeup becous you needs me")

        elif "what do you do"in Query:
            speak("after helpes you. i'm sleeping whole day")         

        
        else:
            speak("i'm not able to listion plese speak again")     
            
