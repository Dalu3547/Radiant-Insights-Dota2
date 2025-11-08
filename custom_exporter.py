from prometheus_client import Gauge, start_http_server
import requests, time, os

# --- Configuration ---
API_KEY = "bfce22d80cfaca9c2bb11af6c8354167"  # Replace with your OpenWeather API key
CITY = "Astana"                # Change to your city
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# --- Define metrics ---
temp = Gauge('weather_temperature_celsius', 'Current temperature in Celsius')
feels = Gauge('weather_feels_like_celsius', 'Feels-like temperature in Celsius')
humidity = Gauge('weather_humidity_percent', 'Humidity (%)')
pressure = Gauge('weather_pressure_hpa', 'Atmospheric pressure (hPa)')
wind_speed = Gauge('weather_wind_speed_mps', 'Wind speed (m/s)')
clouds = Gauge('weather_cloudiness_percent', 'Cloudiness (%)')
visibility = Gauge('weather_visibility_meters', 'Visibility (m)')
sunrise = Gauge('weather_sunrise_timestamp', 'Sunrise timestamp (UTC)')
sunset = Gauge('weather_sunset_timestamp', 'Sunset timestamp (UTC)')
temp_diff = Gauge('weather_temp_difference', 'Difference between temperature and feels like (C)')
wind_chill = Gauge('weather_wind_chill', 'Approx. wind chill temperature (C)')

def fetch_weather():
    try:
        r = requests.get(URL)
        data = r.json()
        main = data['main']
        wind = data['wind']
        sys = data['sys']

        t = main['temp']
        f = main['feels_like']
        h = main['humidity']
        p = main['pressure']
        w = wind['speed']
        c = data['clouds']['all']
        v = data.get('visibility', 0)
        sr = sys['sunrise']
        ss = sys['sunset']

        # set metrics
        temp.set(t)
        feels.set(f)
        humidity.set(h)
        pressure.set(p)
        wind_speed.set(w)
        clouds.set(c)
        visibility.set(v)
        sunrise.set(sr)
        sunset.set(ss)
        temp_diff.set(t - f)
        wind_chill.set(t - (0.7 * w))

        print(f"[OK] Temp={t}°C, Feels={f}°C, Hum={h}%, Wind={w}m/s, Clouds={c}%")

    except Exception as e:
        print("[Error]", e)

if __name__ == "__main__":
    start_http_server(9000)
    print("Weather exporter started on port 9000")
    while True:
        fetch_weather()
        time.sleep(20)
