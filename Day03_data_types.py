# 1. String
name = "Python"
print(type(name))  # <class 'str'>

# 2. Integer
age = 25
print(type(age))  # <class 'int'>

# 3. Float
height = 5.9
print(type(height))  # <class 'float'>

# 4. Boolean
is_active = True
print(type(is_active))  # <class 'bool'>

# 5. List (ordered, mutable)
fruits = ["apple", "banana", "orange"]
print(type(fruits))  # <class 'list'>

# 6. Tuple (ordered, immutable)
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>

# 7. Dictionary (key-value pairs)
person = {"name": "John", "age": 30}
print(type(person))  # <class 'dict'>

# 8. Set (unordered, unique items)
colors = {"red", "blue", "green"}
print(type(colors))  # <class 'set'>

# 9. None
empty = None
print(type(empty))  # <class 'NoneType'>

# Check type of any variable
print(isinstance(age, int))  # True




# Data Types in Python my practice

#string
name = "Nirankar" 
print (type(name))

#boolean
is_true= True
print (type(is_true))

#list
books =["aumotic habits","phychology of money","the power of subconsious mind","rich dad poor dad"]
print (type (books))

#tuple
grops = ("data analyst","data scientist","machine learning engineer")
print (type(grops))

branch =("cse","it","ece","mech","civil")
print (type(branch))

#dictionary
solar_system = {"Mercury": 0.39, "Venus": 0.72, "Earth": 1.00, "Mars": 1.52}
print (type(solar_system))  

product ={ "laptop":50000,"mobile":20000,"headphone":5000}
print (type(product))

#set
unique_numbers = {1, 2, 3, 4, 5}    
print (type(unique_numbers))
