# Operators in Python

# Operators are used to perform operations on variables and values.

# 1. Arithmetic Operators
# Operator	Meaning
# +	Addition
# -	Subtraction
# *	Multiplication
# /	Division
# //	Floor Division
# %	Modulus (Remainder)
# **	Power
# Example
# a = 10
# b = 3

# print(a + b)   # 13
# print(a - b)   # 7
# print(a * b)   # 30
# print(a / b)   # 3.3333
# print(a // b)  # 3
# print(a % b)   # 1
# print(a ** b)  # 1000
# 2. Comparison Operators

# These operators return True or False.

# Operator	Meaning
# ==	Equal
# !=	Not Equal
# >	Greater Than
# <	Less Than
# >=	Greater Than or Equal
# <=	Less Than or Equal
# Example
# a = 10
# b = 20

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)

# Output

# False
# True
# False
# True
# 3. Assignment Operators
# x = 10

# x += 5
# print(x)   # 15

# x -= 2
# print(x)   # 13

# x *= 2
# print(x)   # 26
# 4. Logical Operators
# Operator	Meaning
# and	Both conditions True
# or	At least one True
# not	Reverse the result
# Example
# age = 20

# print(age > 18 and age < 25)
# print(age > 18 or age > 50)
# print(not(age > 18))
# 5. Membership Operators

# Used to check whether a value exists in a sequence.

# Example
# numbers = [10, 20, 30, 40]

# print(20 in numbers)
# print(50 in numbers)
# print(50 not in numbers)

# Output

# True
# False
# True
# 6. Identity Operators

# Checks whether two variables refer to the same object.

# Example
# a = [1, 2, 3]
# b = a

# print(a is b)
# print(a is not b)

# Output

# True
# False
# Practice Questions
# Question 1
# a = 15
# b = 4

# print(a // b)
# print(a % b)
# Question 2
# x = 5

# x += 10
# x *= 2

# print(x)
# Question 3
# a = 10
# b = 20

# print(a < b and b > 15)
# Interview Questions
# What is the difference between / and //?
# print(10 / 3)
# print(10 // 3)

# Output:

# 3.333333333
# 3
# / → Returns decimal value.
# // → Returns integer (floor value).
# What is % used for?

# It returns the remainder.

# print(10 % 3)