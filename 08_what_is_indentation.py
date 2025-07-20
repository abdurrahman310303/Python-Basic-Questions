"""
8. What is indentation in Python?

Indentation in Python is the use of whitespace (spaces or tabs) at the beginning of lines
to define code blocks and structure. Unlike many other programming languages that use
braces {} to define blocks, Python uses indentation to determine the scope of code.
"""

print("=== INDENTATION IN PYTHON ===\n")

# 1. BASIC INDENTATION
print("1. BASIC INDENTATION")
print("-" * 30)

# This is the main level (no indentation)
x = 10

if x > 5:
    # This line is indented - it belongs to the if block
    print("x is greater than 5")
    print("This line is also indented")
    # All indented lines are part of the same block

# This line is back to the main level
print("This is not indented - back to main level")

# 2. INDENTATION RULES
print("\n2. INDENTATION RULES")
print("-" * 30)

# Rule 1: Use consistent indentation (spaces or tabs, but not mixed)
# Good: Using 4 spaces (recommended)
def good_function():
    print("This uses 4 spaces")
    if True:
        print("This uses 8 spaces (4 + 4)")
        for i in range(3):
            print("This uses 12 spaces (4 + 4 + 4)")

# Rule 2: Indentation must be consistent within a block
def demonstrate_indentation():
    # All lines in this block use the same indentation level
    first_line = "This is indented"
    second_line = "This is also indented"
    third_line = "This is also indented"
    
    # You cannot mix indentation levels within the same block
    # bad_line = "This would cause an error"  # Wrong indentation

# 3. INDENTATION IN DIFFERENT STRUCTURES
print("\n3. INDENTATION IN DIFFERENT STRUCTURES")
print("-" * 30)

# If statements
age = 18
if age >= 18:
    print("You are an adult")
    print("You can vote")
    if age >= 21:
        print("You can drink alcohol")
else:
    print("You are a minor")
    print("You cannot vote")

# For loops
print("\nFor loop indentation:")
for i in range(3):
    print(f"Loop iteration {i}")
    print("This is also part of the loop")
    if i == 1:
        print("This is nested inside the loop")
print("This is outside the loop")

# While loops
print("\nWhile loop indentation:")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
    if counter == 2:
        print("Counter is 2")
print("Loop finished")

# 4. FUNCTION INDENTATION
print("\n4. FUNCTION INDENTATION")
print("-" * 30)

def calculate_area(length, width):
    # Function body is indented
    area = length * width
    print(f"Area: {area}")
    return area

def greet_user(name):
    # Function body is indented
    if name:
        # Nested if block is further indented
        print(f"Hello, {name}!")
        return True
    else:
        # Else block is at same level as if
        print("Hello, anonymous!")
        return False

# 5. CLASS INDENTATION
print("\n5. CLASS INDENTATION")
print("-" * 30)

class Calculator:
    # Class body is indented
    def __init__(self):
        # Method body is indented
        self.result = 0
    
    def add(self, x, y):
        # Method body is indented
        self.result = x + y
        return self.result
    
    def get_result(self):
        # Method body is indented
        return self.result

# 6. NESTED STRUCTURES
print("\n6. NESTED STRUCTURES")
print("-" * 30)

def process_data(data):
    # Function body
    results = []
    
    for item in data:
        # Loop body
        if isinstance(item, str):
            # If block body
            processed = item.upper()
            results.append(processed)
        elif isinstance(item, int):
            # Elif block body
            processed = item * 2
            results.append(processed)
        else:
            # Else block body
            results.append(None)
    
    return results

# 7. COMMON INDENTATION ERRORS
print("\n7. COMMON INDENTATION ERRORS")
print("-" * 30)

# Error 1: Inconsistent indentation
def bad_function():
    print("This is correct")
  # print("This would cause IndentationError")  # Wrong indentation

# Error 2: Missing indentation
def another_bad_function():
    print("This is correct")
# print("This would cause IndentationError")  # Missing indentation

# Error 3: Mixed tabs and spaces
def mixed_indentation():
    print("This uses spaces")
	# print("This uses tabs - would cause error")  # Mixed tabs and spaces

# 8. INDENTATION BEST PRACTICES
print("\n8. INDENTATION BEST PRACTICES")
print("-" * 30)

# Best Practice 1: Use 4 spaces (PEP 8 recommendation)
def good_practice_function():
    # Use 4 spaces for indentation
    if True:
        # Use 8 spaces for nested blocks
        for i in range(3):
            # Use 12 spaces for further nesting
            print(f"Nested level {i}")

# Best Practice 2: Be consistent
def consistent_function():
    # All indentation uses the same number of spaces
    first_block = True
    if first_block:
        second_block = True
        if second_block:
            third_block = True

