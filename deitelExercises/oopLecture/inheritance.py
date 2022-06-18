class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speak"


class Dog(Animal):
    def __init__(self, name, type_):
        super().__init__(name)
        self.type = type_

    def speak(self):
        super().speak()
        return "Dog barks"


class Cat(Animal):
    pass


dog = Dog("Bingo", "Rottweiler")
cat = Cat("Kitty")
print(dog.speak())
print(dog.name)
print(dog.type)
print(cat.name)
