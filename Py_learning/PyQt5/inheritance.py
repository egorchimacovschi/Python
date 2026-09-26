#a class inherits from another class


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Wooof")

class Cat(Animal):
    def speak(self):
        print("Meowww")

class Mouse(Animal):
    def speak(self):
        print("Squick")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