# Best Practice 3: Use meaningful indentation
def meaningful_function():
    # Clear structure with proper indentation
    data = [1, 2, 3, 4, 5]
    
    # Process each item
    for item in data:
        # Check if item is valid
        if item > 0:
            # Process valid item
            result = item * 2
            print(f"Processed: {result}")
        else:
            # Handle invalid item
            print("Invalid item")

# 9. INDENTATION IN COMPLEX STRUCTURES
print("\n9. INDENTATION IN COMPLEX STRUCTURES")
print("-" * 30)

# Complex nested structure
def complex_function():
    # Level 1: Function body
    users = ["Alice", "Bob", "Charlie"]
    results = {}
    
    for user in users:
        # Level 2: Loop body
        if user.startswith("A"):
            # Level 3: If block
            results[user] = "Admin"
            print(f"{user} is an admin")
        elif user.startswith("B"):
            # Level 3: Elif block
            results[user] = "User"
            print(f"{user} is a user")
        else:
            # Level 3: Else block
            results[user] = "Guest"
            print(f"{user} is a guest")
    
    return results

# 10. INDENTATION WITH TRY-EXCEPT
print("\n10. INDENTATION WITH TRY-EXCEPT")
print("-" * 30)

def safe_division(a, b):
    try:
        # Try block body
        result = a / b
        print(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        # Except block body
        print("Error: Division by zero")
        return None
    except TypeError:
        # Another except block
        print("Error: Invalid types")
        return None
    finally:
        # Finally block body
        print("Division operation completed")

# 11. INDENTATION IN LIST/DICT COMPREHENSIONS
print("\n11. INDENTATION IN LIST/DICT COMPREHENSIONS")
print("-" * 30)

# List comprehension (no indentation needed)
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers if x % 2 == 0]

# Multi-line list comprehension (indentation for readability)
squares_multi = [
    x**2 
    for x in numbers 
    if x % 2 == 0
]

# Dictionary comprehension
word_lengths = {
    word: len(word) 
    for word in ["apple", "banana", "cherry"]
}

# 12. INDENTATION IN CONTEXT MANAGERS
print("\n12. INDENTATION IN CONTEXT MANAGERS")
print("-" * 30)

# Using 'with' statement
with open("temp_file.txt", "w") as file:
    # Context manager body is indented
    file.write("Hello, World!")
    file.write("\nThis is a test file")

# Reading the file
with open("temp_file.txt", "r") as file:
    # Context manager body is indented
    content = file.read()
    print(f"File content: {content}")

# Clean up
import os
if os.path.exists("temp_file.txt"):
    os.remove("temp_file.txt")

# 13. INDENTATION DEBUGGING
print("\n13. INDENTATION DEBUGGING")
print("-" * 30)

# Common indentation errors and how to fix them

# Error: IndentationError: expected an indented block
def fix_indentation_error():
    if True:
        print("This is correct")
        # Missing indentation would cause error
        # print("This would cause IndentationError")

# Error: IndentationError: unindent does not match any outer indentation level
def fix_unindent_error():
    if True:
        print("This is correct")
    # print("This would cause error - wrong indentation level")
    print("This is correct - back to function level")

# 14. INDENTATION TOOLS AND TIPS
print("\n14. INDENTATION TOOLS AND TIPS")
print("-" * 30)

# Tip 1: Use your editor's indentation guides
def use_indentation_guides():
    # Most editors show indentation guides
    if True:
        # This line should align with the if
        print("Aligned correctly")
        if True:
            # This line should align with the nested if
            print("Nested alignment")

# Tip 2: Use consistent indentation style
def consistent_style():
    # Choose one style and stick to it
    data = [1, 2, 3]
    
    for item in data:
        if item > 1:
            result = item * 2
            print(result)

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("Key Points about Indentation:")
print("1. Python uses indentation to define code blocks")
print("2. Use 4 spaces for indentation (PEP 8 recommendation)")
print("3. Be consistent with indentation within a block")
print("4. Don't mix tabs and spaces")
print("5. Indentation determines code scope and structure")

print("\nIndentation Rules:")
print("- Use consistent indentation (4 spaces recommended)")
print("- All lines in a block must have the same indentation level")
print("- Increase indentation for nested blocks")
print("- Decrease indentation to exit a block")
print("- Empty lines don't affect indentation")

print("\nCommon Structures that Require Indentation:")
print("- Function definitions")
print("- Class definitions")
print("- If/elif/else statements")
print("- For and while loops")
print("- Try/except/finally blocks")
print("- With statements")

print("\nBest Practices:")
print("- Use 4 spaces (not tabs)")
print("- Be consistent throughout your code")
print("- Use meaningful indentation structure")
print("- Let your editor help with indentation")
print("- Use indentation to make code readable") 