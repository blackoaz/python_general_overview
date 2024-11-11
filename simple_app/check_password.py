import hashlib
import os
import json
from pathlib import Path
from cryptography.fernet import Fernet

file_path = Path(__file__).resolve().parent / 'passwords.json'
key_path = Path(__file__).resolve().parent / 'secret.key'


def load_key():
    """Loads the encryption key, generating a new one if necessary."""
    if key_path.exists():
        return key_path.read_bytes()
    else:
        key = Fernet.generate_key()
        key_path.write_bytes(key)
        return key


# Initialize encryption cipher with the loaded key
key = load_key()
cipher_suite = Fernet(key)


def encrypt_file(file_path: Path):
    """Encrypts the specified file."""
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(file_path: Path):
    """Decrypts the specified file."""
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)


def create_password(username: str, password_input: str):
    """Creates a new user with a securely hashed password."""
    salt = os.urandom(32)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256', password_input.encode('utf-8'), salt, iterations=100000
    ).hex()
    user_data = {username: {"password": password_hash, "salt": salt.hex()}}

    # Load existing users or create new file
    if file_path.exists():
        decrypt_file(file_path)
        with open(file_path, 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

            if username in data:
                print("Username already exists.")
                encrypt_file(file_path)
                return

            data.update(user_data)

            # Save updated data and re-encrypt
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        encrypt_file(file_path)
    else:
        with open(file_path, 'w') as file:
            json.dump(user_data, file, indent=4)
        encrypt_file(file_path)

    print(f"Account created successfully for {username}.")


def check_password(username: str, password_input: str) -> bool:
    """Verifies if the provided password matches the stored password for the user."""
    if not file_path.exists():
        print("No users found.")
        return False

    decrypt_file(file_path)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            user_data = data.get(username)
            if not user_data:
                print("Username not found.")
                return False

            salt = bytes.fromhex(user_data['salt'])
            password_hash = hashlib.pbkdf2_hmac(
                'sha256', password_input.encode('utf-8'), salt, iterations=100000
            ).hex()

            return password_hash == user_data['password']
    finally:
        encrypt_file(file_path)
