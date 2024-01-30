from typing import Dict, List


def convert_c_to_f(temp_c: float) -> float:
    return (temp_c * 9 / 5) + 32


def main():
    weather_c = eval(
        input()
    )  # {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

    weather_f: Dict[str, float] = {
        day: convert_c_to_f(temp_c) for (day, temp_c) in weather_c.items()
    }

    print(weather_f)


if __name__ == "__main__":
    main()
