import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Faisal")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            speak("bye bye friend")
            break
        speak(x)
