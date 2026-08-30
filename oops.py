# OOPS (Object Oriented Programming System)

# OOPS ek programming concept hai jisme hum objects aur classes ka use karke programs banate hain.

# Python me OOPS ke 4 main pillars hote hain:

# Class
# Object
# Inheritance
# Polymorphism
# Encapsulation
# Abstraction
# 1. Class

# Class ek blueprint hoti hai.

# class Student:
#     pass
# 2. Object

# Object class ka instance hota hai.

# class Student:
#     pass

# s1 = Student()

# print(type(s1))
# 3. Constructor (__init__)

# Object create hote hi automatically call hota hai.

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Paras", 21)

# print(s1.name)
# print(s1.age)
# 4. Inheritance

# Ek class dusri class ki properties use kar sakti hai.

# class Animal:

#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     pass

# d = Dog()
# d.sound()
# 5. Polymorphism

# Same method alag-alag behavior dikha sakti hai.

# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# d = Dog()
# c = Cat()

# d.sound()
# c.sound()
# 6. Encapsulation

# Data ko secure rakhna.

# class Student:

#     def __init__(self):
#         self.__marks = 90

# s = Student()

# # print(s.__marks)  # Error
# 7. Abstraction

# Sirf important details dikhana, implementation hide karna.

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):

#     def start(self):
#         print("Car Started")

# c = Car()
# c.start()
# Real-Life Example
# Class → Car
# Object → BMW, Audi, Tesla
# Inheritance → ElectricCar inherits Car
# Polymorphism → Different cars have different start methods
# Encapsulation → Engine details hidden
# Abstraction → User sirf Start button use karta hai