fruits = ["Apple", "Pear", "Orange"]  # eval(input())


def make_pie(index: int):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
