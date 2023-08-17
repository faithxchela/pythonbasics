
class Students:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sayhello(self):
        print("My name is ", self.name, "I'm ", self.age, "years ", self.gender)


myobje = Students("Faith", "Female", 19)
myobje = Students("Peter", "Male", 23)
myobje = Students("Farida", "Female", 18)
myobje = Students("John", "Male", 30)
myobje.sayhello()
