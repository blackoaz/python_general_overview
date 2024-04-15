import sys
import bcrypt

class Security:
    def __init__(self, password: str):
        assert isinstance(password, str), 'Password must be a string'
        self.password = password

    def create_password(self):
        salt  = bcrypt.gensalt()
        password_bytes = self.password.encode('utf-8')
        hashed = bcrypt.hashpw(password_bytes, salt).decode()
        print("The salt is: ", salt)
        print("The hashed password:", hashed)

    def check_password(self):
        try:
            if isinstance(self.password, str):
                return self.password
        except TypeError:
            print('Wrong type inference')
            sys.exit(1)

# Create an instance of Security with a string password
security1 = Security("Hello paulo 222")

# Call check_password and print the result
print(security1.check_password())
security1.create_password()
