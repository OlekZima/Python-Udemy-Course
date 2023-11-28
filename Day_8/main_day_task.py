from string import ascii_lowercase
from caeser_cipher import logo

def caesar_cipher(text: str, shift: int, encrypt=True):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if not char.isalpha():
            encrypted_text += char
            continue
        index = ascii_lowercase.index(char)
        new_letter_index = (index + shift) if encrypt else (index - shift)
        if new_letter_index >= len(ascii_lowercase):
            new_letter_index %= len(ascii_lowercase)
        encrypted_text += ascii_lowercase[new_letter_index]
    else:
        return encrypted_text

# print(len(ascii_lowercase))

if __name__ == "__main__":
    print(logo)

    is_continue = True
    while is_continue:
            
        encode = input("Encode or decore?\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if encode.lower() == "encode":
            print(f"Your encoded message is: {caesar_cipher(text, shift)}")
        elif encode.lower() == "decode":
            print(f"Your decoded message is: {caesar_cipher(text, shift, encrypt=False)}")

        user_continue = input("Do you want to restart the program? yesr or no\n").lower()
        is_continue = True if user_continue == "yes" else False