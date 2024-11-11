from check_password import create_password, check_password

def main():
    print("******\t Welcome to Simple Login System\t ******")
    print("")
    print("Do you want to login or register?")
    print("\n1. Login\n2. Register")
    input_choice = int(input("Enter your choice: "))
    if input_choice == 1:
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")
        if check_password(username, password):
            print("Login successful")
        else:
            print("Username or password is incorrect")
    elif input_choice == 2:
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")
        create_password(password, username)



if __name__ == "__main__":
    main()
    
