# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Smth")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("WTF! Raised!")

height = float(input("Height [m]: "))
weight = int(input("Weight [kg]: "))

if height > 3:
    raise ValueError("Height should not be over 3 meters.")

bmi = weight / height**2
print(bmi)

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ["Banana", "Apple", "Pear"]
# fruit = fruit_list[2137]

# TypeError
# text = "abc"
# print(text + 5)
