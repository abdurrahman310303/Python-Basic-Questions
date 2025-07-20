"""
7. How do you write a comment in Python?

Comments in Python are used to explain code, make it more readable, and provide documentation.
Python supports single-line and multi-line comments.
"""

print("=== COMMENTS IN PYTHON ===\n")

# 1. SINGLE-LINE COMMENTS
print("1. SINGLE-LINE COMMENTS")
print("-" * 30)

# This is a single-line comment
name = "John"  # This comment is on the same line as code
age = 25  # Another inline comment

print(f"Name: {name}, Age: {age}")

# Comments can be used to explain complex logic
# Calculate the area of a circle
radius = 5
area = 3.14159 * radius ** 2  # Formula: π * r²

print(f"Circle area: {area}")

# 2. MULTI-LINE COMMENTS
print("\n2. MULTI-LINE COMMENTS")
print("-" * 30)

# Method 1: Using multiple # symbols
# This is a multi-line comment
# using multiple hash symbols
# Each line starts with #

def calculate_rectangle_area(length, width):
    # This function calculates the area of a rectangle
    # Parameters:
    #   length: the length of the rectangle
    #   width: the width of the rectangle
    # Returns: the area of the rectangle
    return length * width

# Method 2: Using triple quotes (docstring style)
"""
This is a multi-line comment
using triple quotes.
This is often used for docstrings
and longer explanations.
"""

'''
This is another way to write
multi-line comments using
single quotes.
'''

# 3. DOCSTRINGS
print("\n3. DOCSTRINGS")
print("-" * 30)

def greet_user(name):
    """
    This is a docstring - a special type of comment
    that provides documentation for functions, classes, and modules.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"

# Accessing docstrings
print(f"Function docstring: {greet_user.__doc__}")

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    
    Attributes:
        name (str): The name of the calculator
    """
    
    def __init__(self, name):
        self.name = name
    
    def add(self, a, b):
        """Add two numbers together."""
        return a + b

# 4. COMMENT STYLES AND CONVENTIONS
print("\n4. COMMENT STYLES AND CONVENTIONS")
print("-" * 30)

# Good comment practices
PI = 3.14159  # Mathematical constant π

# Calculate the hypotenuse of a right triangle
# Using the Pythagorean theorem: c = √(a² + b²)
a = 3
b = 4
c = (a**2 + b**2)**0.5

print(f"Hypotenuse: {c}")

# TODO comments
# TODO: Add input validation
# TODO: Implement error handling
# FIXME: This function needs optimization

# BAD comment practices (avoid these)
x = 5  # x equals 5  # Too obvious
y = x + 1  # add 1 to x  # Redundant

# 5. COMMENT PLACEMENT
print("\n5. COMMENT PLACEMENT")
print("-" * 30)

# Comments above code (most common)
# Initialize the counter
counter = 0

# Comments on the same line (for short explanations)
total = price * quantity  # Calculate total cost

# Comments for complex logic
# Check if user is eligible for discount
# Conditions: age >= 65 OR income < 30000
if age >= 65 or income < 30000:
    discount = 0.1
else:
    discount = 0.0

