import requests as r
import json
import pyttsx3

def pronounce(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

city = input("Enter the City name you want to get the Temparature : ")

url = f"https://api.weatherapi.com/v1/current.json?key=f3df7412bbb741a48cf170913241002&q={city}"

ans = r.get(url)
print(ans.text)
wdic = json.loads(ans.text)

region = wdic["location"]["region"]
degree  = wdic["current"]["temp_c"]
command = f"The Temperature is {degree} in {region}  "
pronounce(command)
