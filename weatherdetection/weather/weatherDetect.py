import requests, json



def weather(s):
    api_key = "147b1134e5c0d89525cc02377dc0940f"


    base_url = "http://api.openweathermap.org/data/2.5/weather?"


    city_name = s


    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()
    # print(x)
    if x["cod"] != "404":

        y = x["main"]
        current_temperature = y["temp"]-273
        # print(current_temperature)
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = str(z[0]["description"])
        
        return current_temperature,current_humidity,weather_description
    else:
        return "No data found"

        
#weather("chennai")