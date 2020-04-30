import pyttsx3 #pip install pyttsx3
import speech_recognition as s_r #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio

name = input("Enter Your Name:")
if len(name) < 1 : MASTER = "Meghang"
else : MASTER = name

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
hour = int(datetime.datetime.now().hour)
mins = int(datetime.datetime.now().minute)

#Speak function will pronounce this string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#wishMe function will speak morning/afternoon/evening as per current time
def wishMe():
    print("INITIALISING ASSISTANT...")
    speak("Initialising assistant...")
    if hour > 0 and hour < 12 :
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour <= 18 :
        speak("Good Afternoon" + MASTER)
    else :
        speak("Good Evening" + MASTER)
    speak("How can i help you?")

#this function will take command from the microphone
def takeCommand():
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1)
    print("LISTNING...")
    with my_mic as source :
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("RECOGNISING...")
    my_string = r.recognize_google(audio)
    return my_string

def quit():
    print("SHUTTING DOWN ASSISTANT...")
    if hour > 0 and hour < 18 :
        speak("Good Day" + MASTER)
    else :
        speak("Good Night" + MASTER)
    speak("See you soon")

#main program starts here
wishMe()
while True:
    my_string = takeCommand()

    #code for executing tasks as per my_string
    if 'wikipedia' in my_string.lower():
        print("SEARCHING WIKIPEDIA...")
        speak("Searching wikipedia...")
        my_string = my_string.replace("wikipedia", "")                                                  #WIKIPEDIA
        wiki_results = wikipedia.summary(my_string, sentences = 2)
        speak(wiki_results)
        continue
    
    elif 'youtube' in my_string.lower():
        print("OPENING YOUTUBE...")                                                                     #OPENING YOUTUBE
        speak("Opening Youtube...")
        webbrowser.open("www.youtube.com")
        speak("Enjoy Youtube")
        continue

    elif 'google' in my_string.lower():
        print("OPENING GOOGLE")
        speak("Opening google")                                                                         #OPENING GOOGLE
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        speak("Enjoy google")
        continue

    elif 'time' in my_string.lower():
        print("The time is --> ", hour, ":", mins)
        speak("The time is ")                                                                           #TIME
        speak(hour)
        speak(mins)
        continue

    elif 'how are you' in my_string:
        print("I am fine thank you.")
        speak("I am fine, thank you.")
        continue

    elif 'quit assistant' in my_string:
        quit()                                                                                          #QUIT ASSISTANT
        break
    
    else:
        print("I CANNOT DO THIS TRY AGAIN")                                                             #TRY AGAIN
        speak("I am not programmed to do this task yet, but i will improve soon, try again.")
