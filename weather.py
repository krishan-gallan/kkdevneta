import requests
cityName = input("please enter the city name for current temperature: -\n")
api_key = "a74cb1ad03eae1d5d658bdb2dc335371"
url = "http://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid="+api_key+"&units=metric"
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
request = requests.get(url)
json = request.json()
#print(json)
descr = json.get("weather")[0].get("description")
cityTemp = json.get("main").get("temp")
print(f"{cityName} city temperature is {cityTemp} and weather remains {descr}"   )

