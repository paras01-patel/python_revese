# 3. Inheritance in Python

# Inheritance ka matlab hai ek class dusri class ke properties aur methods ko use kar sakti hai.

# Simple words me:

# 👉 Parent Class ke features Child Class me aa jate hain.
# 👉 Code Reusability badh jati hai.

# Simple Inheritance
# class Animal:

#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     pass

# d = Dog()
# d.sound()

# Output:

# Animal Sound

# Yaha Dog class ne Animal class ka sound() method inherit kar liya.

# Parent aur Child Class
# class Person:

#     def display(self):
#         print("I am a Person")

# class Student(Person):
#     pass

# s = Student()
# s.display()

# Output:

# I am a Person
# Child Class Apna Method Bhi Bana Sakti Hai
# class Animal:

#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):

#     def bark(self):
#         print("Dog Barking")

# d = Dog()

# d.sound()
# d.bark()

# Output:

# Animal Sound
# Dog Barking
# Types of Inheritance
# 1. Single Inheritance
# class A:
#     pass

# class B(A):
#     pass

# Ek Parent → Ek Child

# 2. Multilevel Inheritance
# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# A → B → C

# 3. Multiple Inheritance
# class A:
#     def show(self):
#         print("Class A")

# class B:
#     def display(self):
#         print("Class B")

# class C(A, B):
#     pass

# c = C()

# c.show()
# c.display()
# 4. Hierarchical Inheritance
# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass