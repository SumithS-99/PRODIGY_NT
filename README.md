# PRODIGY_NT
def encrypt(text, shift):
    result = ""
    
    # Loop through each character in the input text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabet characters are unchanged
    
    return result

def decrypt(text, shift):
    result = ""
    
    # Loop through each character in the input text
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabet characters are unchanged
    
    return result

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted = encrypt(message, shift)
    print(f"Encrypted message: {encrypted}")
    
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
