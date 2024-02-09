def add(*nums: int):
    overall_sum = 0
    for n in nums:
        overall_sum += n
    return overall_sum


print(add(1, 2, 3, 4, 5, 6, 7, 6, 11, 23, 1, 23, 123, 1, 23, 145, 15, 1, 25))
