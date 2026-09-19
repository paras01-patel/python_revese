# Polymorphism in Python

# Polymorphism ka matlab hai "One Name, Many Forms".

# Simple words me:

# 👉 Same method ka naam ho sakta hai, lekin alag-alag classes me uska behavior alag ho sakta hai.

# Example 1: Same Method, Different Behavior
# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# d = Dog()
# c = Cat()

# d.sound()
# c.sound()

# Output:

# Bark
# Meow

# Yaha sound() method dono classes me hai, lekin output alag hai.

# Example 2: Polymorphism with Loop
# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.sound()

# Output:

# Bark
# Meow
# Method Overriding

# Jab child class parent class ke method ko apne hisab se redefine karti hai.

# class Animal:
#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog Barking")

# d = Dog()
# d.sound()

# Output:

# Dog Barking
# Real Life Example
# Shape → area()

# Circle → area()
# Square → area()
# Rectangle → area()