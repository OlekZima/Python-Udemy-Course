age = input()

weeks_in_year = round(365 / 7)

weeks_left = (90 - int(age)) * weeks_in_year

print(f"You have {weeks_left} weeks left.")