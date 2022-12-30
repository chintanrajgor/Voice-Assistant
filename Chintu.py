import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener =sr.Recognizer()
bot=pyttsx3.init()
voices=bot.getProperty("voices")
bot.setProperty('voice',voices[0].id)

def talk(text):
    bot.say(text)
    bot.runAndWait()

def take_command():
    try:
        with sr.Microphone() as mic:
            talk("Chintu Reporting, What can I do Captian")
            voice= listener.listen(mic)
            command=listener.recognize_google(voice)
            if "Chintu" in command:
                command = command.replace("Chintu","")
                #talk(command)
    except:
        pass 
    return command

def run_chintu():
    command=take_command()
    if "play" in command:
        song = command.replace('play',"")
        talk('Playing ' + song + " Youtube")
        print(song)
        pywhatkit.playonyt(song)
    elif "whats the time" in command or "what is the current time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is'+ time)
        print(time)
    elif "what is" in command or "who is" in command:
        if 'what is' in command:
            question=command.replace('what is','')
            info=wikipedia.summary(question,1)
            print(info)
            talk(info)
            
        elif 'who is' in command:
            question=command.replace('who is','')
            info=wikipedia.summary(question,1)
            print(info)
            talk(info)
            
    elif "search" in command:
        command=command.replace('search','')
        pywhatkit.search(command)
        talk("Searching "+command+" on Google")
    else :
        talk('Sorry cant Understand')
while True:
    run_chintu()