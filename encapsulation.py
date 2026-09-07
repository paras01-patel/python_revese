# Encapsulation in Python

# Encapsulation ka matlab hai data (variables) aur methods (functions) ko ek class ke andar rakhna aur data ko direct access se protect karna.

# Simple words me:

# 👉 User data ko direct change na kar sake.
# 👉 Data ko methods ke through access karo.

# Without Encapsulation
# class Student:
#     def __init__(self):
#         self.marks = 90

# s = Student()

# print(s.marks)

# s.marks = -100

# print(s.marks)

# Output:

# 90
# -100

# Yaha koi bhi marks ko galat value de sakta hai.

# With Encapsulation

# Private variable ke liye __ (double underscore) lagate hain.

# class Student:

#     def __init__(self):
#         self.__marks = 90

#     def get_marks(self):
#         return self.__marks

# s = Student()

# print(s.get_marks())

# Output:

# 90
# Direct Access Karne Par Error
# class Student:

#     def __init__(self):
#         self.__marks = 90

# s = Student()

# print(s.__marks)

# Output:

# AttributeError

# Kyunki __marks private hai.

# Getter and Setter Example
# class Student:

#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid Marks")

#     def get_marks(self):
#         return self.__marks

# s = Student()

# s.set_marks(85)

# print(s.get_marks())

# Output:

# 85