"""
6. What is a variable in Python?

A variable in Python is a name that refers to a value stored in memory.
Variables are used to store data that can be accessed and modified throughout a program.
"""

print("=== VARIABLES IN PYTHON ===\n")

# 1. BASIC VARIABLE ASSIGNMENT
print("1. BASIC VARIABLE ASSIGNMENT")
print("-" * 30)

# Simple variable assignment
name = "John"
age = 25
height = 5.9
is_student = True

print(f"name = {name}")
print(f"age = {age}")
print(f"height = {height}")
print(f"is_student = {is_student}")

# 2. VARIABLE NAMING RULES
print("\n2. VARIABLE NAMING RULES")
print("-" * 30)

# Valid variable names
first_name = "Alice"
lastName = "Johnson"
age_2024 = 30
_private_var = "private"
CONSTANT = 3.14159

print(f"Valid variable names:")
print(f"  first_name = {first_name}")
print(f"  lastName = {lastName}")
print(f"  age_2024 = {age_2024}")
print(f"  _private_var = {_private_var}")
print(f"  CONSTANT = {CONSTANT}")

# Invalid variable names (commented out to avoid errors)
# 2name = "invalid"  # Cannot start with number
# my-name = "invalid"  # Cannot contain hyphens
# class = "invalid"  # Cannot use reserved keywords

print("\nInvalid variable names:")
print("- Cannot start with numbers")
print("- Cannot contain hyphens")
print("- Cannot use reserved keywords")
print("- Cannot contain spaces")

# 3. DYNAMIC TYPING
print("\n3. DYNAMIC TYPING")
print("-" * 30)

# Variables can change types dynamically
x = 10
print(f"x = {x}, type: {type(x)}")

x = "Hello"
print(f"x = {x}, type: {type(x)}")

x = [1, 2, 3]
print(f"x = {x}, type: {type(x)}")

x = {"name": "John", "age": 30}
print(f"x = {x}, type: {type(x)}")

# 4. MULTIPLE ASSIGNMENT
print("\n4. MULTIPLE ASSIGNMENT")
print("-" * 30)

# Multiple variables in one line
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Unpacking from a list
numbers = [10, 20, 30]
x, y, z = numbers
print(f"x = {x}, y = {y}, z = {z}")

# Swapping variables
a, b = 5, 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# 5. VARIABLE SCOPES
print("\n5. VARIABLE SCOPES")
print("-" * 30)

# Global variable
global_var = "I'm global"

def test_function():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Global variable: {global_var}")

test_function()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error - local_var is not accessible

# 6. VARIABLE REFERENCES
print("\n6. VARIABLE REFERENCES")
print("-" * 30)

# Variables are references to objects
list1 = [1, 2, 3]
list2 = list1  # Both variables reference the same object

print(f"list1 = {list1}")
print(f"list2 = {list2}")

list1.append(4)
print(f"After modifying list1: {list1}")
print(f"list2 also changed: {list2}")

# Creating a copy
list3 = list1.copy()  # Creates a new object
list1.append(5)
print(f"list1 after append: {list1}")
print(f"list3 unchanged: {list3}")

# 7. VARIABLE MEMORY MANAGEMENT
print("\n7. VARIABLE MEMORY MANAGEMENT")
print("-" * 30)

import sys

# Memory usage of different variables
small_int = 42
large_list = [i for i in range(1000)]
string_var = "Hello, World!"

print(f"Memory usage:")
print(f"  small_int: {sys.getsizeof(small_int)} bytes")
print(f"  large_list: {sys.getsizeof(large_list)} bytes")
print(f"  string_var: {sys.getsizeof(string_var)} bytes")

# 8. VARIABLE NAMING CONVENTIONS
print("\n8. VARIABLE NAMING CONVENTIONS")
print("-" * 30)

# Python naming conventions
# snake_case for variables and functions
user_name = "John"
first_name = "Alice"
calculate_area = lambda x, y: x * y

# UPPER_CASE for constants
PI = 3.14159
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# camelCase (less common in Python)
firstName = "Bob"
lastName = "Smith"

print(f"snake_case: {user_name}, {first_name}")
print(f"UPPER_CASE constants: {PI}, {MAX_RETRIES}")
print(f"camelCase: {firstName}, {lastName}")

# 9. VARIABLE TYPES AND TYPE HINTS
print("\n9. VARIABLE TYPES AND TYPE HINTS")
print("-" * 30)

# Type hints (Python 3.5+)
from typing import List, Dict, Optional

# With type hints
name: str = "John"
age: int = 25
scores: List[int] = [85, 90, 78]
user_info: Dict[str, str] = {"name": "Alice", "city": "Boston"}
optional_value: Optional[str] = None

print(f"Variables with type hints:")
print(f"  name: {name} (type: {type(name)})")
print(f"  age: {age} (type: {type(age)})")
print(f"  scores: {scores} (type: {type(scores)})")
print(f"  user_info: {user_info} (type: {type(user_info)})")
print(f"  optional_value: {optional_value} (type: {type(optional_value)})")

# 10. PRACTICAL EXAMPLES
print("\n10. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Calculator variables
num1 = 10
num2 = 5
result = num1 + num2
print(f"Calculator: {num1} + {num2} = {result}")

# Example 2: String manipulation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Example 3: List operations
numbers = [1, 2, 3, 4, 5]
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {sum_numbers}")
print(f"Average: {average}")

# Example 4: Dictionary variables
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")

# 11. VARIABLE BEST PRACTICES
print("\n11. VARIABLE BEST PRACTICES")
print("-" * 30)

# Good practices
meaningful_name = "Use descriptive names"
CONSTANT_VALUE = 100  # Use UPPER_CASE for constants
user_input = "Get input from user"
is_valid = True  # Boolean variables start with 'is' or 'has'

# Avoid these practices
# a = "Don't use single letters"
# x = "Don't use unclear names"
# temp = "Don't use temporary names"

print("Good variable naming practices:")
print("- Use descriptive names")
print("- Use snake_case for variables")
print("- Use UPPER_CASE for constants")
print("- Boolean variables start with 'is' or 'has'")
print("- Avoid single letters (except in loops)")
print("- Avoid unclear abbreviations")

# 12. VARIABLE DEBUGGING
print("\n12. VARIABLE DEBUGGING")
print("-" * 30)

# Using id() to see memory address
x = 42
y = 42
z = x

print(f"Variable debugging:")
print(f"  x = {x}, id(x) = {id(x)}")
print(f"  y = {y}, id(y) = {id(y)}")
print(f"  z = {z}, id(z) = {id(z)}")

# Using dir() to see object attributes
print(f"\nAttributes of x: {dir(x)}")

# 13. SUMMARY
print("\n13. SUMMARY")
print("-" * 30)

print("Key Points about Variables:")
print("1. Variables are names that reference values in memory")
print("2. Python uses dynamic typing (variables can change types)")
print("3. Variables follow naming conventions (snake_case)")
print("4. Variables have scope (local vs global)")
print("5. Variables are references to objects")
print("6. Use descriptive names for better code readability")
print("7. Constants use UPPER_CASE naming")
print("8. Variables can be typed with type hints")

print("\nVariable Lifecycle:")
print("1. Declaration: name = value")
print("2. Assignment: name = new_value")
print("3. Usage: print(name) or name.operation()")
print("4. Deletion: del name (automatic when out of scope)")

print("\nMemory Management:")
print("- Python automatically manages memory")
print("- Variables are garbage collected when no longer referenced")
print("- Use sys.getsizeof() to check memory usage")
print("- Large objects consume more memory") 