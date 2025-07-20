"""
12. What is the use of the 'return' statement?

The 'return' statement in Python is used to exit a function and optionally send a value back
to the calling code. It terminates the function execution and returns control to the caller.
"""

print("=== THE RETURN STATEMENT IN PYTHON ===\n")

# 1. BASIC RETURN STATEMENT
print("1. BASIC RETURN STATEMENT")
print("-" * 30)

def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result

# Using the returned value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

# 2. RETURN WITHOUT VALUE
print("\n2. RETURN WITHOUT VALUE")
print("-" * 30)

def print_and_return_none():
    """Function that prints and returns None."""
    print("This function prints something")
    return  # Returns None implicitly

def early_exit(condition):
    """Function with early exit."""
    if condition:
        print("Condition is True, exiting early")
        return  # Early exit
    
    print("Condition is False, continuing...")
    print("More processing...")

# Testing early exit
early_exit(True)
early_exit(False)

# 3. MULTIPLE RETURN VALUES
print("\n3. MULTIPLE RETURN VALUES")
print("-" * 30)

def get_name_and_age():
    """Return multiple values as a tuple."""
    return "John", 25

# Unpacking multiple return values
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

def calculate_stats(numbers):
    """Return multiple statistics."""
    if not numbers:
        return 0, 0, 0  # count, sum, average
    
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    
    return count, total, average

stats = calculate_stats([1, 2, 3, 4, 5])
print(f"Count: {stats[0]}, Sum: {stats[1]}, Average: {stats[2]}")

# 4. CONDITIONAL RETURN
print("\n4. CONDITIONAL RETURN")
print("-" * 30)

def absolute_value(x):
    """Return absolute value of a number."""
    if x >= 0:
        return x
    else:
        return -x

print(f"Absolute value of 5: {absolute_value(5)}")
print(f"Absolute value of -5: {absolute_value(-5)}")

def check_even_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(f"7 is {check_even_odd(7)}")
print(f"8 is {check_even_odd(8)}")

# 5. RETURN IN LOOPS
print("\n5. RETURN IN LOOPS")
print("-" * 30)

def find_first_even(numbers):
    """Find the first even number in a list."""
    for num in numbers:
        if num % 2 == 0:
            return num  # Return immediately when found
    return None  # Return None if no even number found

numbers_list = [1, 3, 5, 8, 9, 10]
first_even = find_first_even(numbers_list)
print(f"First even number: {first_even}")

def search_item(items, target):
    """Search for an item and return its index."""
    for i, item in enumerate(items):
        if item == target:
            return i  # Return index immediately when found
    return -1  # Return -1 if not found

fruits = ["apple", "banana", "cherry"]
index = search_item(fruits, "banana")
print(f"Index of 'banana': {index}")

# 6. RETURN IN NESTED FUNCTIONS
print("\n6. RETURN IN NESTED FUNCTIONS")
print("-" * 30)

def outer_function(x):
    """Outer function that returns an inner function."""
    
    def inner_function(y):
        """Inner function that returns a calculation."""
        return x + y
    
    return inner_function  # Return the inner function

# Using the returned function
add_five = outer_function(5)
result = add_five(3)
print(f"Result: {result}")

def create_calculator(operation):
    """Create a calculator function based on operation."""
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    elif operation == "multiply":
        return multiply
    else:
        return None

# Using the calculator
calc = create_calculator("add")
if calc:
    result = calc(10, 5)
    print(f"10 + 5 = {result}")

# 7. RETURN WITH DIFFERENT DATA TYPES
print("\n7. RETURN WITH DIFFERENT DATA TYPES")
print("-" * 30)

def return_string():
    """Return a string."""
    return "Hello, World!"

def return_number():
    """Return a number."""
    return 42

def return_list():
    """Return a list."""
    return [1, 2, 3, 4, 5]

def return_dict():
    """Return a dictionary."""
    return {"name": "John", "age": 30}

def return_tuple():
    """Return a tuple."""
    return (1, 2, 3)

