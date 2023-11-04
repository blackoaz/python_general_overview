from datetime import datetime
import json

class AtmMachine():

    def __init__(self,first_name: str, last_name: str, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def create_account(self):
        filename = "customers.json"
        print(filename)
        data = [{"Customers":{"Created at":datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "First Name":self.first_name, "Last Name":self.last_name,"Email":self.email}}]
        with open(filename, 'w+') as file:
            json.dump(data, file, indent=2, sort_keys=True)
            

    def deposit_money():
        pass

    def check_balance():
        pass

    def change_password():
        pass

customer1 = AtmMachine('paulo', 'akello', 'paulo@mail.com')
customer2 = AtmMachine('paulo1', 'akello1', 'paulo@mail.com')
customer1.create_account()
customer2.create_account()