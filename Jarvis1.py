import pyttsx3
import datetime
import speech_recognition as sr #speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir ")
    elif hour>=12 and hour<=18:
        speak("good aftenoon sir ")
    else:
        speak("good Evening sir ")
        
    speak("i am  jarvis sir . please tell me how may i help you , share your problem with me")
def takeCommand():
    #it takes microphone input from the user and return string output
    
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        #print(e)
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttIs()
    server.login('youremail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir , the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\Sohail\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'email to harry' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "harryyourEmail.com"
                sendEmail(to , content)
                speak("Email has been sent")
            except Exception as e :
                print (e)
                speak("sorry sir  email was not sent")



    