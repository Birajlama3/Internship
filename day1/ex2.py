class MyClass:
    x = 5
    y =10
suvam = MyClass()
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
print(suvam.y)
print(obj1.x)
print(obj2.x)
print(obj3.x)

#__init__method --> used to assign values to object properties.
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def printname(self):
        print(self.name,self.age)
p1 = Person("Biraj", 22)
print(p1.name)
print(p1.age)

class Class2:
    def calculate(self,a,b):
        return a * b
c1 = Class2()
print(c1.calculate(3,4))

class Student(Person): #inheritance of class Person
    pass
x = Student("Nabin", 23)
x.printname()

#Encapsulation
class Cars:
    def __init__(self,name,model):
        self.name = name
        self.__model = model #Private property.

    def get_model(self):
        return self.__model
car1 = Cars("BMW",2026)
print(car1.get_model())
