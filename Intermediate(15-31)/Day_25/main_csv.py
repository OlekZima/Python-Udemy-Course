import csv
from typing import List

with open("weather_data.csv", mode="r") as file:
    data = csv.reader(file)
    temperatures: List[int] = []
    for row in data:
        if row[1] == "temp":
            continue
        temperatures.append(int(row[1]))

    print(temperatures)
