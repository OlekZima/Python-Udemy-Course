import requests
from datetime import datetime

base_url = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": 52.229675,
    "lng": 21.012230,
    "formatted": 0,
    # "tzid": "Europe/Warsaw",
}

response = requests.get(base_url, params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time_unix: str = data["results"]["sunrise"]
sunset_time_unix: str = data["results"]["sunset"]

sunrise_hour = sunrise_time_unix.split("T")[1].split(":")[0]
sunset_hour = sunset_time_unix.split("T")[1].split(":")[0]

time_now_hour = datetime.now().time().hour
print(sunrise_hour, sunset_hour)
print(time_now_hour)
