class Animal:
    name = "Eranko"

    def move(self):
        print("Animal moves!")


mammals = Animal()
aves = Animal()
pisces = Animal()

print(mammals)
print(aves)

mammals.name = "Dog"   #This is a form of setting

aves.name = "Bird"

print(mammals.name)     #This is a form of getting

print(aves.name)

print(pisces.name)

#methods are functions declared in a class
#when methods are called on an object,
# the object implicitly passes itself as a parameter of that method,
#To prevent this error, pass in "self" as the parameter of that method before calling it on an object
#For example: aves.move is implicitly move(aves) if "self" is not passed in.

class Student:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return f"Object name is {self.name} and age is {self.age}"


student1 = Student("Adewale", 56)
print(student1.name)
print(student1.age)
print(student1)


