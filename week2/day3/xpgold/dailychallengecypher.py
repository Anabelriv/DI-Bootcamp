def caesar_cipher(text, shift):
    cypher_text = ""
    for letter in text:
        if letter.isalpha():
            shitf_amount = shift % 26
            if letter.isupper():
                cypher_letter = chr((ord(letter) - 65 + shitf_amount) % 26 + 65)
            else:
                cypher_letter = chr((ord(letter) - 97 + shitf_amount) % 26 + 97)
            cypher_text += cypher_letter
        else:
            cypher_letter += letter
    return cypher_text


def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ")
        if choice.lower() == "e":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift amount: "))
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice.lower() == "d":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift amount: "))
            decrypted_message = caesar_cipher(message, -shift)
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Inavlid choice. Please enter 'e' for encrypt or 'd' for decrypt. ")
            continue

        another = input("Do you want to encrypt or decrypt another message? (y/n): ")
        if another.lower() == "n":
            break


if __name__ == "__main__":
    main()
