class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Animal is making a sound")


# TODO: Create the Dog and Cat classes with make_sound method
class Dog(Animal):

    def make_sound(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):

    def make_sound(self):
        print(f"{self.name} says: Meow!")


# TODO: Create a common interface that takes any object of type Animal (or its subclasses) and calls their make_sound method
def make_sound(animal : Animal):
    animal.make_sound()

# Do not change the code below
animal = Animal("Rabbit")
make_sound(animal)

animal = Dog("Buddy")
make_sound(animal)

animal = Cat("Whiskers")
make_sound(animal)
