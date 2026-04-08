"""
File: operators_in_python.py
Author: Vidhata Parte
Description: Demonstrates all types of Python operators with examples
"""

# ---------------- Arithmetic Operators ----------------
print("\n--- Arithmetic Operators ---")
a = 10
b = 3
print(a + b)      # Addition: 13
print(a - b)      # Subtraction: 7
print(a * b)      # Multiplication: 30
print(a / b)      # Division: 3.333...
print(a // b)     # Floor Division: 3
print(a % b)      # Modulus: 1
print(a ** b)     # Exponentiation: 1000

# ---------------- Comparison Operators ----------------
print("\n--- Comparison Operators ---")
print(a == b)     # Equal: False
print(a != b)     # Not Equal: True
print(a > b)      # Greater Than: True
print(a < b)      # Less Than: False
print(a >= b)     # Greater or Equal: True
print(a <= b)     # Less or Equal: False

# ---------------- Logical Operators ----------------
print("\n--- Logical Operators ---")
x = True
y = False
print(x and y)    # Logical AND: False
print(x or y)     # Logical OR: True
print(not x)      # Logical NOT: False

# ---------------- Assignment Operators ----------------
print("\n--- Assignment Operators ---")
c = 5
c += 3            # c = c + 3 → 8
c -= 2            # c = c - 2 → 6
c *= 2            # c = c * 2 → 12
c //= 3           # c = c // 3 → 4
print(c)          # Final value: 4

# ---------------- Membership Operators ----------------
print("\n--- Membership Operators ---")
lst = [1, 2, 3, 4, 5]
print(3 in lst)       # True
print(10 not in lst)  # True

print("\n--- More Membership Operators ---")
string = "hello world"
print("h" in string)          # True
print("x" in string)          # False
print("world" in string)      # True
print("abc" not in string)    # True

tuple_data = (10, 20, 30, 40)
print(20 in tuple_data)       # True
print(50 not in tuple_data)   # True

# ---------------- Identity Operators ----------------
print("\n--- Identity Operators ---")
d = [1, 2, 3]
e = d
f = [1, 2, 3]
print(d is e)     # True (same object)
print(d is f)     # False (different objects)
print(d is not f) # True

print("\nProgram executed successfully ✅")