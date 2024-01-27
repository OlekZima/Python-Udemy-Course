import pandas as pd


def main():
    data = pd.read_csv("../weather_data.csv")
    # print(data)
    # print(type(data))
    # print(type(data["temp"]))

    data_dict = data.to_dict()
    print(data_dict)

    data_series_list = data["temp"].to_list()
    print(data_series_list)

    print(data["temp"].max())
    print(data.condition)  # So cursed

    print(data[data["day"] == "Monday"])

    print("==" * 40)
    print(data[data["temp"] == data["temp"].max()])
    print("==" * 40)

    monday = data[data["day"] == "Monday"]
    monday_temp = monday["temp"]
    monday_temp_fahr = monday_temp * 9 / 5 + 32
    print(monday_temp_fahr)
    print("==" * 40)

    data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

    new_dataframe = pd.DataFrame(data_dict)
    # print(new_dataframe)
    new_dataframe.to_csv("../new_data.csv")


if __name__ == "__main__":
    main()
