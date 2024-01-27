import csv
from typing import List


def main():
    with open("weather_data.csv", mode="r") as file:
        data = csv.reader(file)
        temperatures: List[int] = []
        for row in data:
            if row[1] == "temp":
                continue
            temperatures.append(int(row[1]))

        print(temperatures)


if __name__ == "__main__":
    main()
