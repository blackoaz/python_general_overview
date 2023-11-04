import os
def say_hello ():
    with open('name.txt', 'w') as file:
        file.writelines('Hello peopele I hope everyone is fine\nallow me to pass my greetings to everyone\ntoday is a good day as we gather here to celebrate the gift of life\nhave a good day everybody')

say_hello()