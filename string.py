# Python String

# String characters (letters, numbers, symbols) ka collection hoti hai jo quotes ("" ya '') ke andar likhi jati hai.

# name = "Paras"
# city = 'Indore'
# String Create Karna
# name = "Paras"

# print(name)

# Output:

# Paras
# Indexing

# String ka har character ek index par hota hai.

# name = "Python"

# print(name[0])
# print(name[1])
# print(name[5])

# Output:

# P
# y
# n
# Negative Indexing
# name = "Python"

# print(name[-1])
# print(name[-2])

# Output:

# n
# o
# String Slicing
# name = "Python"

# print(name[0:3])
# print(name[2:5])

# Output:

# Pyt
# tho
# String Concatenation

# Do strings ko jodna.

# first = "Paras"
# last = "Chandrawanshi"

# print(first + " " + last)

# Output:

# Paras Chandrawanshi
# String Repetition
# print("Hi " * 3)

# Output:

# Hi Hi Hi
# Important String Methods
# Upper Case
# name = "paras"
# print(name.upper())

# Output:

# PARAS
# Lower Case
# name = "PARAS"
# print(name.lower())

# Output:

# paras
# Capitalize
# name = "paras"
# print(name.capitalize())

# Output:

# Paras
# Replace
# text = "I like Java"

# print(text.replace("Java", "Python"))

# Output:

# I like Python
# Find
# text = "Hello Python"

# print(text.find("Python"))

# Output:

# 6
# String Loop
# name = "Paras"

# for ch in name:
#     print(ch)

# Output:

# P
# a
# r
# a
# s
# String Length
# name = "Paras"

# print(len(name))

# Output:

# 5
# String Sorting
# s = "dcba"

# print(sorted(s))

# Output:

# ['a', 'b', 'c', 'd']

# Sorted string banane ke liye:

# s = "dcba"

# result = "".join(sorted(s))

# print(result)

# Output:

# abcd