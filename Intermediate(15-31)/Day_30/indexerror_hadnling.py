fruits = ["Apple", "Pear", "Orange"]  # eval(input())


def make_pie(index: int):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")


make_pie(4)
