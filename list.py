# Lists in Python

# A List is a collection of items stored in a single variable.

# Ordered ✅
# Mutable (can be changed) ✅
# Allows duplicate values ✅
# Creating a List
# numbers = [10, 20, 30, 40]

# print(numbers)

# Output

# [10, 20, 30, 40]
# Accessing Elements

# Index starts from 0.

# numbers = [10, 20, 30, 40]

# print(numbers[0])
# print(numbers[2])

# Output

# 10
# 30
# Negative Indexing
# numbers = [10, 20, 30, 40]

# print(numbers[-1])
# print(numbers[-2])

# Output

# 40
# 30
# Updating Elements
# numbers = [10, 20, 30]

# numbers[1] = 100

# print(numbers)

# Output

# [10, 100, 30]
# Adding Elements
# append()

# Adds one element at the end.

# numbers = [10, 20, 30]

# numbers.append(40)

# print(numbers)

# Output

# [10, 20, 30, 40]
# insert()

# Adds an element at a specific position.

# numbers = [10, 20, 30]

# numbers.insert(1, 99)

# print(numbers)

# Output

# [10, 99, 20, 30]
# Removing Elements
# remove()

# Removes a value.

# numbers = [10, 20, 30]

# numbers.remove(20)

# print(numbers)

# Output

# [10, 30]
# pop()

# Removes by index.

# numbers = [10, 20, 30]

# numbers.pop(1)

# print(numbers)

# Output

# [10, 30]
# Length of List
# numbers = [10, 20, 30, 40]

# print(len(numbers))

# Output

# 4
# Traversing a List
# Using for Loop
# numbers = [10, 20, 30, 40]

# for i in numbers:
#     print(i)
# Using Index
# numbers = [10, 20, 30, 40]

# for i in range(len(numbers)):
#     print(numbers[i])
# Searching in List
# numbers = [10, 20, 30, 40]

# print(20 in numbers)
# print(100 in numbers)

# Output

# True
# False
# Sorting a List
# Ascending Order
# numbers = [5, 2, 8, 1]

# numbers.sort()

# print(numbers)

# Output

# [1, 2, 5, 8]
# Descending Order
# numbers = [5, 2, 8, 1]

# numbers.sort(reverse=True)

# print(numbers)

# Output

# [8, 5, 2, 1]
# Reverse a List
# numbers = [10, 20, 30, 40]

# numbers.reverse()

# print(numbers)

# Output

# [40, 30, 20, 10]
# Slicing
# numbers = [10, 20, 30, 40, 50]

# print(numbers[1:4])

# Output

# [20, 30, 40]
# Common Interview Programs
# Find Largest Element
# numbers = [10, 40, 20, 80, 30]

# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# print(largest)

# Output

# 80
# Find Sum of List
# numbers = [10, 20, 30, 40]

# total = 0

# for i in numbers:
#     total += i

# print(total)

# Output

# 100
# Find Maximum and Minimum
# numbers = [10, 40, 20, 80, 30]

# print(max(numbers))
# print(min(numbers))
# Important List Methods
# Method	Use
# append()	Add element
# insert()	Add at index
# remove()	Remove value
# pop()	Remove by index
# sort()	Sort list
# reverse()	Reverse list
# len()	Length
# max()	Largest value
# min()	Smallest value
# count()	Count occurrences
# Example
# numbers = [1, 2, 2, 3, 2]

# print(numbers.count(2))

# Output

# 3