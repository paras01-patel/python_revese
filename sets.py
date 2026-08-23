# Sets in Python

# A Set is a collection of unique elements.

# Features of Set
# Unordered ✅
# Mutable ✅
# No duplicate values ✅
# Faster searching than lists ✅
# Creating a Set
# numbers = {10, 20, 30, 40}

# print(numbers)
# print(type(numbers))

# Output

# {10, 20, 30, 40}
# <class 'set'>
# Duplicate Values are Removed
# numbers = {10, 20, 20, 30, 30, 40}

# print(numbers)

# Output

# {10, 20, 30, 40}
# Creating an Empty Set

# ❌ Wrong

# s = {}
# print(type(s))

# Output:

# <class 'dict'>

# ✅ Correct

# s = set()
# print(type(s))

# Output:

# <class 'set'>
# Add Elements
# numbers = {10, 20, 30}

# numbers.add(40)

# print(numbers)

# Output:

# {10, 20, 30, 40}
# Add Multiple Elements
# numbers = {10, 20}

# numbers.update([30, 40, 50])

# print(numbers)

# Output:

# {10, 20, 30, 40, 50}
# Remove Elements
# remove()
# numbers = {10, 20, 30}

# numbers.remove(20)

# print(numbers)

# Output:

# {10, 30}
# discard()
# numbers = {10, 20, 30}

# numbers.discard(50)

# print(numbers)

# No error occurs if the value doesn't exist.

# Length of Set
# numbers = {10, 20, 30, 40}

# print(len(numbers))

# Output:

# 4
# Check Membership
# numbers = {10, 20, 30}

# print(20 in numbers)
# print(50 in numbers)

# Output:

# True
# False
# Traversing a Set
# numbers = {10, 20, 30, 40}

# for i in numbers:
#     print(i)
# Set Operations
# Union (|)

# Combines all unique elements.

# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a | b)

# Output:

# {1, 2, 3, 4, 5}
# Intersection (&)

# Common elements.

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a & b)

# Output:

# {2, 3}
# Difference (-)

# Elements in first set but not second.

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a - b)

# Output:

# {1}
# Symmetric Difference (^)

# Elements present in only one set.

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a ^ b)

# Output:

# {1, 4}
# Convert List to Set

# Useful for removing duplicates.

# nums = [1, 2, 2, 3, 3, 4]

# unique_nums = set(nums)

# print(unique_nums)

# Output:

# {1, 2, 3, 4}
# Interview Questions
# Remove duplicates from a list
# nums = [1, 2, 2, 3, 3, 4]

# nums = list(set(nums))

# print(nums)
# Check Common Elements
# a = [1, 2, 3]
# b = [3, 4, 5]

# if set(a) & set(b):
#     print("Common elements found")
# Important Set Methods
# Method	Use
# add()	Add one element
# update()	Add multiple elements
# remove()	Remove element
# discard()	Remove without error
# clear()	Remove all elements
# union()	Combine sets
# intersection()	Common elements
# difference()	Difference
# symmetric_difference()	Unique elements