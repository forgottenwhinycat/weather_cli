import requests
import argparse
from config import API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise ValueError(data.get("message", "Failed to get weather data"))

    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
    return weather

def main():
    parser = argparse.ArgumentParser(description="Get current weather by city")
    parser.add_argument("city", help="City name to get the weather for")
    args = parser.parse_args()

    try:
        weather = get_weather(args.city)
        print(f"{weather['city']}: {weather['temperature']}°C, {weather['description'].capitalize()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
