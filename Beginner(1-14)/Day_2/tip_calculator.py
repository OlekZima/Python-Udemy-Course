def main():
    print("Welcome to the tip calculator.")

    total_bill = float(input("What was the total bill? $"))
    people_number = int(input("How many people to split the bill? "))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

    total_bill += total_bill * tip_percentage / 100
    bill_per_person = round(total_bill / people_number, 2)


    print(f"Each person should pay: ${bill_per_person}")

if __name__ == "__main__":
    main()