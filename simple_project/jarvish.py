import pyttsx3 as p3
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import datetime



def speak(text):
    engine=p3.init()
    engine.setProperty('rate',190)
    engine.say(text)
    engine.runAndWait() 
def takevoice():
    r=sr.Recognizer()
    with sr.Microphone()as sourse:
        print("listening.....................")
        r.pause_threshold=1
        audio=r.listen(sourse)
    try:
        print("recognizing.......")
        query=r.recognize_google(audio,language='en-in')
        print(query)
        return query
    except Exception as  e:
        print(e)
        print("sorry say again..........")
        return

if __name__== "__main__":
    speak("Hello  sir  i am your assistent . how can i help you")
    while True:
        command=takevoice().lower()

        if command == "who are you":
            speak("i am your assistance ")
        
        elif "boss" in command:
            speak("my boss is banti sir ")
        elif "good morning" in command:
            speak("good morning banti sir")  
        elif "good afternoon" in command:
            speak("good afternoon banti sir") 
        elif "good evening" in command:
            speak("good evening banti sir")  
    
        elif "sheetal" in command:
            speak("sheetal is banti sir friend")
        elif "thank you" in command:
            speak("Welcome  sir ")
        elif "youtube" in command :
            webbrowser.open("https://www.youtube.com/watch?v=mkYq7FuCfi0&list=PLgWjD_CBfh0DlYNZwgmrS-rO4U143kskh&index=3")
        elif "google" in command :
            webbrowser.open("https://www.google.co.in/?gfe_rd=cr&ei=_w5RWPj3E-3s8AfXu6b4Dw")
        elif "wikipedia"  in  command :
            speak("searching in wikipedia.........")
            command = command.replace("wikipedia", "")
            result= wikipedia.summary(command,sentences = 2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif "music" in command:
            os.startfile("C:\\Users\\DELL\\Music\\mp3\\3(mp3pk.com)(1)(1).mp3")
            speak("open sucsessfull  sir ")
        elif "time" in command:
            speak(datetime.datetime.now())
            print(datetime.datetime.now())
            print(speak)

        elif "phone number" in command:
            speak("7697691340  number is banti sir ")
         
        elif "kaise ho dear" in command:
            speak(" i am fine sir and about you ")
        elif "rani" in command:
            speak(" i  love you yash love you so much ")
        elif "birthday" in command:
            speak(" happy birthday banti sir good bless you")
        elif "sleeping" in command:
            speak("good night sir sweet dreams ")
        elif "my friends name" in command:
            
            speak(" khushi akash ritika shantanu  anzeela  sheetal pooja di  ranudi")