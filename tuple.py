# Python Tuple

# Tuple ek collection data type hai jo multiple values ko ek hi variable me store karta hai.

# Tuple ordered hoti hai.
# Tuple immutable hoti hai (change nahi kar sakte).
# Round brackets () ka use hota hai.
# Duplicate values allow hoti hain.
# Tuple Banane Ka Tarika
# numbers = (10, 20, 30, 40)

# print(numbers)

# Output:

# (10, 20, 30, 40)
# Indexing
# t = (100, 200, 300, 400)

# print(t[0])
# print(t[2])

# Output:

# 100
# 300
# Negative Indexing
# t = (10, 20, 30, 40)

# print(t[-1])

# Output:

# 40
# Slicing
# t = (10, 20, 30, 40, 50)

# print(t[1:4])

# Output:

# (20, 30, 40)
# Loop in Tuple
# t = (10, 20, 30, 40)

# for i in t:
#     print(i)

# Output:

# 10
# 20
# 30
# 40
# Tuple Methods
# count()

# Kitni baar value aayi hai.

# t = (1, 2, 2, 3, 2)

# print(t.count(2))

# Output:

# 3
# index()

# Value ka index batata hai.

# t = (10, 20, 30, 40)

# print(t.index(30))

# Output:

# 2
# Tuple Packing
# t = 10, 20, 30

# print(t)

# Output:

# (10, 20, 30)
# Tuple Unpacking
# t = (10, 20, 30)

# a, b, c = t

# print(a)
# print(b)
# print(c)

# Output:

# 10
# 20
# 30
# Tuple Immutable Hai
# t = (10, 20, 30)

# t[0] = 100

# Output:

# TypeError: 'tuple' object does not support item assignment
# List vs Tuple
# List	Tuple
# Mutable	Immutable
# [] use hota hai	() use hota hai
# Change kar sakte hain	Change nahi kar sakte
# More methods	Kam methods

