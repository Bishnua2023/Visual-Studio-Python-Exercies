import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature_kelvin = data["main"]["temp"]
            temperature_celsius = kelvin_to_celsius(temperature_kelvin)

            print(f"Weather in {city}: {weather_description}")
            print(f"Temperature: {temperature_celsius:.2f} °C")
        else:
            print(f"Error: {data['message']}")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")

if _name_ == "_main_":
    api_key = "7cbda39c729111aa7fe17b2e34b774b1"
    city = input("Enter the name of the municipality: ")

    get_weather(api_key, city)