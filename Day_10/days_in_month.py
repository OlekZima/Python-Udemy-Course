def is_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year: int, month: int) -> int:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year = is_leap(year)
    if is_leap_year and month == 2:
        return month_days[month - 1] + 1
    return month_days[month - 1]

def main():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)

def test_days():
    assert days_in_month(2020, 2) == 29
    assert days_in_month(2022, 2) == 28

if __name__ == "__main__":
    try:
        test_days()
        main()
    except AssertionError:
        print("Test failed!")