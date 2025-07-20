"""
10. What is a function in Python?

A function in Python is a reusable block of code that performs a specific task.
Functions help organize code, avoid repetition, and make programs more modular.
"""

print("=== FUNCTIONS IN PYTHON ===\n")

# 1. BASIC FUNCTION DEFINITION
print("1. BASIC FUNCTION DEFINITION")
print("-" * 30)

# Simple function without parameters
def greet():
    """This is a simple function that prints a greeting."""
    print("Hello, World!")

# Calling the function
greet()

# Function with parameters
def greet_person(name):
    """Function that greets a specific person."""
    print(f"Hello, {name}!")

# Calling with argument
greet_person("Alice")
greet_person("Bob")

# 2. FUNCTION WITH RETURN VALUES
print("\n2. FUNCTION WITH RETURN VALUES")
print("-" * 30)

def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result

# Using the return value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

rectangle_area = calculate_area(4, 6)
print(f"Rectangle area (4x6): {rectangle_area}")

# 3. FUNCTION PARAMETERS
print("\n3. FUNCTION PARAMETERS")
print("-" * 30)

# Required parameters
def multiply(x, y):
    return x * y

print(f"Multiply: {multiply(3, 4)}")

# Default parameters
def greet_with_default(name="World"):
    return f"Hello, {name}!"

print(f"Default: {greet_with_default()}")
print(f"Custom: {greet_with_default('Alice')}")

# Multiple default parameters
def create_profile(name, age=25, city="Unknown"):
    return f"Name: {name}, Age: {age}, City: {city}"

print(f"Profile 1: {create_profile('John')}")
print(f"Profile 2: {create_profile('Alice', 30)}")
print(f"Profile 3: {create_profile('Bob', 35, 'New York')}")

# 4. ARBITRARY ARGUMENTS
print("\n4. ARBITRARY ARGUMENTS")
print("-" * 30)

# *args - arbitrary positional arguments
def sum_all(*args):
    """Sum all provided numbers."""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_all(10, 20, 30, 40)}")

# **kwargs - arbitrary keyword arguments
def print_info(**kwargs):
    """Print all provided keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Person info:")
print_info(name="John", age=30, city="New York", occupation="Engineer")

# 5. FUNCTION TYPES
print("\n5. FUNCTION TYPES")
print("-" * 30)

# Built-in functions
print(f"Length of 'hello': {len('hello')}")
print(f"Maximum of 1, 5, 3: {max(1, 5, 3)}")
print(f"Type of 42: {type(42)}")

# User-defined functions
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# 6. FUNCTION SCOPE
print("\n6. FUNCTION SCOPE")
print("-" * 30)

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Global variable: {global_var}")

scope_demo()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variables
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment_counter()
increment_counter()
increment_counter()

# 7. FUNCTION DOCUMENTATION
print("\n7. FUNCTION DOCUMENTATION")
print("-" * 30)

def calculate_volume(length, width, height):
    """
    Calculate the volume of a rectangular prism.
    
    Args:
        length (float): The length of the prism
        width (float): The width of the prism
        height (float): The height of the prism
        
    Returns:
        float: The volume of the prism
        
    Raises:
        ValueError: If any dimension is negative
    """
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    
    volume = length * width * height
    return volume

# Accessing docstring
print(f"Function docstring: {calculate_volume.__doc__}")

# 8. FUNCTION AS OBJECTS
print("\n8. FUNCTION AS OBJECTS")
print("-" * 30)

def greet_function():
    return "Hello!"

# Functions are objects
print(f"Function name: {greet_function.__name__}")
print(f"Function type: {type(greet_function)}")

# Functions can be assigned to variables
my_greeting = greet_function
print(f"Using variable: {my_greeting()}")

# Functions can be passed as arguments
def apply_function(func, value):
    return func(value)

def double(x):
    return x * 2

result = apply_function(double, 5)
print(f"Applied function result: {result}")

# 9. NESTED FUNCTIONS
print("\n9. NESTED FUNCTIONS")
print("-" * 30)

def outer_function(x):
    """Outer function that contains a nested function."""
    
    def inner_function(y):
        """Inner function that can access outer function's variables."""
        return x + y  # x is from outer function
    
    return inner_function

