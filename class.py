# Python Class

# Class ek blueprint (naksha) hoti hai jisse objects banaye jate hain.

# Real Life Example:

# Class = Student
# Object = Paras, Rahul, Aman

# Sab students ke paas name, age, roll_no ho sakta hai, isliye pehle class banate hain.

# Simple Class
# class Student:
#     pass

# s1 = Student()

# print(type(s1))

# Output:

# <class '__main__.Student'>
# Class with Attributes
# class Student:
#     name = "Paras"
#     age = 21

# s1 = Student()

# print(s1.name)
# print(s1.age)

# Output:

# Paras
# 21
# Constructor (__init__)

# Object create hote hi automatically call hota hai.

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Paras", 21)

# print(s1.name)
# print(s1.age)

# Output:

# Paras
# 21
# Multiple Objects
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Paras", 21)
# s2 = Student("Rahul", 22)

# print(s1.name)
# print(s2.name)

# Output:

# Paras
# Rahul
# Class Method
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Name:", self.name)

# s1 = Student("Paras")
# s1.display()

# Output:

# Name: Paras
# self Kya Hota Hai?

# self current object ko refer karta hai.

# class Test:

#     def show(self):
#         print("Hello")

# t = Test()
# t.show()

# Python internally:

# Test.show(t)