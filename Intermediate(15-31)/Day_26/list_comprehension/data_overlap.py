from typing import List


def get_list_from_file(path: str) -> List[int]:
    with open(path, mode="r") as f:
        list_of_ints = f.read().split("\n")
        return [int(n) for n in list_of_ints]


def main():
    first_file = get_list_from_file("./file1.txt")
    second_file = get_list_from_file("./file2.txt")
    result = [num for num in first_file if num in second_file]
    print(result)


if __name__ == "__main__":
    main()
