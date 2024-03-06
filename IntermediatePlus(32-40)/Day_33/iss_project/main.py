from typing import Tuple
import requests
from datetime import datetime


def get_iss_position() -> Tuple[float, float]:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    return (float(latitude), float(longitude))


def is_iss_above(lat: float, lng: float, iss_position: Tuple[float, float]) -> bool:
    if iss_position[0] - 5 < lat < iss_position[0] + 5:
        is_lat = True
    if iss_position[1] - 5 < lng < iss_position[1] + 5:
        is_lng = True

    return is_lat and is_lng


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

sunrise_hour = int(sunrise_time_unix.split("T")[1].split(":")[0])
sunset_hour = int(sunset_time_unix.split("T")[1].split(":")[0])

time_now_hour = datetime.now().time().hour
print(sunrise_hour, sunset_hour)
print(time_now_hour)
