class Animal:
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Prey(Animal):
    def flee(self):
        print("This animal is hunting")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabitt(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabitt()
hawk = Hawk()
fish = Fish()