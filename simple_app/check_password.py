import hashlib
import os
import json
from pathlib import Path

def create_password(password_input: str, username: str):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password_input.encode('utf-8'), salt, 100000)
    
    # Load existing data or initialize with an empty dictionary
    file_path = Path('./passwords.json')
    try:
        with open(file_path, 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
                
            # Check if the username already exists
            if username in data:
                print("Username already exists")
                return

            # Add the new user's password hash and salt
            data[username] = {
                'password': key.hex(),
                'salt': salt.hex()
            }
            
            # Write the updated data back to the file
            file.seek(0)
            json.dump(data, file, indent=4, sort_keys=True)
            file.truncate() # Remove any remaining data

            print(salt)
            print(key)
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            data = {
                username: {
                    'password': key.hex(),
                    'salt': salt.hex()
                }
            }
            json.dump(data, file, indent=4, sort_keys=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

def check_password(username: str, password_input: str):
     try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
            if username in data:
                user_data = data[username]
                salt = bytes.fromhex(user_data['salt'])
                key = hashlib.pbkdf2_hmac('sha256', password_input.encode('utf-8'), salt, 100000)
                if key.hex() == user_data['password']:
                    return True
                else:
                    return False
            else:
                print("Username not found")
                return False
     except FileNotFoundError:
        print("No users found")
        return False