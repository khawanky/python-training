# from urllib import request
import requests
import json
import pyttsx3

# r = request.urlopen("http://www.google.com")

api_url_response = requests.get("https://official-joke-api.appspot.com/random_ten")
print(api_url_response.status_code)
data = api_url_response.text
json_data = json.loads(data)
# print(json_data)


class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        return f"Setup: {self.setup}, Punchline: {self.punchline}"

jokes = []

for j in json_data:
    my_setup = j['setup']
    punch_line = j['punchline']

    joke = Joke(my_setup, punch_line)
    # jokes.append(joke)
    jokes.append(joke)

engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 300)     # setting up new voice rate

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#
# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()
#
# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()


engine.say("Salma")

num = 3
num2 = 0

for joooo in jokes:
    print(joooo)
    # pyttsx3.speak(joooo.setup)
    # pyttsx3.speak(joooo.punchline)
    num2+=1
    if num == num2:
        break
