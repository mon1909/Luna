import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import requests
from bs4 import BeautifulSoup
import pyautogui
from time import sleep
from pynput.keyboard import Key,Controller
import random
import wolframalpha
from datetime import timedelta
from plyer import notification
from pygame import mixer
from tkinter import *
from PIL import Image,ImageTk,ImageSequence
from fnmatch import translate
from googletrans import Translator
import googletrans 
from gtts import gTTS
import googletrans
from playsound import playsound
import time
import ctypes
import time
import subprocess


mixer.init()

root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("luna.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("soothing.mp3")
    mixer.music.play()
    mixer.music.fadeout(5000)
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()

for i in range(3):
    a = input("Enter password to open Luna : ")
    pw_file=open("password.txt","r")
    pw= pw_file.read()
    pw_file.close()
    if (a==pw):
        print("Welcome!! We can talk")
        break
    elif (i==2 and a!=pw) :
        exit()
    elif(a!=pw):
        print("Try Again :/")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>+0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak(" Hello I am Luna.")
    speak(" How can i help you today?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        r.energy_threshold = 500
        audio=r.listen(source,0,4)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said :{query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

dictapp={"command prompt":"cmd","word":"winword","paint":"paint","excel":"excel","chrome":"chrome","vs code":"code","powerpoint":"powerpnt"}

keyboard = Controller()

def volumeup():
    pyautogui.press('volumeup', presses=5)
        
def volumedown():
    pyautogui.press('volumeup', presses=5)

def wolframAlpha(query):
    apikey='JPQUWL-L67QJ4QGQG'
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        return "The value is not answerable"

def cal(query):
    term = str(query)
    term = term.replace("luna", "")
    term = term.replace("multiplied by", "*")
    term = term.replace("into", "*")
    term = term.replace("plus", "+")
    term = term.replace("divided by", "/")
    term = term.replace("minus", "-")

    Final = str(term)

    try:
        result = wolframAlpha(Final)
        print(f"{result}")
        speak(result)
    except:
        speak("the value is not answerable")

def game_play():
    
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

def translategl(query):
    speak("SURE")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")   
    text_to_translate = translator.translate(query,src = "auto",dest= b,)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia ")
            speak(results)
        
        elif "change password" in query:
            speak("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"Your new password is{new_pw}")
        
        elif "hey" in query:
            speak("Hello ,how are you?")

        elif "i am fine" in query or "i am good" in query or "good" in query:
            speak("That's great")

        elif "how are you" in query:
            speak("Perfect")

        elif "thank you" in query:
            speak("You're welcome.")
        
        elif "let's talk" in query:
            speak("Sure, Let's talk.")
            speak("How was your day?")
        
        elif 'how was your day' in query:
            speak("I'm well")

        elif "what's up" in query :
            try:
                joke=pyjokes.get_joke()
                speak(joke)
            except Exception as e:
                speak("couldn't say a joke.")

        elif 'joke' in query :
            try:
                joke=pyjokes.get_joke()
                speak(joke)
            except Exception as e:
                speak("couldn't say a joke.")

        elif 'idiot' in query:
            speak("I am sorry. what have i done? ")
        
        elif "open" in query:   
            query = query.replace("open","")
            query = query.replace("luna","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter") 
        
        elif "play game" in query or "i am bored" in query :
            speak("Let's play rock, paper and scissors")
            game_play()

        elif "schedule my day" in query:
            tasks = []  
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = takeCommand().lower()

            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()

            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
        
        elif "show my schedule" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
            notification.notify(
                title = "My schedule :-",
                message = content,
                timeout = 15
                )
            
        elif "translate" in query:
                    query = query.replace("luna","")
                    query = query.replace("translate","")
                    translategl(query)

        elif "lock my pc" in query:
            speak("Locking the PC")
            ctypes.windll.user32.LockWorkStation()

        elif "you are amazing" in query:
            speak("i am so glad you like me.")
        
        elif "screenshot" in query:
            import pyautogui 
            im = pyautogui.screenshot()
            im.save("ss.jpg")

        elif "click a picture" in query or "click my picture" in query :
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")
            time.sleep(2)
            if os.name == 'nt':
                subprocess.call("taskkill /IM WindowsCamera.exe /F")
            else: 
                pyautogui.hotkey("alt", "f4")

               
        elif "tired" in query or "favourite music" in query:
            speak("playing your favorite song")
            a= range(1,8)
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=Q-yJcnX0Qzg")
            elif b==2:
                webbrowser.open("https://www.youtube.com/watch?v=jHNNMj5bNQw")
            elif b==3:
                webbrowser.open("https://www.youtube.com/watch?v=mt9xg0mmt28")
            elif b==4:
                webbrowser.open("https://www.youtube.com/watch?v=gJLVTKhTnog")
            elif b==5:
                webbrowser.open("https://www.youtube.com/watch?v=iAIBF2ngbWY")
            elif b==6:
                webbrowser.open("https://www.youtube.com/watch?v=zDknxGb00I4")
            elif b==7:
                webbrowser.open("https://www.youtube.com/watch?v=g3yrqmjaoKA")

        elif "calculate" in query:
            query=query.replace("calculate","")
            query=query.replace("luna","")
            cal(query)

        elif "pause" in query:
            pyautogui.press("k")
            speak("Video paused")
        
        elif "play" in query:
            pyautogui.press("k")
            speak("Video playing")
        
        elif "mute" in query:
            pyautogui.press("m")
            speak("Video muted")

        elif "volume up" in query or "increase the volume" in query:
            speak("Turning volumn up")
            volumeup()
            
        elif "volume down" in query or "increase the volume" in query:
            speak("Turning volumn down")
            volumedown()
        
        elif "remember that" in query:
            rm=query.replace("remember that","")
            rm=query.replace("luna","")
            speak ("You told me "+rm)
            remember=open("remember.txt","w")
            remember.write(rm)
            remember.close()

        elif "what do you remember" in query:
            remember=open("remember.txt","r")
            speak("You asked me to  "+remember.read())

        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break
            
        elif  'open' in query:
               speak("Opening...")
               if ".com" in query or ".co.in" in query or ".org" in query:
                   query=query.replace("luna","")
                   query=query.replace("open","")
                   query=query.replace("launch","")
                   query=query.replace("can you","")
                   query=query.replace("for me","")
                   query=query.replace(" ","")
                   webbrowser.open(f"https://www.{query}")

               else :
                   keys=list(dictapp.keys())
                   for app in keys:
                       if app in query:
                           os.system(f"start {dictapp[app]}")

        elif 'close' in query:
            speak("Closing...")
            if "one tab" in query or "1 tab" in query:
                pyautogui.hotkey("ctrl","w")

            elif "2 tab" in query or "to tab" in query :
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All the tabs are closed")

            elif "3 tab" in query :
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All the tabs are closed")

            elif "4 tab" in query :
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All the tabs are closed")

            elif "5 tab" in query :
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All the tabs are closed")
            
            else:
                keys=list(dictapp.keys())
                for app in keys:
                    if app in query:
                        os.system(f"taskkill /f /im {dictapp[app]}.exe") 

        elif 'youtube' in query:
            speak("This is what i found for your search.")
            query=query.replace("luna","")
            query=query.replace("play","")
            query=query.replace("search for","")
            query=query.replace("on youtube","")
            web= "https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done.")
                
        elif 'google' in query:
            import wikipedia as googleScrap
            query=query.replace("luna","")
            query=query.replace("search for","")
            query=query.replace("in google","")
            query=query.replace("on google","")
            query=query.replace("can you","")
            speak("This is what I found")
            
            try:
                pywhatkit.search(query)
                result=googleScrap.summary(query,2)
                speak(result)
            
            except:
                speak("No speakable output available.")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is{strTime}")
        
        elif 'open vs code' in query:
            codePath="C:\\Users\\monic\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
        
        elif "temperature" in query:
            search= "temperature in bangalore"
            url= f"https://www.google.com/search?q={search}"
            r= requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ ='BNeawe').text
            speak(f"{search} is {temp}")

        elif "weather" in query:
            search= "temperature in bangalore"
            url= f"https://www.google.com/search?q={search}"
            r= requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ ='BNeawe').text
            speak(f"{search} is {temp}")

        elif "bye" in query:
            speak("Thank you for using me. I shall see you soon. Take care")
            exit()
        
        elif "quit" in query:
            exit()