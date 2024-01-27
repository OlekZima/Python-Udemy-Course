from typing import List


def main():
    data: List[str] = []
    with open("weather_data.csv", mode="r") as f:
        data = f.readlines()
    print(data)


if __name__ == "__main__":
    main()
