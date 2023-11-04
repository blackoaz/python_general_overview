class Security:
    def __init__(self, password: str):
        # assert password.type == str
        self.password = password

    def create_password():
        pass

    def check_password(self):
        try:
            if isinstance (self.password, str):
                print(self.password)
                
        except TypeError:
            print('Wrong type inference')

security1 = Security(21)
print(security1.check_password())