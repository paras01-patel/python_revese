# ython Object

# Object class ka instance hota hai.

# Simple words me:

# 👉 Class = Blueprint (Naksha)
# 👉 Object = Real Thing

# Real Life Example
# Class = Car
# Object = BMW, Audi, Tesla

# Car ek blueprint hai, lekin BMW aur Audi actual objects hain.

# Object Banana
# class Student:
#     pass

# s1 = Student()   # Object

# print(s1)

# Yaha s1 ek object hai jo Student class se bana hai.

# Object ke Through Data Access Karna
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

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Paras")
# s2 = Student("Rahul")
# s3 = Student("Aman")

# print(s1.name)
# print(s2.name)
# print(s3.name)

# Output:

# Paras
# Rahul
# Aman
# Object Method Call Karna
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Name:", self.name)

# s1 = Student("Paras")

# s1.display()

# Output:

# Name: Paras
# Object ki Type Check Karna
# class Student:
#     pass

# s1 = Student()

# print(type(s1))

# Output:

# <class '__main__.Student'>