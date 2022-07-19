import json
import requests


def get_weather_desc_and_temp():
    api = "82a94936c64849c9e2f5dc6b0db7da24"
    city = {
        "name": "Orlando",
        "lat": 28.5384,
        "lon": 81.3789,
    }

    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&appid={api}&units=imperial"

    promise = requests.get(URL)
    response = promise.json()

    description = response.get("weather")[0].get("description")
    temperature = [
        response.get("main").get("temp_min"),
        response.get("main").get("temp_max"),
    ]
    return {"description": description, "temperature": temperature}


def main():
    weather_dict = get_weather_desc_and_temp()

    print(
        f"todays weather is {weather_dict.get('description')} with a mininum temp of {weather_dict.get('temperature')[0]} and a max of {weather_dict.get('temperature')[1]}"
    )


# write_file = open("weather.json", "w")
# write_file.write(json.dumps(response, indent=2))
# write_file.close()

# read_file = open("weather.json", "r")
# weather_text = read_file.read()
# read_file.close()
