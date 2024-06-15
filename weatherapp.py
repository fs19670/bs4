import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    city = input("Enter the name of the city\n")
    
    url = f"http://api.weatherapi.com/v1/current.json?key=a6aa0a42c0874e70bcd203826241506&q={city}"
    
    r = requests.get(url)
    
    if r.status_code == 200:
        wdic = json.loads(r.text)
        w = wdic["current"]["temp_c"]
        
        message = f"The current weather in {city} is {w} degrees"
        print(message)
        speak(message)
    else:
        error_message = "Sorry, I couldn't fetch the weather information."
        print(error_message)
        speak(error_message)
