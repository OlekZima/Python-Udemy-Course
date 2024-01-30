from typing import Dict, List


def main():
    sentence: List[str] = input().split(" ")
    # sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

    result: Dict[str, int] = {word: len(word) for word in sentence}
    print(result)


if __name__ == "__main__":
    main()
