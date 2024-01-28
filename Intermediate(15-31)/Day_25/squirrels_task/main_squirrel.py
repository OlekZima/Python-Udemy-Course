import pandas as pd

# Primary Fur Color is the color


def main():
    data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240127.csv")

    fur_color_data = data["Primary Fur Color"]
    fur_color_quantity = fur_color_data.value_counts()
    # fur_color_quantity.to_csv("squirrel_count.csv")
    pd.DataFrame(fur_color_quantity).to_csv("squirrel_count.csv")


if __name__ == "__main__":
    main()
