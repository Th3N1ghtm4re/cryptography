import sys, os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print("Key:", key.decode())
    return key

def encrypt_file(input_file):
    key = generate_key()
    cipher_suite = Fernet(key)

    with open(input_file, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    output_file = input_file.replace('.txt', '.enc')

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
    
    print(f'File encrypted and saved as {output_file}')

def decrypt_file(input_file, key):
    cipher_suite = Fernet(key)

    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    filename, _ = os.path.splitext(input_file)
    output_file = f"{filename}.txt"

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
    
    print(f'File decrypted and saved as {output_file}')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("For encryption: CRYPT.py enc <input_file>")
        print("For decryption: CRYPT.py dec <input_file> <key>")
        sys.exit(1)
    
    action = sys.argv[1]
    input_file = sys.argv[2]

    if action == "enc":
        encrypt_file(input_file)
    elif action == "dec":
        if len(sys.argv) != 4:
            print("For decryption, you need to provide the key.")
            sys.exit(1)
        key = sys.argv[3].encode()
        decrypt_file(input_file, key)
    else:
        print("Invalid action. Use 'enc' or 'dec'.")
