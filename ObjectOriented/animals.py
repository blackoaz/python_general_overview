class Animal:
    animalage = 0

    def __init__(self,sound: str,legs: int):
        self.legs = legs
        self.sound = sound

    def __str__(self)-> str:
        return f"This animal {self.sound} and has {self.legs} legs"
    
class Goat(Animal):

    def __init__(self, sound: str, legs: int):
        super().__init__(sound, legs)
    
    def __str__(self) -> str:
        return f"A goat {self.sound}'s and has {self.legs} legs"

def main():

    my_animal = Goat('bleet',4)
    print(my_animal)

main()