# 6. PRACTICAL EXAMPLES
print("\n6. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Algorithm explanation
def bubble_sort(arr):
    """
    Sort an array using the bubble sort algorithm.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping occurs, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr

# Example 2: Configuration comments
# Database configuration
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "myapp"
DB_USER = "admin"
# DB_PASSWORD = "secret"  # Commented out for security

# Example 3: Debugging comments
def debug_function():
    # Enable debug mode
    DEBUG = True
    
    if DEBUG:
        print("Debug: Entering function")
        # print("Debug: Variable x =", x)  # Commented debug line
    
    # Main function logic
    result = 42
    
    if DEBUG:
        print("Debug: Exiting function")
    
    return result

# 7. COMMENT BEST PRACTICES
print("\n7. COMMENT BEST PRACTICES")
print("-" * 30)

# Good: Explain WHY, not WHAT
# Bad: x = x + 1  # Add 1 to x
# Good: x = x + 1  # Increment counter for next iteration

# Good: Comment complex algorithms
def find_prime_factors(n):
    """Find all prime factors of a number."""
    factors = []
    d = 2
    
    # Divide by 2 until odd
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is still > 2, it's prime
    if n > 2:
        factors.append(n)
    
    return factors

# Good: Use comments for section headers
# ==========================================
# DATA PROCESSING SECTION
# ==========================================

# Good: Comment out code temporarily
# old_code = "This is commented out"
new_code = "This is active"

# 8. COMMENT TYPES AND PURPOSES
print("\n8. COMMENT TYPES AND PURPOSES")
print("-" * 30)

# 1. Header comments
# ==========================================
# File: user_management.py
# Author: John Doe
# Date: 2024-01-15
# Description: User management functionality
# ==========================================

# 2. Function documentation
def validate_email(email):
    """
    Validate email address format.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Raises:
        ValueError: If email is empty
    """
    if not email:
        raise ValueError("Email cannot be empty")
    
    # Check for @ symbol
    if '@' not in email:
        return False
    
    # Check for domain
    if '.' not in email.split('@')[1]:
        return False
    
    return True

# 3. Inline explanations
def complex_calculation(x, y, z):
    # Use the quadratic formula: x = (-b ± √(b² - 4ac)) / 2a
    # where a = x, b = y, c = z
    discriminant = y**2 - 4*x*z
    
    if discriminant < 0:
        return None  # No real solutions
    
    sqrt_disc = discriminant**0.5
    solution1 = (-y + sqrt_disc) / (2*x)
    solution2 = (-y - sqrt_disc) / (2*x)
    
    return solution1, solution2

# 4. TODO and FIXME comments
def incomplete_function():
    # TODO: Implement user authentication
    # TODO: Add input validation
    # FIXME: This causes a memory leak
    # HACK: Temporary workaround for bug #123
    pass

# 9. COMMENTING DIFFERENT CODE STRUCTURES
print("\n9. COMMENTING DIFFERENT CODE STRUCTURES")
print("-" * 30)

# Class comments
class BankAccount:
    """
    A simple bank account class.
    
    Attributes:
        balance (float): Current account balance
        account_number (str): Unique account identifier
    """
    
    def __init__(self, account_number, initial_balance=0):
        """Initialize a new bank account."""
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return True
        return False

# Module-level comments
"""
This module provides utility functions for data processing.
It includes functions for:
- Data validation
- Data transformation
- Data analysis
"""

# Import comments
import os  # For file system operations
import sys  # For system-specific parameters
import json  # For JSON data handling

# 10. COMMENTING STYLES
print("\n10. COMMENTING STYLES")
print("-" * 30)

# Style 1: Minimal comments (self-documenting code)
def calculate_area(length, width):
    return length * width  # Self-explanatory

# Style 2: Detailed comments
def calculate_area_detailed(length, width):
    # Calculate the area of a rectangle
    # Formula: Area = Length × Width
    # Parameters:
    #   length: the length of the rectangle in units
    #   width: the width of the rectangle in units
    # Returns: the area in square units
    area = length * width
    return area

# Style 3: Block comments
def process_data(data):
    # ==========================================
    # DATA PROCESSING PIPELINE
    # ==========================================
    # Step 1: Clean the data
    # Step 2: Transform the data
    # Step 3: Validate the data
    # ==========================================
    
    # Step 1: Clean the data
    cleaned_data = [item.strip() for item in data if item]
    
    # Step 2: Transform the data
    transformed_data = [item.upper() for item in cleaned_data]
    
    # Step 3: Validate the data
    valid_data = [item for item in transformed_data if len(item) > 0]
    
    return valid_data

# 11. SUMMARY
print("\n11. SUMMARY")
print("-" * 30)

print("Comment Types in Python:")
print("1. Single-line comments: # comment")
print("2. Multi-line comments: ''' or \"\"\"")
print("3. Docstrings: \"\"\" for functions/classes \"\"\"")
print("4. Inline comments: code # comment")

print("\nComment Best Practices:")
print("- Explain WHY, not WHAT")
print("- Use comments for complex logic")
print("- Keep comments up to date")
print("- Use clear and concise language")
print("- Avoid obvious comments")
print("- Use TODO/FIXME for future work")

print("\nComment Placement:")
print("- Above code for explanations")
print("- Same line for short clarifications")
print("- Use docstrings for function documentation")
print("- Use header comments for file/module documentation")

print("\nWhen to Comment:")
print("- Complex algorithms")
print("- Business logic")
print("- Workarounds and hacks")
print("- Configuration settings")
print("- Future improvements (TODO)")
print("- Bug fixes (FIXME)") 