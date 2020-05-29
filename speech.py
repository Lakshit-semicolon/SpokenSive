import speech_recognition as sr
from speak import female

female("I am starting")
def rect1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak")
        female("Please Speak")
        r.pause_threshold=1 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Analyzing \...") 
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            female("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")
            female("Sorry could not recognize what you said")
            rect()
def rect():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak")
        female("Please Speak")
        r.pause_threshold=1 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Analyzing \...") 
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            female("You said : {}".format(text))
            print("Do you want to convert to handwritting?(yes/no)")
            female("Do you want to convert to handwritting?(yes/no)")
            
            flagin=rect1()
            if flagin == "yes":
                return text
            else:
                rect()    
        except:
            print("Sorry could not recognize what you said")
            female("Sorry could not recognize what you said")
            rect()


