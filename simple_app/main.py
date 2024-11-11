#!/usr/bin/env python3
from check_password import create_password, check_password

def login():
    trial_count = 0
    max_attempts = 3
    while trial_count < max_attempts:
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")
        if check_password(username, password):
            print("Login successful")
            return True
        else:
            trial_count += 1
            print("Username or password is incorrect.")
            print(f"Trial count: {trial_count}")
            if trial_count >= max_attempts:
                print("Maximum login attempts reached.")
                return False
    return False


def create_account():
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ")
    create_password(username, password)


def main():
    print("******\t Welcome to Simple Login System\t ******")
    print("")
    print("Do you have an account with us?")
    print("\n1. Yes\n2. No")
    try:
        input_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return main()

    if input_choice == 1:
        if login():
            print("Welcome back!")
        else:
            print("Login failed. Please try again later.")
    elif input_choice == 2:
        create_account()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()
        
if __name__ == "__main__":
    main()
    
