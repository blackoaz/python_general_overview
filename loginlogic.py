def checkpassword(input_pin):
    saved_pin = 1234
    if input_pin == saved_pin:
        return True
    else:
        return False
    
def enterpassword():
    i = 0
    while i < 3:
        input_pin = eval(input("Enter your pin: "))
        password = checkpassword(input_pin)
        if password:
            print("User successfully logged in")
            break
        else:
            print("Wrong password")
        i += 1
    return password

def choice_made(choice):
    print("you have selected choice {}".format(choice))

def system_menu():
    print("\t\t*** WELCOME TO POA BANK ***")
    print("--------------------SERVICES------------------------")
    print("\t\t1.Register with us\n\t\t2.Withdraw Money\n\t\t3.Check Balance")
    choice = eval(input("Select a service by typing e.g 1, 2 ...: "))

    choice_made(choice)


def main():
    is_logged_in = enterpassword()
    if is_logged_in:
        print("Welcome back")
        system_menu()
    else:
        print("Too many attempts, User blocked")

main()