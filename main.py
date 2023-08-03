import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

var = True


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("I am your alexa assistant master Sambhav, what can I do for you")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print("Query = " + command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time)
    elif 'search' in command:
        element = command.replace('search', '')
        info = wikipedia.summary(element, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'turn off' in command:
        global var
        talk("Thank you for letting me help you, Please call me again soon")
        var = False
    else:
        talk("Sorry, I did not understood, Please repeat again")


while var:
    run_alexa()


















