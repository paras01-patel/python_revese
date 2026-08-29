# Python Loops

# Loop ka use kisi code ko baar-baar execute karne ke liye kiya jata hai.

# Python me mainly 2 types ke loops hote hain:

# for loop
# while loop
# 1. For Loop

# Jab hume pata ho ki loop kitni baar chalega tab for loop use karte hain.

# Example 1
# for i in range(5):
#     print(i)

# Output:

# 0
# 1
# 2
# 3
# 4
# Example 2
# for i in range(1, 6):
#     print(i)

# Output:

# 1
# 2
# 3
# 4
# 5
# Example 3: List ke Sath
# fruits = ["Apple", "Banana", "Mango"]

# for fruit in fruits:
#     print(fruit)

# Output:

# Apple
# Banana
# Mango
# 2. While Loop

# Jab tak condition True rahegi tab tak loop chalta rahega.

# Example
# i = 1

# while i <= 5:
#     print(i)
#     i += 1

# Output:

# 1
# 2
# 3
# 4
# 5
# Nested Loop

# Loop ke andar loop.

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# Output:

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# break Statement

# Loop ko turant stop kar deta hai.

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# Output:

# 1
# 2
# 3
# 4
# continue Statement

# Current iteration skip kar deta hai.

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# Output:

# 1
# 2
# 4
# 5
# pass Statement

# Kuch bhi nahi karta, placeholder ki tarah use hota hai.

# for i in range(5):
#     pass