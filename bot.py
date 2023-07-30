import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')


def parle(text):
    engine.say(text)
    engine.runAndWait()


def ecoute():
    try:
        with sr.Microphone() as source:
            print("parler")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')

    except:
        pass
    return command


def assistant():
    command = ecoute()
    print(command)
    if 'bonjour' in command:
        parle('bonjour comment ca va ?')

    elif 'bien et toi ' in command:
        parle('je vais bien merci, comment je peut vous aider ?')

    elif 'mettez la chanson de' in command:
        chanteur = command.replace('mettez la chanson de', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)

    elif 'heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        parle("il est "+heure)

    elif 'ton nom' in command:
        parle(" je m'appelle Ghost H 404")


while True:
    assistant()
