import sys
import os
from cryptography.fernet import Fernet

SECRET_KEY = 'YOUR-KEY'

def encrypt_file(input_file):
    cipher_suite = Fernet(SECRET_KEY.encode())

    with open(input_file, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    output_file = input_file.replace('.txt', '.mk1')

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
    
    print(f'File encrypted and saved as {output_file}')

def decrypt_file(input_file):
    cipher_suite = Fernet(SECRET_KEY.encode())

    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    filename, _ = os.path.splitext(input_file)
    output_file = f"{filename}.txt"

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
    
    print(f'File decrypted and saved as {output_file}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("For encryption: secretmk1.exe enc <input_file>")
        print("For decryption: secretmk1.exe dec <input_file>")
        sys.exit(1)
    
    action = sys.argv[1]
    input_file = sys.argv[2]

    if action == "enc":
        encrypt_file(input_file)
    elif action == "dec":
        decrypt_file(input_file)
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