# Using nested function
add_five = outer_function(5)
result = add_five(3)
print(f"Nested function result: {result}")

# 10. PRACTICAL EXAMPLES
print("\n10. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Calculator functions
def calculator(operation, a, b):
    """Simple calculator with different operations."""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print("Calculator examples:")
print(f"5 + 3 = {calculator('+', 5, 3)}")
print(f"10 - 4 = {calculator('-', 10, 4)}")
print(f"6 * 7 = {calculator('*', 6, 7)}")
print(f"15 / 3 = {calculator('/', 15, 3)}")

# Example 2: Data processing functions
def process_student_grades(grades):
    """Process a list of student grades."""
    if not grades:
        return {"average": 0, "highest": 0, "lowest": 0, "count": 0}
    
    return {
        "average": sum(grades) / len(grades),
        "highest": max(grades),
        "lowest": min(grades),
        "count": len(grades)
    }

student_grades = [85, 92, 78, 96, 88, 91]
grade_stats = process_student_grades(student_grades)
print(f"\nGrade statistics: {grade_stats}")

# Example 3: String manipulation functions
def format_name(first, last, middle=""):
    """Format a person's name."""
    if middle:
        return f"{first} {middle} {last}"
    else:
        return f"{first} {last}"

def validate_email(email):
    """Validate email format."""
    if '@' in email and '.' in email.split('@')[1]:
        return True
    return False

print(f"\nFormatted name: {format_name('John', 'Doe', 'Michael')}")
print(f"Email valid: {validate_email('john@example.com')}")

# 11. ADVANCED FUNCTION FEATURES
print("\n11. ADVANCED FUNCTION FEATURES")
print("-" * 30)

# Function decorators
def timer(func):
    """Decorator to measure function execution time."""
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
    """A function that takes time to execute."""
    import time
    time.sleep(0.1)
    return "Done!"

slow_function()

# Generator functions
def fibonacci(n):
    """Generate Fibonacci numbers up to n."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"Fibonacci sequence: {list(fibonacci(10))}")

# 12. FUNCTION BEST PRACTICES
print("\n12. FUNCTION BEST PRACTICES")
print("-" * 30)

# Good: Single responsibility
def calculate_circle_area(radius):
    """Calculate area of a circle."""
    import math
    return math.pi * radius ** 2

# Good: Clear naming
def is_valid_age(age):
    """Check if age is valid (0-150)."""
    return 0 <= age <= 150

# Good: Proper error handling
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Good: Type hints (Python 3.5+)
def greet_typed(name: str, age: int = 25) -> str:
    """Greet with type hints."""
    return f"Hello {name}, you are {age} years old"

# 13. SUMMARY
print("\n13. SUMMARY")
print("-" * 30)

print("Key Points about Functions:")
print("1. Functions are reusable blocks of code")
print("2. They can take parameters and return values")
print("3. They help organize and modularize code")
print("4. They reduce code duplication")
print("5. They improve code readability")

print("\nFunction Components:")
print("- def keyword for definition")
print("- Function name (should be descriptive)")
print("- Parameters (optional)")
print("- Function body (indented)")
print("- return statement (optional)")

print("\nFunction Types:")
print("- Built-in functions (len, print, etc.)")
print("- User-defined functions")
print("- Lambda functions (anonymous)")
print("- Methods (functions in classes)")

print("\nBest Practices:")
print("- Use descriptive function names")
print("- Keep functions small and focused")
print("- Use docstrings for documentation")
print("- Handle errors appropriately")
print("- Use type hints when possible")
print("- Follow single responsibility principle") 