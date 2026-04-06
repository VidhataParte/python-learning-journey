# Day 2 - Comments and Data Types in Python
# Author: Vidhata
# Goal: Start journey towards Data Analyst

# ==============================
# Comments in Python
# ==============================

# Single-line comment:
# Comments are ignored by Python and used to explain code

"""
This is a Docstring (multi-line string)
Used for longer explanations
"""

# ==============================
# Variables and Data Types
# ==============================

name = "Vidhata"     # String
age = 25             # Integer
height = 5.7         # Float
is_student = True    # Boolean

print(name)
print(age)
print(height)
print(is_student)

# ==============================
# Variable Naming Rules
# ==============================

# - Must start with a letter or underscore
# - Can contain letters, numbers, underscores
# - Case-sensitive
# - Use meaningful names

my_variable = 10
_private_var = 20 
CONSTANT_VALUE = 100

# ==============================
# Variable Reassignment
# ==============================

count = 5
count = count + 1
print(count)

# ==============================
# Multiple Assignment
# ==============================

x, y, z = 1, 2, 3
print(x, y, z)

# ==============================
# My Practice
# ==============================

name = "Vidhata"
age = 20
salary = 99999999
city = "Mumbai"

print("Hello", name)
print("You are a great person and I know you will be successful in your life.")
print("You will be a great Data Analyst and Data Scientist.")
print("Your age is:", age)
print("Your salary is:", salary)
print("You are from:", city)