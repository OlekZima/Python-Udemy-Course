student_heights = input().split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number_of_students = 0
total_height = 0
for n in student_heights:
    total_height += n
    number_of_students += 1

print(round(total_height/number_of_students))