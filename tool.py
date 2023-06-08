import requests
import argparse

def get_weather_forecast(city):
    api_key = "102ef2ff474723e3b5d7ef4c5496cef0"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        if data.get("cod") == 200:
            weather_info = {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
            
            print(f"Weather forecast for {city}:")
            print(f"Temperature: {weather_info['temperature']}°C")
            print(f"Description: {weather_info['description']}")
            print(f"Humidity: {weather_info['humidity']}%")
        else:
            print(f"Error: {data['message']}")
        
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get current weather forecast for a city")
    parser.add_argument("city", help="Name of the city")
    args = parser.parse_args()
    
    get_weather_forecast(args.city)