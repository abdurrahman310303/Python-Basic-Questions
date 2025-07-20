"""
2. What are the key features of Python?

Python has several distinctive features that make it popular among developers:
"""

# 1. SIMPLE AND READABLE SYNTAX
print("=== 1. Simple and Readable Syntax ===")
# Python uses English keywords and clear syntax
if True:
    print("This is easy to read!")
    print("Indentation shows code blocks")

# 2. DYNAMIC TYPING
print("\n=== 2. Dynamic Typing ===")
# Variables can change types dynamically
x = 10          # x is an integer
print(f"x = {x}, type: {type(x)}")

x = "Hello"     # x is now a string
print(f"x = {x}, type: {type(x)}")

x = [1, 2, 3]  # x is now a list
print(f"x = {x}, type: {type(x)}")

# 3. AUTOMATIC MEMORY MANAGEMENT
print("\n=== 3. Automatic Memory Management ===")
# Python handles memory allocation and deallocation automatically
import sys

# Creating objects
list1 = [1, 2, 3, 4, 5]
print(f"Memory usage of list1: {sys.getsizeof(list1)} bytes")

# Python automatically frees memory when objects go out of scope
del list1  # Explicitly delete (though not necessary)

# 4. EXTENSIVE STANDARD LIBRARY
print("\n=== 4. Extensive Standard Library ===")
import os
import datetime
import json
import urllib.request

# File operations
print(f"Current working directory: {os.getcwd()}")

# Date and time
now = datetime.datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# JSON handling
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

# 5. CROSS-PLATFORM COMPATIBILITY
print("\n=== 5. Cross-Platform Compatibility ===")
import platform
print(f"Operating System: {platform.system()}")
print(f"Python Version: {platform.python_version()}")

# 6. OBJECT-ORIENTED PROGRAMMING
print("\n=== 6. Object-Oriented Programming ===")
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some sound"
    
    def get_info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")
    
    def make_sound(self):
        return "Woof!"

my_dog = Dog("Buddy")
print(f"Dog info: {my_dog.get_info()}")
print(f"Dog sound: {my_dog.make_sound()}")

# 7. FUNCTIONAL PROGRAMMING SUPPORT
print("\n=== 7. Functional Programming Support ===")
# Lambda functions
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

# Map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")

# Filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# 8. LIST COMPREHENSIONS
print("\n=== 8. List Comprehensions ===")
# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(f"Traditional squares: {squares}")

# List comprehension way
squares_comp = [i**2 for i in range(1, 6)]
print(f"Comprehension squares: {squares_comp}")

# 9. EXCEPTION HANDLING
print("\n=== 9. Exception Handling ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred")
finally:
    print("This always executes")

# 10. ITERATORS AND GENERATORS
print("\n=== 10. Iterators and Generators ===")
# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_sequence = list(fibonacci(10))
print(f"First 10 Fibonacci numbers: {fib_sequence}")

# 11. DECORATORS
print("\n=== 11. Decorators ===")
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(0.1)
    return "Done!"

slow_function()

# 12. CONTEXT MANAGERS
print("\n=== 12. Context Managers ===")
# Using 'with' statement for file handling
with open("temp_file.txt", "w") as f:
    f.write("This is a temporary file")

with open("temp_file.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")

# Clean up
import os
if os.path.exists("temp_file.txt"):
    os.remove("temp_file.txt")

print("\n=== Summary ===")
print("Python's key features make it:")
print("- Easy to learn and use")
print("- Highly productive for development")
print("- Versatile across different domains")
print("- Well-supported with extensive libraries")
print("- Ideal for both beginners and experts") 