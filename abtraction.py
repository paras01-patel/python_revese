# 2. Abstraction in Python

# Abstraction ka matlab hai sirf important cheeze user ko dikhana aur internal implementation ko hide karna.

# Simple words me:

# 👉 User ko "kya karna hai" pata hota hai.
# 👉 "Kaise ho raha hai" ye hidden rehta hai.

# Real Life Example
# Car

# Jab aap car start karte ho:

# Start Button Press
#       ↓
# Car Start

# Engine ke andar fuel kaise ja raha hai, spark kaise ho raha hai, ye sab hidden hai.

# Yehi Abstraction hai.

# Abstract Class Example
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

# Output:

# Car Started
# Abstract Method
# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):

#     def area(self):
#         print("Area = side * side")

# s = Square()
# s.area()

# Output:

# Area = side * side
# Kya Hota Hai Yaha?
# ABC = Abstract Base Class
# @abstractmethod = Abstract Method
# Abstract method ka body nahi hota.
# Child class ko method implement karna hi padta hai.
# Error Example
# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

# v = Vehicle()

# Output:

# TypeError:
# Can't instantiate abstract class Vehicle