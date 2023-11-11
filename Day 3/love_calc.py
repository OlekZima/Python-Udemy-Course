print("The Love Calculator is calculating your score...")
name1 = input().lower()
name2 = input().lower()

true_counter = 0
love_counter = 0

# True counter
true_counter += name1.count('t')
true_counter += name2.count('t')

true_counter += name1.count('r')
true_counter += name2.count('r')

true_counter += name1.count('u')
true_counter += name2.count('u')

true_counter += name1.count('e')
true_counter += name2.count('e')

# Love counter
love_counter += name1.count('l')
love_counter += name2.count('l')

love_counter += name1.count('o')
love_counter += name2.count('o')

love_counter += name1.count('v')
love_counter += name2.count('v')

love_counter += name1.count('e')
love_counter += name2.count('e')

total_points = true_counter * 10 + love_counter

if total_points < 10 or total_points > 90:
    print(f"Your score is {total_points}, you go tohether like coke and mentos.")
elif 40 < total_points < 50:
    print(f"Your score is {total_points}, you are alright together.")
else:
    print(f"Your score is {total_points}.")
    