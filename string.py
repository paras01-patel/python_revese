# Strings in Python

# A String is a sequence of characters enclosed in quotes.

# name = "Paras"

# Here, "Paras" is a string.

# Creating Strings
# name = "Paras"
# city = 'Indore'

# print(name)
# print(city)
# String Indexing

# Index starts from 0.

# name = "Paras"

# print(name[0])
# print(name[1])
# print(name[2])

# Output

# P
# a
# r
# Negative Indexing
# name = "Paras"

# print(name[-1])
# print(name[-2])

# Output

# s
# a
# String Slicing
# Syntax
# string[start:end]
# Example
# name = "Paras"

# print(name[0:3])

# Output

# Par
# name = "Paras"

# print(name[1:4])

# Output

# ara
# String Length
# name = "Paras"

# print(len(name))

# Output

# 5
# String Concatenation
# first = "Paras"
# last = "Chandrawanshi"

# print(first + " " + last)

# Output

# Paras Chandrawanshi
# String Repetition
# print("Hi " * 3)

# Output

# Hi Hi Hi
# Convert Case
# name = "Paras"

# print(name.upper())
# print(name.lower())

# Output

# PARAS
# paras
# Remove Spaces
# name = "  Paras  "

# print(name.strip())

# Output

# Paras
# Replace Characters
# name = "Paras"

# print(name.replace("a", "@"))

# Output

# P@r@s
# Split String
# text = "Python Django React"

# print(text.split())

# Output

# ['Python', 'Django', 'React']
# Check Substring
# name = "Paras"

# print("ra" in name)

# Output

# True
# Loop Through String
# name = "Paras"

# for ch in name:
#     print(ch)
# Reverse String
# Method 1 (Slicing)
# name = "Paras"

# print(name[::-1])

# Output

# saraP
# Method 2 (Loop)
# name = "Paras"

# rev = ""

# for ch in name:
#     rev = ch + rev

# print(rev)
# Palindrome Check

# A palindrome reads the same forward and backward.

# Examples:

# madam
# level
# radar
# s = "madam"

# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# Count Characters
# s = "banana"

# count = 0

# for ch in s:
#     if ch == "a":
#         count += 1

# print(count)

# Output

# 3
# Character Frequency (Important)
# s = "banana"

# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)

# Output

# {'b': 1, 'a': 3, 'n': 2}
# Valid Anagram (Interview)

# Two strings are anagrams if they contain the same characters with the same frequency.

# s = "listen"
# t = "silent"

# if sorted(s) == sorted(t):
#     print(True)
# else:
#     print(False)

# Output

# True
# Important String Methods
# Method	Use
# upper()	Uppercase
# lower()	Lowercase
# strip()	Remove spaces
# replace()	Replace text
# split()	Convert to list
# find()	Find index
# count()	Count characters
# startswith()	Check beginning
# endswith()	Check ending