print(f"String: {return_string()}")
print(f"Number: {return_number()}")
print(f"List: {return_list()}")
print(f"Dictionary: {return_dict()}")
print(f"Tuple: {return_tuple()}")

# 8. RETURN IN EXCEPTION HANDLING
print("\n8. RETURN IN EXCEPTION HANDLING")
print("-" * 30)

def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    except TypeError:
        return "Error: Invalid types"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

def read_file_safely(filename):
    """Read a file and return its content."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Permission denied"

# 9. RETURN IN RECURSIVE FUNCTIONS
print("\n9. RETURN IN RECURSIVE FUNCTIONS")
print("-" * 30)

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

def fibonacci(n):
    """Calculate Fibonacci number using recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(6): {fibonacci(6)}")

# 10. RETURN WITH GENERATORS
print("\n10. RETURN WITH GENERATORS")
print("-" * 30)

def number_generator(start, end):
    """Generate numbers from start to end."""
    for i in range(start, end + 1):
        yield i
    return "Generator completed"  # This is the return value of the generator

# Using the generator
gen = number_generator(1, 5)
for num in gen:
    print(f"Generated: {num}")

# 11. RETURN IN CLASS METHODS
print("\n11. RETURN IN CLASS METHODS")
print("-" * 30)

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, x, y):
        """Add two numbers and return the result."""
        self.result = x + y
        return self.result
    
    def get_result(self):
        """Return the current result."""
        return self.result
    
    def reset(self):
        """Reset the calculator and return confirmation."""
        self.result = 0
        return "Calculator reset"

calc = Calculator()
result = calc.add(10, 5)
print(f"Calculator result: {result}")
print(f"Current result: {calc.get_result()}")
print(calc.reset())

# 12. RETURN BEST PRACTICES
print("\n12. RETURN BEST PRACTICES")
print("-" * 30)

# Good: Early return for simple cases
def validate_age(age):
    """Validate age with early return."""
    if age < 0:
        return False
    if age > 150:
        return False
    return True

# Good: Consistent return types
def process_data(data):
    """Process data with consistent return type."""
    if not data:
        return []  # Always return a list
    
    processed = []
    for item in data:
        processed.append(item * 2)
    return processed

# Good: Clear return values
def get_user_status(user_id):
    """Get user status with clear return values."""
    if user_id == 1:
        return "active"
    elif user_id == 2:
        return "inactive"
    else:
        return "unknown"

# 13. COMMON RETURN PATTERNS
print("\n13. COMMON RETURN PATTERNS")
print("-" * 30)

# Pattern 1: Success/Error pattern
def divide_numbers(a, b):
    """Divide numbers with success/error pattern."""
    try:
        result = a / b
        return {"success": True, "result": result}
    except ZeroDivisionError:
        return {"success": False, "error": "Division by zero"}

# Pattern 2: Default value pattern
def get_config_value(key, default=None):
    """Get configuration value with default."""
    config = {"debug": True, "timeout": 30}
    return config.get(key, default)

# Pattern 3: Boolean pattern
def is_valid_email(email):
    """Check if email is valid."""
    if '@' not in email:
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True

# Pattern 4: Optional pattern
def find_user(user_id):
    """Find user with optional return."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns None if not found

# 14. SUMMARY
print("\n14. SUMMARY")
print("-" * 30)

print("Key Points about Return Statement:")
print("1. Exits the function immediately")
print("2. Can return any data type")
print("3. Functions without return return None")
print("4. Can return multiple values as tuples")
print("5. Can be used for early exit")

print("\nReturn Statement Uses:")
print("- Send values back to caller")
print("- Exit function early")
print("- Return multiple values")
print("- Return functions (closures)")
print("- Return None for void functions")

print("\nBest Practices:")
print("- Use early returns for simple cases")
print("- Be consistent with return types")
print("- Return meaningful values")
print("- Handle all code paths")
print("- Use clear return values")
print("- Document return values in docstrings")

print("\nCommon Patterns:")
print("- Success/Error pattern")
print("- Default value pattern")
print("- Boolean pattern")
print("- Optional pattern")
print("- Multiple return pattern") 