# Star Pattern Questions in Python
# 1. Square Pattern
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# Output:

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# 2. Right Triangle
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Output:

# *
# * *
# * * *
# * * * *
# * * * * *
# 3. Inverted Triangle
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Output:

# * * * * *
# * * * *
# * * *
# * *
# *
# 4. Pyramid Pattern
# for i in range(1, 6):
#     print(" " * (5 - i), end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()

# Output:

#     *
#    ***
#   *****
#  *******
# *********
# 5. Inverted Pyramid
# for i in range(5, 0, -1):
#     print(" " * (5 - i), end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()

# Output:

# *********
#  *******
#   *****
#    ***
#     *
# 6. Diamond Pattern
# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))

# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))

# Output:

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *