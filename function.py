# Functions in Python

# A function is a block of code that performs a specific task and can be reused multiple times.

# Instead of writing the same code again and again, we put it inside a function.

# Why Use Functions?

# ✅ Code Reusability
# ✅ Better Readability
# ✅ Easier Debugging
# ✅ Used in Django, APIs, DSA, and Interviews

# Creating a Function
# Syntax
# def function_name():
#     # code
# Example
# def greet():
#     print("Hello Paras")

# greet()

# Output

# Hello Paras
# Function with Parameters

# Parameters are values passed to a function.

# def greet(name):
#     print("Hello", name)

# greet("Paras")
# greet("Rahul")

# Output

# Hello Paras
# Hello Rahul
# Function with Multiple Parameters
# def add(a, b):
#     print(a + b)

# add(10, 20)

# Output

# 30
# Return Statement

# return sends a value back from a function.

# def add(a, b):
#     return a + b

# result = add(10, 20)

# print(result)

# Output

# 30
# Difference Between print() and return
# Using Print
# def add(a, b):
#     print(a + b)

# x = add(10, 20)

# print(x)

# Output:

# 30
# None
# Using Return
# def add(a, b):
#     return a + b

# x = add(10, 20)

# print(x)

# Output:

# 30

# Interview Question:
# return gives the value back, while print only displays it.

# Default Parameters
# def greet(name="Guest"):
#     print("Hello", name)

# greet()
# greet("Paras")

# Output

# Hello Guest
# Hello Paras
# Keyword Arguments
# def student(name, age):
#     print(name, age)

# student(age=21, name="Paras")
# Function to Check Even or Odd
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     return "Odd"

# print(even_odd(7))

# Output

# Odd
# Function to Find Largest Number
# def largest(a, b):
#     if a > b:
#         return a
#     return b

# print(largest(20, 15))

# Output

# 20
# Function with List
# def total(numbers):
#     return sum(numbers)

# nums = [10, 20, 30, 40]

# print(total(nums))

# Output

# 100
# Scope of Variables
# Local Variable
# def test():
#     x = 10
#     print(x)

# test()

# x exists only inside the function.

# Global Variable
# x = 100

# def test():
#     print(x)

# test()

# Output:

# 100
# Interview Questions
# Q1. What is a Function?

# A function is a reusable block of code that performs a specific task.

# Q2. Why do we use Functions?
# Reusability
# Modularity
# Better code organization
# Q3. Difference between Parameter and Argument?
# def greet(name):   # Parameter
#     print(name)

# greet("Paras")     # Argument
# Practice Questions
# 1. Create a function to find the square of a number.
# square(5)

# Output:

# 25
# 2. Create a function to find the factorial of a number.
# factorial(5)

# Output:

# 120