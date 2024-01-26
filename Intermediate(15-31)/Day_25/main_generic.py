def main():
    data = []
    with open("weather_data.csv", mode="r") as f:
        data = f.readlines()
    print(data)


if __name__ == "__main__":
    main()
