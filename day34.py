import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use 'metric' for Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            print(f"\n🌤️ Weather Report for {city_name.title()} 🌤️")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels Like: {data['main']['feels_like']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Condition: {data['weather'][0]['description'].title()}")
        else:
            print(f"❌ City not found! ({data['message']})")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    print("=== Weather Forecast App ===")
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, api_key)
