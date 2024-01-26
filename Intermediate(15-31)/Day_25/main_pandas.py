import pandas


def main():
    data = pandas.read_csv("weather_data.csv")
    # print(data)
    print(data["temp"])


if __name__ == "__main__":
    main()
