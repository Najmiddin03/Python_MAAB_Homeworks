import requests

api_key = "3c05315253118f0776373b9a6ca6485b"

url = f"http://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    weather_description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']

    print(f"Weather in Warsaw:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Weather: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Error: {response.status_code}, Unable to fetch weather data")
