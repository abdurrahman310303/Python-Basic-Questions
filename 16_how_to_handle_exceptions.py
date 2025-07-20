"""
16. How do you handle exceptions in Python?

Exception handling in Python allows you to gracefully handle errors and unexpected
situations in your code. Python uses try, except, else, and finally blocks.
"""

print("=== EXCEPTION HANDLING IN PYTHON ===\n")

# 1. BASIC TRY-EXCEPT BLOCK
print("1. BASIC TRY-EXCEPT BLOCK")
print("-" * 30)

# Simple exception handling
try:
    number = int("abc")
    print(f"Number: {number}")
except ValueError:
    print("Error: Could not convert string to integer")

# Another example
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero")

# 2. HANDLING MULTIPLE EXCEPTIONS
print("\n2. HANDLING MULTIPLE EXCEPTIONS")
print("-" * 30)

# Multiple except blocks
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Single except block with multiple exceptions
try:
    # Some risky operation
    data = [1, 2, 3]
    index = int(input("Enter index: "))
    print(f"Value: {data[index]}")
except (ValueError, IndexError) as e:
    print(f"Error: {e}")

# 3. EXCEPTION WITH ELSE CLAUSE
print("\n3. EXCEPTION WITH ELSE CLAUSE")
print("-" * 30)

try:
    number = int("42")
except ValueError:
    print("Error: Invalid number")
else:
    print(f"Successfully converted to: {number}")
    print("No exceptions occurred")

# Another example
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("Error: File not found")
else:
    content = file.read()
    file.close()
    print("File read successfully")

# 4. FINALLY CLAUSE
print("\n4. FINALLY CLAUSE")
print("-" * 30)

# Finally always executes
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid number")
finally:
    print("This always executes")

# Finally with file handling
try:
    file = open("temp_file.txt", "w")
    file.write("Hello, World!")
except IOError as e:
    print(f"Error writing file: {e}")
finally:
    file.close()
    print("File closed")

# Clean up
import os
if os.path.exists("temp_file.txt"):
    os.remove("temp_file.txt")

# 5. RAISING EXCEPTIONS
print("\n5. RAISING EXCEPTIONS")
print("-" * 30)

# Raising built-in exceptions
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# Raising custom exceptions
class AgeError(Exception):
    """Custom exception for age validation."""
    pass

def validate_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")
    if age > 150:
        raise AgeError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except AgeError as e:
    print(f"Age error: {e}")

# 6. CUSTOM EXCEPTIONS
print("\n6. CUSTOM EXCEPTIONS")
print("-" * 30)

class InsufficientFundsError(Exception):
    """Exception raised when account has insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds. Balance: ${balance}, Required: ${amount}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return amount

# Using custom exception
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Withdrawal failed: {e}")

# 7. EXCEPTION HIERARCHY
print("\n7. EXCEPTION HIERARCHY")
print("-" * 30)

# Catching specific exceptions
try:
    # Some operation that might fail
    data = [1, 2, 3]
    print(data[10])
except IndexError:
    print("Index out of range")
except KeyError:
    print("Key not found")
except TypeError:
    print("Type error occurred")
except Exception as e:
    print(f"Some other error: {e}")

# 8. PRACTICAL EXAMPLES
print("\n8. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Safe file reading
def read_file_safely(filename):
    """Read a file safely with exception handling."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except UnicodeDecodeError:
        return f"Error: Cannot decode file '{filename}'"
    except Exception as e:
        return f"Unexpected error: {e}"

