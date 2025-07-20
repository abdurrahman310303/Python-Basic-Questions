"""
11. How do you define a function?

Function definition in Python uses the 'def' keyword followed by the function name,
parameters (optional), and a colon. The function body is indented.
"""

print("=== HOW TO DEFINE A FUNCTION ===\n")

# 1. BASIC FUNCTION DEFINITION
print("1. BASIC FUNCTION DEFINITION")
print("-" * 30)

# Simple function without parameters
def say_hello():
    """This is a simple function definition."""
    print("Hello, World!")

# Function with parameters
def greet(name):
    """Function with one parameter."""
    print(f"Hello, {name}!")

# Function with multiple parameters
def add_numbers(a, b):
    """Function with two parameters."""
    return a + b

# 2. FUNCTION DEFINITION SYNTAX
print("\n2. FUNCTION DEFINITION SYNTAX")
print("-" * 30)

# Syntax: def function_name(parameters):
#     function_body

def example_function():
    """Example of basic function definition."""
    print("This is the function body")
    print("All code here is part of the function")

# Function with parameters
def calculate_area(length, width):
    """Calculate area of rectangle."""
    area = length * width
    return area

# Function with default parameters
def greet_with_default(name="World"):
    """Function with default parameter."""
    return f"Hello, {name}!"

# 3. DIFFERENT TYPES OF PARAMETERS
print("\n3. DIFFERENT TYPES OF PARAMETERS")
print("-" * 30)

# Required parameters
def required_params(name, age):
    """Function with required parameters."""
    return f"Name: {name}, Age: {age}"

# Default parameters
def default_params(name="Unknown", age=0):
    """Function with default parameters."""
    return f"Name: {name}, Age: {age}"

# Keyword-only parameters
def keyword_params(*, name, age):
    """Function with keyword-only parameters."""
    return f"Name: {name}, Age: {age}"

# Positional-only parameters
def positional_params(name, age, /):
    """Function with positional-only parameters."""
    return f"Name: {name}, Age: {age}"

# 4. ARBITRARY ARGUMENTS
print("\n4. ARBITRARY ARGUMENTS")
print("-" * 30)

