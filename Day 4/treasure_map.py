                        # A   B   C
line1 = [" ", " ", " "] # 1   1   1
line2 = [" ", " ", " "] # 2   2   2
line3 = [" ", " ", " "] # 3   3   3

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input()

row = int(position[1]) - 1

collumn = position[0]
if collumn == 'A':
    collumn = 0
elif collumn == 'B':
    collumn = 1
elif collumn == 'C':
    collumn = 2

map[row][collumn] = 'X'

print(f"{line1}\n{line2}\n{line3}")
