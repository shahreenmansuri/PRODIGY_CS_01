def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if choice == 'e':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        continue_choice = input("Do you want to encrypt/decrypt another message? (y/n): ").lower()
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()
