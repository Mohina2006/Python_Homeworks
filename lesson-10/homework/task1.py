import requests

def get_coordinates(city, api_key):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    try:
        response = requests.get(geo_url)
        response.raise_for_status()
        data = response.json()
        

        if not data:
            print(f"❌ No coordinates found for city: {city}")
            return None, None

        lat = data[0].get('lat')
        lon = data[0].get('lon')
        return lat, lon

    except requests.RequestException as e:
        print("🚫 Network or API error:", e)
        return None, None

def get_weather_by_coordinates(lat, lon, api_key):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        data = response.json()

        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        print(f"\n🌤️ Weather Info:")
        print(f"📌 Description: {description}")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")

    except requests.RequestException as e:
        print("🚫 Failed to retrieve weather data:", e)

api_key = '619f1b281b24e6834170f25f0f8a8509' 

city = input("Enter a city: ").strip()

lat, lon = get_coordinates(city, api_key)
if lat is not None and lon is not None:
    get_weather_by_coordinates(lat, lon, api_key)
else:
    print("❗ Program ended due to invalid city or API error.")
