# Loops in Python (for and while)

# A loop is used to execute a block of code repeatedly.

# 1. for Loop

# Used when you know how many times the loop should run.

# Syntax
# for variable in sequence:
#     statement
# Example 1
# for i in range(5):
#     print(i)

# Output

# 0
# 1
# 2
# 3
# 4
# Example 2: Print 1 to 5
# for i in range(1, 6):
#     print(i)

# Output

# 1
# 2
# 3
# 4
# 5
# Example 3: Print a List
# numbers = [10, 20, 30, 40]

# for i in numbers:
#     print(i)

# Output

# 10
# 20
# 30
# 40
# 2. while Loop

# Used when you don't know exactly how many times the loop will run.

# Syntax
# while condition:
#     statement
# Example
# i = 1

# while i <= 5:
#     print(i)
#     i += 1

# Output

# 1
# 2
# 3
# 4
# 5
# 3. break Statement

# Stops the loop immediately.

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# Output

# 1
# 2
# 3
# 4
# 4. continue Statement

# Skips the current iteration.

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# Output

# 1
# 2
# 4
# 5
# 5. pass Statement

# Placeholder for future code.

# for i in range(5):
#     pass
# Common Interview Programs
# Print Table of 5
# num = 5

# for i in range(1, 11):
#     print(num * i)
# Sum of First 10 Numbers
# sum = 0

# for i in range(1, 11):
#     sum += i

# print(sum)

# Output

# 55
# Count Even Numbers
# count = 0

# for i in range(1, 11):
#     if i % 2 == 0:
#         count += 1

# print(count)

# Output

# 5
# Pattern Questions
# Pattern 1
# for i in range(5):
#     print("*")

# Output:

# *
# *
# *
# *
# *
# Pattern 2
# for i in range(1, 6):
#     print("*" * i)

# Output:

# *
# **
# ***
# ****
# *****
# Nested Loop
# for i in range(3):
#     for j in range(3):
#         print(i, j)

# Output

# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# Time Complexity Connection
# for i in range(n):
#     print(i)

# ➡️ Runs n times → O(n)

# for i in range(n):
#     for j in range(n):
#         print(i, j)