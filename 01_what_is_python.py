"""
1. What is Python?

Python is a high-level, interpreted, general-purpose programming language created by Guido van Rossum 
and first released in 1991. It emphasizes code readability with its notable use of significant whitespace.

Key Characteristics:
- High-level language (closer to human language than machine language)
- Interpreted (executed line by line, not compiled)
- Object-oriented programming support
- Dynamic typing
- Automatic memory management
- Extensive standard library
- Cross-platform compatibility
"""

# Example 1: Simple Hello World
print("Hello, World!")

# Example 2: Python's readability
def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

# Example 3: Python's simplicity
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]  # List comprehension
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared}")

# Example 4: Python's versatility
import math

# Mathematical operations
radius = 5
area = math.pi * radius**2
print(f"Area of circle with radius {radius}: {area:.2f}")

# Example 5: Working with different data types
text = "Python is amazing!"
number = 42
decimal = 3.14
is_true = True
my_list = [1, 2, 3, 4, 5]

print(f"Text: {text}")
print(f"Number: {number}")
print(f"Decimal: {decimal}")
print(f"Boolean: {is_true}")
print(f"List: {my_list}")

# Example 6: Python's object-oriented nature
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Camry")
print(f"My car: {my_car.display_info()}")

# Example 7: Python's extensive standard library
import datetime

current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")

# Example 8: File handling
with open("sample.txt", "w") as file:
    file.write("Python is a versatile programming language!")

with open("sample.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# Clean up
import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")

print("\nPython is widely used for:")
print("- Web development (Django, Flask)")
print("- Data science and machine learning")
print("- Automation and scripting")
print("- Game development")
print("- Desktop applications")
print("- API development")
print("- And much more!") 