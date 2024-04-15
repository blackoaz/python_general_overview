from datetime import datetime
import json
import os

class AtmMachine:

    def __init__(self,first_name: str, last_name: str, email: str, id_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id_number = id_number
        self.account_number = ""

    @property
    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def create_account(self):
        filename = os.path.join('/Users/pauloakello/Desktop/paulo/python/database',"customers.json")
        try:
            with open(filename,'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"Customers":[]}
        new_customer = {"Created at":datetime.now().strftime("%d-%m-%Y %H:%M:%S"), 
                        "First Name":self.first_name, 
                        "Last Name":self.last_name,
                        "Email":self.email,
                        "Account Number": ''
                        }
        data["Customers"].append(new_customer)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2, sort_keys=True)
            

    def deposit_money(self):
        pass

    def check_balance(self):
        pass

    def change_password(self):
        pass

customer1 = AtmMachine('paulo', 'akello', 'paulo@mail.com')
customer2 = AtmMachine('paulo1', 'akello1', 'paulo@mail.com')
customer1.create_account()
customer2.create_account()