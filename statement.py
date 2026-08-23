# Conditional Statements (if, elif, else)

# Conditional statements are used to make decisions in a program.

# 1. if Statement

# Executes a block of code only if the condition is True.

# Syntax
# if condition:
#     statement
# Example
# age = 20

# if age >= 18:
#     print("You can vote")

# Output

# You can vote
# 2. if-else Statement

# If the condition is True, the if block runs; otherwise, the else block runs.

# Example
# age = 16

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# Output

# You cannot vote
# 3. if-elif-else Statement

# Used when there are multiple conditions.

# Example
# marks = 75

# if marks >= 90:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")

# Output

# Grade B
# 4. Nested if

# An if statement inside another if.

# Example
# age = 20
# has_license = True

# if age >= 18:
#     if has_license:
#         print("You can drive")
#     else:
#         print("Get a license first")
# else:
#     print("You are underage")
# 5. Using Logical Operators
# Example
# age = 22

# if age >= 18 and age <= 25:
#     print("Eligible")
# Even or Odd Program
# num = 7

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Output

# Odd
# Positive, Negative, or Zero
# num = -5

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
# Largest of Two Numbers
# a = 10
# b = 20

# if a > b:
#     print(a)
# else:
#     print(b)
# Largest of Three Numbers
# a = 10
# b = 25
# c = 15

# if a > b and a > c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)
# Interview Questions
# Difference between if and elif
# marks = 85

# if marks >= 50:
#     print("Pass")

# if marks >= 80:
#     print("Excellent")

# Both if statements can run.

# marks = 85

# if marks >= 80:
#     print("Excellent")
# elif marks >= 50:
#     print("Pass")

# Only one block runs in if-elif-else.

# Practice Questions
# 1. Check whether a number is divisible by 5.
# num = 25
# 2. Check whether a person is eligible to vote.
# age = 17
# 3. Find the largest of three numbers.
# a = 45
# b = 78
# c = 23
# 4. Check whether a year is a leap year.
# year = 2024