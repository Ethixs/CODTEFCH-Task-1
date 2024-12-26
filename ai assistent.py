# pip install SpeechRecognition
# pip install pyttsx3
# pip install pywhatkit
# pip install wikipedia

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import webbrowser

# Initialize the Recognizer instance
r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print('Listening...')
            audioin = r.listen(source)  # Capture audio
            my_text = r.recognize_google(audioin)  # Recognize speech using Google
            my_text = my_text.lower()  # Convert speech to lowercase for consistency
            print(my_text)
            #speak(my_text)
            
            #youtube
            if 'play' in my_text:
                my_text= my_text.replace('play','')
                speak('playing'+my_text)
                pywhatkit.playonyt(my_text)
                
            #Google
            if 'search' in my_text:
                my_text = my_text.replace('search', '')
                speak(f"Searching for {my_text} on Google")
                query = my_text.strip()
                webbrowser.open(f"https://www.google.com/search?q={query}")
    
            #date
            elif 'date' in my_text:
                today= datetime.date.today()
                speak(today)
                
            #time
            elif 'time' in my_text:
                timenow= datetime.datetime.now().strftime('%H:%M')
                speak(timenow)
                
            #wikipedia
            elif 'who is' in my_text:
                person= my_text.replace('who is','')
                info= wikipedia.summary(person,1)
                speak(info)
                
            #phone number
            #if "phone number"in my_text:
                #names=list(phone_numbers)
                #print(names)
                #for name in names:
                    #if name in my_text:
                        #print(name + "phone number is" + phone_numbers[name])
                        #speak(name + "phone number is" + phone_numbers[name])
                    
            else:
                speak('i can not here you')
            
                
            
            
    except sr.UnknownValueError:
        print('Sorry, I could not understand the audio.')  # Specific exception for unrecognized audio
    except sr.RequestError:
        print('Sorry, there was an error with the speech service.')  # Specific exception for API errors
    except Exception as e:
        print(f'An unexpected error occurred: {e}')  # General error handler

# Start the program
speak("Welcome to Quify")
commands()
