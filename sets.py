# Python Set

# Set ek unordered collection hota hai jisme duplicate values allow nahi hoti.

# Curly braces {} me likha jata hai.
# Duplicate values automatically remove ho jati hain.
# Indexing nahi hoti.
# Mutable hota hai (elements add/remove kar sakte hain).
# Set Banane Ka Tarika
# numbers = {1, 2, 3, 4, 5}

# print(numbers)

# Output:

# {1, 2, 3, 4, 5}
# Duplicate Values
# numbers = {1, 2, 2, 3, 4, 4, 5}

# print(numbers)

# Output:

# {1, 2, 3, 4, 5}
# Add Element
# numbers = {1, 2, 3}

# numbers.add(4)

# print(numbers)

# Output:

# {1, 2, 3, 4}
# Remove Element
# numbers = {1, 2, 3, 4}

# numbers.remove(2)

# print(numbers)

# Output:

# {1, 3, 4}
# Loop in Set
# fruits = {"Apple", "Banana", "Mango"}

# for fruit in fruits:
#     print(fruit)
# Union (|)

# Dono sets ke unique elements.

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

# Pehle set me jo hai aur dusre me nahi.

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a - b)

# Output:

# {1}
# Important Set Methods
# Method	Kaam
# add()	Element add karta hai
# remove()	Element remove karta hai
# pop()	Random element remove karta hai
# clear()	Set empty karta hai
# union()	Sets ko combine karta hai
# intersection()	Common elements deta hai
# difference()	Difference deta hai