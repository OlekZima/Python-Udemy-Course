from string import ascii_lowercase

def caesar_cipher(text: str, shift: int, encrypt=True):
    text = text.lower()
    encrypted_text = ""
    for letter in text:
        index = ascii_lowercase.index(letter)
        new_letter_index = (index + shift) if encrypt else (index - shift)
        if new_letter_index >= len(ascii_lowercase):
            new_letter_index -= len(ascii_lowercase)
        encrypted_text += ascii_lowercase[new_letter_index]
    else:
        return encrypted_text

def encrypt(text: str, shift: int):
    text = text.lower()
    encrypted_text = ""
    for letter in text:
        index = ascii_lowercase.index(letter)
        new_letter_index = index + shift
        if new_letter_index >= len(ascii_lowercase):
            new_letter_index = new_letter_index - len(ascii_lowercase)
        encrypted_text += ascii_lowercase[new_letter_index]
    else:
        return encrypted_text
    

# print(len(ascii_lowercase))

if __name__ == "__main__":
    encode = input("Encode or decore?\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if encode.lower() == "encode":
        print(caesar_cipher(text, shift))
    elif encode.lower() == "decode":
        print(caesar_cipher(text, shift, encrypt=False))

