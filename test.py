# from base64 import b64encode
# import random

# hello = 'Hello world'.encode('utf-8')
# print(hello.decode('utf-8'))
# v1 = b64encode(hello).decode('utf-8')
# print(v1)

# number = random.randint(2,20)
# n = number // 2 + 1

# print(n)
# # pow()
# asc = ord('h')
# aschr = chr(asc)
# print(asc)
# print(aschr)

# https://www.ic.unicamp.br/~rdahab/cursos/mo421-mc889/Welcome_files/Stinson-Paterson_CryptographyTheoryAndPractice-CRC%20Press%20%282019%29.pdf

class Animal:
    def __init__(self, name: str, cry: str):
        self.name = name
        self.cry = cry

class Dog(Animal):
    def __init__(self,name: str, cry: str, age: int):
        super().__init__(name, cry)
        self.age = age
    def dog_details(self):
        print(f"{self.name} - {self.cry} - {self.age}")             

dog1 = Dog("Max","Bark", 2 )

dog1.dog_details()

