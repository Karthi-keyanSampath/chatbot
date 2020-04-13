import os
import wolframalpha
import speech_recognition as sr
import sys
import webbrowser
import random
import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1])

def speak(audio):
    print('MAX: ' + audio)
    engine.say(audio)
    engine.runAndWait()

greet = ['what can I do for you?', 'how can i help you?', 'how can I assist you?']
speak('hey boss ' + random.choice(greet))

def myCommand():
    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry BOSS! I didn\'t get that! Try typing the command!')
        query = str(input('MAX : '))

    return query
        
if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open instagram' in query:
            speak('okay opening instagram')
            webbrowser.open('www.instagram.com')

        elif 'open youtube' in query:
            speak('okay opening youtube')
            webbrowser.open('www.youtube.com')

        elif 'open gmail' in query:
            speak('okay opening gmail')
            webbrowser.open('www.gmail.com')

        elif 'what is your name' in query or 'name of the assistant' in query:
            speak('I\'m MAX')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'tell me something' in query:
             th = ['www.nasa.gov/news', 'www.nationalgeographic.com/latest-stories/', 'www.cnet.com/news/', 'www.isro.gov.in','www.researchgate.net']
             webbrowser.open (random.choice(th))
        elif "what\'s your boss name" in query or "name of your creator" in query:
            stMsgs = ['karthikeyan']
            speak(random.choice(stMsgs))
            
        elif 'open twitter' in query:
            speak('okay opening twitter')
            webbrowser.open("www.twitter.com")

        elif 'open email' in query:
            speak('okay opening email')
            webbrowser.open("www.email.com")

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye boss, have a good day.')
            sys.exit()
           
        elif 'hello' in query or 'hi' in query or 'hi max' in query or 'hello max' in query:
            speak('Hello boss, how may I help you?')

        elif 'bye' in query or 'bye MAX' in query:
            speak('Bye boss, have a good day.')
            sys.exit()
                                    
        elif 'open map' in query:
            speak('okay opening map')
            webbrowser.open("www.google.co.in/maps")

        elif 'open translator' in query:
           speak('Okay openig G translate')
           webbrowser.open("www.translate.google.co.in")
           
        elif 'about you' in query or 'about MAX' in query:
            speak('I\'m your digital assistant MAX, made by KARTHIKEYAN in 31 april 2020')
           
        elif 'open news' in query or 'show news' in query or 'show current affairs' in query:
            speak('opening news')
            webbrowser.open("news")

        else:
            query = query
            speak('Searching...')
            
            try:
                try:
                    client = wolframalpha.Client('JKT223-QK73WYJ6JL')
                    res = client.query(query)
                    results = next(res.results).text
                    speak('here the information')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)
        
            except:
                webbrowser.open("query")
        
        speak('Next Command! boss!')
        
