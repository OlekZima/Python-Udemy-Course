from time import sleep
from typing import Tuple
import requests
from datetime import datetime
import smtplib
import credentials


def get_iss_position() -> Tuple[float, float]:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    iss_pos = (float(latitude), float(longitude))

    # print(iss_pos)

    return iss_pos


def is_iss_above(lat: float, lng: float, iss_position: Tuple[float, float]) -> bool:
    is_lat = False
    is_lng = False
    if iss_position[0] - 5 < lat < iss_position[0] + 5:
        is_lat = True
    if iss_position[1] - 5 < lng < iss_position[1] + 5:
        is_lng = True

    return is_lat and is_lng


def get_sunrise_sunset_now_hours(lat: float, lng: float):
    base_url = "https://api.sunrise-sunset.org/json"

    parameters = {
        "lat": lat,
        "lng": lng,
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

    return (sunrise_hour, sunset_hour, time_now_hour)


def is_night_now(time: Tuple[int, int, int]) -> bool:
    if time[2] > time[1] and time[2] > time[0]:
        return True
    return False


def main(lat: float, lng: float) -> bool:
    time = get_sunrise_sunset_now_hours(lat, lng)
    is_night = is_night_now(time)

    iss_pos = get_iss_position()
    is_above = is_iss_above(lat, lng, iss_pos)

    if is_night and is_above:
        return True
    return False


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=credentials.gmail, password=credentials.gmail_app)
        connection.sendmail(
            from_addr=credentials.gmail,
            to_addrs=credentials.gmail,
            msg=f"Subject:Look up! ISS\n\nLook at the sky, ISS is close!",
        )


if __name__ == "__main__":
    is_look = main(lat=52.229675, lng=21.012230)
    if is_look:
        for _ in range(5):
            send_mail()
            sleep(60)

if __name__ == "__main__":
    sleep(60)
    is_look = main(lat=52.229675, lng=21.012230)
    if is_look:
        send_mail()
