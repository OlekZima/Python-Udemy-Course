target = int(input()) # between 0 and 1000

sum_of_n_even = 0

for number in range(0, target + 1, 2):
    sum_of_n_even += number

print(sum_of_n_even)