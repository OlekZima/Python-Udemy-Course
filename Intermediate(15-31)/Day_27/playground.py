def add(*nums: int) -> int:  # *args is a tuple
    overall_sum = 0
    for n in nums:
        overall_sum += n
    return overall_sum


def calculate(n, **kwargs):  # **kwargs is a dict
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


def main():
    print(add(1, 2, 3, 4, 5, 6, 7, 6, 11, 23, 1, 23, 123, 1, 23, 145, 15, 1, 25))

    calculate(2, add=3, multiply=5)


if __name__ == "__main__":
    main()