# *args - arbitrary positional arguments
def sum_all(*args):
    """Function that can take any number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

# **kwargs - arbitrary keyword arguments
def print_info(**kwargs):
    """Function that can take any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Combined *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts both positional and keyword arguments."""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

# 5. RETURN VALUES
print("\n5. RETURN VALUES")
print("-" * 30)

# Function with return value
def square_number(x):
    """Return the square of a number."""
    return x ** 2

# Function with multiple return values
def get_name_and_age():
    """Return multiple values."""
    return "John", 25

# Function with conditional return
def absolute_value(x):
    """Return absolute value of a number."""
    if x >= 0:
        return x
    else:
        return -x

# Function with no return (returns None)
def print_message(message):
    """Print a message (no return value)."""
    print(message)

# 6. FUNCTION DOCUMENTATION
print("\n6. FUNCTION DOCUMENTATION")
print("-" * 30)

def well_documented_function(param1, param2):
    """
    This is a well-documented function.
    
    This function demonstrates proper documentation using docstrings.
    
    Args:
        param1 (str): The first parameter
        param2 (int): The second parameter
        
    Returns:
        str: A formatted string with the parameters
        
    Raises:
        ValueError: If param2 is negative
        
    Example:
        >>> well_documented_function("Hello", 42)
        'Hello 42'
    """
    if param2 < 0:
        raise ValueError("param2 cannot be negative")
    
    return f"{param1} {param2}"

# 7. NESTED FUNCTION DEFINITIONS
print("\n7. NESTED FUNCTION DEFINITIONS")
print("-" * 30)

def outer_function(x):
    """Outer function that contains a nested function."""
    
    def inner_function(y):
        """Inner function defined inside outer function."""
        return x + y  # Can access x from outer function
    
    return inner_function

# Function that returns a function
def create_multiplier(factor):
    """Create a function that multiplies by a factor."""
    
    def multiplier(x):
        return x * factor
    
    return multiplier

# 8. LAMBDA FUNCTIONS (ANONYMOUS)
print("\n8. LAMBDA FUNCTIONS (ANONYMOUS)")
print("-" * 30)

# Lambda function definition
square = lambda x: x ** 2

# Lambda with multiple parameters
add = lambda x, y: x + y

# Lambda with conditional expression
absolute = lambda x: x if x >= 0 else -x

# Lambda with no parameters
get_pi = lambda: 3.14159

# 9. FUNCTION DEFINITION PATTERNS
print("\n9. FUNCTION DEFINITION PATTERNS")
print("-" * 30)

# Pattern 1: Simple utility function
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

# Pattern 2: Data processing function
def process_data(data_list):
    """Process a list of data."""
    if not data_list:
        return []
    
    processed = []
    for item in data_list:
        if isinstance(item, (int, float)):
            processed.append(item * 2)
        else:
            processed.append(str(item).upper())
    
    return processed

# Pattern 3: Configuration function
def create_config(debug=False, timeout=30, max_retries=3):
    """Create a configuration dictionary."""
    return {
        "debug": debug,
        "timeout": timeout,
        "max_retries": max_retries
    }

# Pattern 4: Factory function
def create_greeter(greeting="Hello"):
    """Create a greeter function."""
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

# 10. ADVANCED FUNCTION DEFINITIONS
print("\n10. ADVANCED FUNCTION DEFINITIONS")
print("-" * 30)

# Function with type hints
def typed_function(name: str, age: int) -> str:
    """Function with type hints."""
    return f"{name} is {age} years old"

# Function with complex parameters
def complex_function(
    required_param,
    default_param="default",
    *args,
    keyword_only,
    **kwargs
):
    """Function with complex parameter structure."""
    print(f"Required: {required_param}")
    print(f"Default: {default_param}")
    print(f"Args: {args}")
    print(f"Keyword only: {keyword_only}")
    print(f"Kwargs: {kwargs}")

# Generator function
def number_generator(start, end):
    """Generate numbers from start to end."""
    for i in range(start, end + 1):
        yield i

# 11. FUNCTION DEFINITION BEST PRACTICES
print("\n11. FUNCTION DEFINITION BEST PRACTICES")
print("-" * 30)

# Good: Clear, descriptive names
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# Good: Single responsibility
def validate_email(email):
    """Validate email format."""
    return '@' in email and '.' in email.split('@')[1]

# Good: Proper error handling
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Good: Use type hints
def process_user_data(user_id: int, name: str, age: int = 0) -> dict:
    """Process user data with type hints."""
    return {
        "id": user_id,
        "name": name,
        "age": age
    }

# 12. COMMON FUNCTION DEFINITION PATTERNS
print("\n12. COMMON FUNCTION DEFINITION PATTERNS")
print("-" * 30)

# Pattern 1: Validation functions
def is_valid_age(age):
    """Validate if age is reasonable."""
    return 0 <= age <= 150

def is_valid_email(email):
    """Validate email format."""
    return '@' in email and '.' in email.split('@')[1]

# Pattern 2: Transformation functions
def capitalize_words(text):
    """Capitalize each word in a string."""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

# Pattern 3: Calculation functions
def calculate_tax(income, rate=0.15):
    """Calculate tax based on income and rate."""
    return income * rate

def calculate_discount(price, discount_percent):
    """Calculate discounted price."""
    discount = price * (discount_percent / 100)
    return price - discount

# Pattern 4: Utility functions
def format_currency(amount, currency="USD"):
    """Format amount as currency."""
    return f"{currency} {amount:.2f}"

def format_percentage(value, total):
    """Format value as percentage of total."""
    if total == 0:
        return "0%"
    percentage = (value / total) * 100
    return f"{percentage:.1f}%"

# 13. FUNCTION DEFINITION EXAMPLES
print("\n13. FUNCTION DEFINITION EXAMPLES")
print("-" * 30)

# Example 1: String manipulation
def count_words(text):
    """Count words in a text."""
    if not text:
        return 0
    return len(text.split())

def find_longest_word(text):
    """Find the longest word in a text."""
    if not text:
        return ""
    words = text.split()
    return max(words, key=len)

# Example 2: List processing
def filter_even_numbers(numbers):
    """Filter even numbers from a list."""
    return [num for num in numbers if num % 2 == 0]

def sort_by_length(items):
    """Sort items by their length."""
    return sorted(items, key=len)

# Example 3: Dictionary operations
def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries."""
    result = dict1.copy()
    result.update(dict2)
    return result

def get_dict_stats(data):
    """Get statistics about a dictionary."""
    if not data:
        return {"count": 0, "keys": [], "values": []}
    
    return {
        "count": len(data),
        "keys": list(data.keys()),
        "values": list(data.values())
    }

# 14. SUMMARY
print("\n14. SUMMARY")
print("-" * 30)

print("Function Definition Syntax:")
print("def function_name(parameters):")
print("    function_body")
print("    return value  # optional")

print("\nKey Components:")
print("1. def keyword")
print("2. Function name (descriptive)")
print("3. Parameters (optional)")
print("4. Colon (:)")
print("5. Indented function body")
print("6. return statement (optional)")

print("\nParameter Types:")
print("- Required parameters")
print("- Default parameters")
print("- *args (arbitrary positional)")
print("- **kwargs (arbitrary keyword)")
print("- Keyword-only parameters")
print("- Positional-only parameters")

print("\nBest Practices:")
print("- Use descriptive function names")
print("- Include docstrings")
print("- Use type hints when possible")
print("- Keep functions focused and small")
print("- Handle errors appropriately")
print("- Use meaningful parameter names")
print("- Follow PEP 8 style guidelines") 