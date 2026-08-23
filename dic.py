# Tuple in Python

# A Tuple is a collection of items stored in a single variable.

# Features of Tuple
# Ordered ✅
# Immutable (cannot be changed) ✅
# Allows duplicate values ✅
# Faster than List ✅
# Creating a Tuple
# numbers = (10, 20, 30, 40)

# print(numbers)
# print(type(numbers))

# Output

# (10, 20, 30, 40)
# <class 'tuple'>
# Accessing Elements
# numbers = (10, 20, 30, 40)

# print(numbers[0])
# print(numbers[2])

# Output

# 10
# 30
# Negative Indexing
# numbers = (10, 20, 30, 40)

# print(numbers[-1])
# print(numbers[-2])

# Output

# 40
# 30
# Tuple is Immutable

# ❌ Not Allowed

# numbers = (10, 20, 30)

# numbers[1] = 100

# Error

# TypeError: 'tuple' object does not support item assignment
# Single Element Tuple

# ❌ Wrong

# t = (10)

# print(type(t))

# Output:

# <class 'int'>

# ✅ Correct

# t = (10,)

# print(type(t))

# Output:

# <class 'tuple'>
# Tuple Packing
# student = ("Paras", 21, "BCA")

# print(student)
# Tuple Unpacking
# student = ("Paras", 21, "BCA")

# name, age, course = student

# print(name)
# print(age)
# print(course)

# Output

# Paras
# 21
# BCA
# Length of Tuple
# numbers = (10, 20, 30, 40)

# print(len(numbers))

# Output

# 4
# Traversing a Tuple
# numbers = (10, 20, 30, 40)

# for i in numbers:
#     print(i)
# Slicing
# numbers = (10, 20, 30, 40, 50)

# print(numbers[1:4])

# Output

# (20, 30, 40)
# Count Method

# Counts occurrences of a value.

# numbers = (10, 20, 20, 30, 20)

# print(numbers.count(20))

# Output

# 3
# Index Method

# Returns the index of a value.

# numbers = (10, 20, 30, 40)

# print(numbers.index(30))

# Output

# 2
# Convert Tuple to List
# numbers = (10, 20, 30)

# numbers = list(numbers)

# numbers.append(40)

# print(numbers)

# Output

# [10, 20, 30, 40]
# Convert List to Tuple
# numbers = [10, 20, 30, 40]

# numbers = tuple(numbers)

# print(numbers)

# Output

# (10, 20, 30, 40)
# Interview Questions
# Difference Between List and Tuple
# List	Tuple
# Mutable	Immutable
# Uses []	Uses ()
# Slower	Faster
# More Methods	Fewer Methods
# When Should We Use Tuple?

# Use a tuple when data should not change.

# Examples:

# Student records
# Coordinates (x, y)
# Database records
# Fixed configuration values
# Practice Questions
# 1. Find the Length of a Tuple
# t = (10, 20, 30, 40, 50)
# 2. Count How Many Times 20 Appears
# t = (10, 20, 20, 30, 20)
# 3. Convert a Tuple into a List
# t = (1, 2, 3, 4)
# 4. Find the Largest Element
# # t = (10, 50, 30, 70, 20)