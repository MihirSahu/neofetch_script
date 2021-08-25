#!/usr/bin/python3

import os
import requests
import json

#Quotes
dict = json.loads(requests.get('https://api.quotable.io/random').content)
print(dict["content"])

print('')

#Time
req = requests.get('https://timeapi.io/api/Time/current/zone?timeZone=US/Central').json()
print(req["dayOfWeek"] + " " + req["time"] + " " + req["date"])

print('')

#Weather
dict = json.loads(requests.get('http://api.weatherapi.com/v1/current.json?key=de975d3393fa4dd19ad211908212308&q=Houston&aqi=no').content)
print("Weather for " + dict["location"]["name"] + ", " + dict["location"]["region"])

if dict["current"]["condition"]["code"] in os.listdir("~/.config/weather_icons"):
    print()
