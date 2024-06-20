import requests
import json
city = input("Enter your city name\n")
url = f"https://api.weatherapi.com/v1/current.json?key=1edaa6debe914ca5ba6153350242803&q={city}"

r=requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])