# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["key"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Smth")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was close.")




# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ["Banana", "Apple", "Pear"]
# fruit = fruit_list[2137]

# TypeError
# text = "abc"
# print(text + 5)
