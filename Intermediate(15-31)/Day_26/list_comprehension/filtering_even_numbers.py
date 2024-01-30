list_of_strings = input().split(",")

list_of_ints = [int(num) for num in list_of_strings]

result = [n for n in list_of_ints if n % 2 == 0]

print(result)
