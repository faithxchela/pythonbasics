# inheritance allows one class to inherit attributes
# and methods from another class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Bird(Animal):
    def speak(self):
        return "Chirp"


class Pig(Animal):
    def speak(self):
        return "Snort"


# this are objects
doggy = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Birdie")
pig = Pig("Piggie")
print(doggy.speak())
print(cat.speak())
print(bird.speak())
print(pig.speak())
