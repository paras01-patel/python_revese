# Variables and Data Types in Python
# 1. Variables

# A variable is used to store data in memory.

# Syntax
# variable_name = value
# Example
# name = "Paras"
# age = 21
# city = "Bhopal"

# print(name)
# print(age)
# print(city)

# Output

# Paras
# 21
# Bhopal
# Rules for Variable Names

# ✅ Valid

# name = "Paras"
# _age = 21
# student1 = "BCA"

# ❌ Invalid

# 1name = "Paras"    # Cannot start with a number
# my-name = "Paras"  # Hyphen not allowed
# Data Types

# A Data Type defines the type of value stored in a variable.

# 1. Integer (int)

# Stores whole numbers.

# age = 21
# marks = 95

# print(age)
# print(type(age))

# Output

# 21
# <class 'int'>
# 2. Float (float)

# Stores decimal numbers.

# price = 99.99
# height = 5.8

# print(price)
# print(type(price))

# Output

# 99.99
# <class 'float'>
# 3. String (str)

# Stores text.

# name = "Paras"

# print(name)
# print(type(name))

# Output

# Paras
# <class 'str'>
# 4. Boolean (bool)

# Stores True or False.

# is_student = True

# print(is_student)
# print(type(is_student))

# Output

# True
# <class 'bool'>
# 5. List (list)

# Stores multiple values and can be changed.

# numbers = [10, 20, 30, 40]

# print(numbers)
# print(type(numbers))

# Output

# [10, 20, 30, 40]
# <class 'list'>
# Accessing List Elements
# numbers = [10, 20, 30, 40]

# print(numbers[0])
# print(numbers[2])

# Output

# 10
# 30
# 6. Tuple (tuple)

# Similar to a list but cannot be modified.

# data = (10, 20, 30)

# print(data)
# print(type(data))

# Output

# (10, 20, 30)
# <class 'tuple'>
# 7. Set (set)

# Stores unique values only.

# nums = {1, 2, 3, 3, 4}

# print(nums)
# print(type(nums))

# Output

# {1, 2, 3, 4}
# <class 'set'>

# Notice that duplicate 3 is removed.

# 8. Dictionary (dict)

# Stores data in key-value pairs.

# student = {
#     "name": "Paras",
#     "age": 21,
#     "course": "BCA"
# }

# print(student)
# print(type(student))

# Output

# {'name': 'Paras', 'age': 21, 'course': 'BCA'}
# <class 'dict'>
# Accessing Dictionary Values
# student = {
#     "name": "Paras",
#     "age": 21
# }

# print(student["name"])
# print(student["age"])

# Output

# Paras
# 21
# Type Conversion
# Integer to String
# age = 21

# age_str = str(age)

# print(age_str)
# print(type(age_str))
# String to Integer
# num = "100"

# num_int = int(num)

# print(num_int)
# print(type(num_int))