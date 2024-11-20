def caesar_cipher(text, shift, mode='encrypt'):
    result = []

    # Ensure shift is a positive integer
    shift = shift % 26

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            # Determine the starting point for the shift (uppercase or lowercase)
            start = ord('A') if char.isupper() else ord('a')
            
            if mode == 'encrypt':
                # For encryption, shift forward
                shifted_char = chr(start + (ord(char) - start + shift) % 26)
            elif mode == 'decrypt':
                # For decryption, shift backward
                shifted_char = chr(start + (ord(char) - start - shift) % 26)
            
            result.append(shifted_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)

    return ''.join(result)

def main():
    print("Caesar Cipher Encryption and Decryption")

    # Ask the user for input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (integer): "))
    
    # Encrypt the message
    encrypted_message = caesar_cipher(message, shift, mode='encrypt')
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

