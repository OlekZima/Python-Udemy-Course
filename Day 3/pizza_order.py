print("Thank you for choosing Python Pizza Deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input()

total_bill = 0

if size == 'S':
    total_bill += 15
elif size == 'M':
    total_bill += 20
elif size == 'L':
    total_bill += 25
else:
    print("What size? Error")

if add_pepperoni == 'Y':
    if size == 'S':
        total_bill += 2
    elif size == 'M' or size == 'L':
        total_bill += 3

if extra_cheese == 'Y':
    total_bill += 1

print(f"Your final bill is: ${total_bill}")