import speech_recognition as sr
import pyttsx3
import datetime
import requests

r = sr.Recognizer()

engine = pyttsx3.init()

def set_reminder(reminder_time):
    current_time = datetime.datetime.now()
    reminder_time = datetime.datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")
    if reminder_time > current_time:
        time_diff = reminder_time - current_time
        engine.say("Reminder set for " + str(time_diff) + " from now")
        engine.runAndWait()
    else:
        engine.say("Invalid reminder time. Please try again.")
        engine.runAndWait()

def check_weather(location):
    weather_api_key = "7d2e36b5da66c9181317fd67e5057edd"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "404":
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        engine.say(f"The weather in {location} is {weather} with a temperature of {temp} degrees Celsius.")
        engine.runAndWait()
    else:
        engine.say("Location not found. Please try again.")
        engine.runAndWait()

def who_is_it():
    engine.say("I am a personal assistant. My name is Karen.")
    engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        if "reminder" in text:
            reminder_time = text.split("for")[-1]
            set_reminder(reminder_time)
        elif "who are you" in text.lower():
            who_is_it()
        elif "weather" in text:
            location = text.split("in")[-1]
            check_weather(location)
    except sr.UnknownValueError:
        print("PocketSphinx could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from PocketSphinx service; {0}".format(e))