# Example 2: Safe data conversion
def safe_convert_to_int(value):
    """Safely convert value to integer."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

# Example 3: Database-like operations
def get_user_by_id(user_id):
    """Simulate database lookup with exception handling."""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    
    try:
        return users[user_id]
    except KeyError:
        return None

# 9. CONTEXT MANAGERS (WITH STATEMENT)
print("\n9. CONTEXT MANAGERS (WITH STATEMENT)")
print("-" * 30)

# Using with statement for file handling
try:
    with open("temp_file.txt", "w") as file:
        file.write("Hello, World!")
    print("File written successfully")
except IOError as e:
    print(f"Error writing file: {e}")

# Reading the file
try:
    with open("temp_file.txt", "r") as file:
        content = file.read()
        print(f"File content: {content}")
except FileNotFoundError:
    print("File not found")

# Clean up
if os.path.exists("temp_file.txt"):
    os.remove("temp_file.txt")

# 10. ADVANCED EXCEPTION HANDLING
print("\n10. ADVANCED EXCEPTION HANDLING")
print("-" * 30)

# Exception chaining
def process_data(data):
    try:
        return int(data)
    except ValueError as e:
        raise RuntimeError("Failed to process data") from e

try:
    result = process_data("abc")
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Original error: {e.__cause__}")

# Exception groups (Python 3.11+)
def multiple_operations():
    errors = []
    
    try:
        int("abc")
    except ValueError as e:
        errors.append(e)
    
    try:
        1 / 0
    except ZeroDivisionError as e:
        errors.append(e)
    
    if errors:
        raise ExceptionGroup("Multiple errors occurred", errors)

# 11. EXCEPTION BEST PRACTICES
print("\n11. EXCEPTION BEST PRACTICES")
print("-" * 30)

# Good: Specific exception handling
def good_example():
    try:
        value = int("123")
        return value
    except ValueError:
        return None

# Good: Proper cleanup
def file_operation():
    file = None
    try:
        file = open("temp.txt", "w")
        file.write("data")
    except IOError:
        print("Error writing file")
    finally:
        if file:
            file.close()

# Good: Informative error messages
def divide_safely(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError(f"Cannot divide {a} by zero")

# 12. COMMON EXCEPTION PATTERNS
print("\n12. COMMON EXCEPTION PATTERNS")
print("-" * 30)

# Pattern 1: Try-except-else
def validate_and_process(data):
    try:
        number = int(data)
    except ValueError:
        return "Invalid number"
    else:
        return number * 2

# Pattern 2: Exception suppression
def safe_operation():
    try:
        risky_operation()
    except (ValueError, TypeError):
        pass  # Suppress specific exceptions

# Pattern 3: Retry mechanism
def retry_operation(max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return risky_operation()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            print(f"Attempt {attempt + 1} failed, retrying...")

# 13. DEBUGGING WITH EXCEPTIONS
print("\n13. DEBUGGING WITH EXCEPTIONS")
print("-" * 30)

import traceback

def debug_exception():
    try:
        # Some operation that might fail
        result = 10 / 0
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print("Full traceback:")
        traceback.print_exc()

# 14. SUMMARY
print("\n14. SUMMARY")
print("-" * 30)

print("Exception Handling Components:")
print("1. try - block of code that might raise an exception")
print("2. except - handles specific exceptions")
print("3. else - executes if no exception occurs")
print("4. finally - always executes, used for cleanup")
print("5. raise - manually raises exceptions")

print("\nCommon Built-in Exceptions:")
print("- ValueError - invalid value")
print("- TypeError - wrong type")
print("- IndexError - invalid index")
print("- KeyError - invalid key")
print("- FileNotFoundError - file not found")
print("- ZeroDivisionError - division by zero")
print("- AttributeError - attribute not found")

print("\nBest Practices:")
print("- Catch specific exceptions, not generic ones")
print("- Use finally for cleanup operations")
print("- Provide informative error messages")
print("- Don't suppress exceptions unless necessary")
print("- Use context managers (with statement)")
print("- Log exceptions for debugging")
print("- Handle exceptions at appropriate levels")

print("\nException Handling Flow:")
print("1. Code in try block executes")
print("2. If exception occurs, control goes to except")
print("3. If no exception, else block executes")
print("4. Finally block always executes")
print("5. Program continues after exception handling") 