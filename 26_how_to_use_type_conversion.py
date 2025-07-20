"""
26. How do you use type conversion in Python?

Type conversion (also called type casting) in Python allows you to convert one
data type to another. Python provides built-in functions for converting between
different types, and you can also create custom conversion functions.
"""

print("=== TYPE CONVERSION IN PYTHON ===\n")

# 1. BASIC TYPE CONVERSION FUNCTIONS
print("1. BASIC TYPE CONVERSION FUNCTIONS")
print("-" * 30)

# Converting to int
print("Converting to int:")
print(f"int(3.14): {int(3.14)}")
print(f"int('42'): {int('42')}")
print(f"int(True): {int(True)}")
print(f"int(False): {int(False)}")

# Converting to float
print("\nConverting to float:")
print(f"float(42): {float(42)}")
print(f"float('3.14'): {float('3.14')}")
print(f"float(True): {float(True)}")

# Converting to str
print("\nConverting to str:")
print(f"str(42): '{str(42)}'")
print(f"str(3.14): '{str(3.14)}'")
print(f"str(True): '{str(True)}'")
print(f"str([1, 2, 3]): '{str([1, 2, 3])}'")

# Converting to bool
print("\nConverting to bool:")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

# 2. CONVERTING BETWEEN NUMERIC TYPES
print("\n2. CONVERTING BETWEEN NUMERIC TYPES")
print("-" * 30)

# Integer to float
integer_value = 42
float_value = float(integer_value)
print(f"Integer {integer_value} to float: {float_value}")

# Float to integer (truncates)
float_value = 3.14
integer_value = int(float_value)
print(f"Float {float_value} to integer: {integer_value}")

# Complex numbers
complex_value = complex(3, 4)
print(f"Complex number: {complex_value}")

# Converting from complex
real_part = complex_value.real
imaginary_part = complex_value.imag
print(f"Real part: {real_part}")
print(f"Imaginary part: {imaginary_part}")

# 3. CONVERTING STRINGS TO NUMBERS
print("\n3. CONVERTING STRINGS TO NUMBERS")
print("-" * 30)

# String to integer
print("String to integer:")
print(f"int('42'): {int('42')}")
print(f"int('1010', 2): {int('1010', 2)}")  # Binary
print(f"int('1A', 16): {int('1A', 16)}")    # Hexadecimal

# String to float
print("\nString to float:")
print(f"float('3.14'): {float('3.14')}")
print(f"float('42'): {float('42')}")
print(f"float('1.23e-4'): {float('1.23e-4')}")

# Error handling for invalid conversions
try:
    int("not_a_number")
except ValueError as e:
    print(f"Error converting 'not_a_number' to int: {e}")

# 4. CONVERTING SEQUENCES
print("\n4. CONVERTING SEQUENCES")
print("-" * 30)

# List to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List {my_list} to tuple: {my_tuple}")

# Tuple to list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(f"Tuple {my_tuple} to list: {my_list}")

# String to list (characters)
my_string = "Hello"
char_list = list(my_string)
print(f"String '{my_string}' to list: {char_list}")

# List to string
char_list = ['H', 'e', 'l', 'l', 'o']
my_string = ''.join(char_list)
print(f"List {char_list} to string: '{my_string}'")

# 5. CONVERTING TO AND FROM DICTIONARIES
print("\n5. CONVERTING TO AND FROM DICTIONARIES")
print("-" * 30)

# List of tuples to dictionary
pairs = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(pairs)
print(f"List of tuples {pairs} to dict: {my_dict}")

# Dictionary to list of tuples
my_dict = {'a': 1, 'b': 2, 'c': 3}
pairs = list(my_dict.items())
print(f"Dict {my_dict} to list of tuples: {pairs}")

# Dictionary keys and values
keys = list(my_dict.keys())
values = list(my_dict.values())
print(f"Dict keys: {keys}")
print(f"Dict values: {values}")

# 6. CONVERTING TO SETS
print("\n6. CONVERTING TO SETS")
print("-" * 30)

# List to set
my_list = [1, 2, 2, 3, 3, 4, 5, 5]
my_set = set(my_list)
print(f"List {my_list} to set: {my_set}")

# Tuple to set
my_tuple = (1, 2, 2, 3, 3, 4)
my_set = set(my_tuple)
print(f"Tuple {my_tuple} to set: {my_set}")

# String to set (unique characters)
my_string = "hello"
char_set = set(my_string)
print(f"String '{my_string}' to set: {char_set}")

# Set back to list
my_list = list(my_set)
print(f"Set {my_set} back to list: {my_list}")

# 7. CONVERTING TO AND FROM BYTES
print("\n7. CONVERTING TO AND FROM BYTES")
print("-" * 30)

# String to bytes
my_string = "Hello, World!"
my_bytes = my_string.encode('utf-8')
print(f"String '{my_string}' to bytes: {my_bytes}")

# Bytes to string
my_string = my_bytes.decode('utf-8')
print(f"Bytes {my_bytes} to string: '{my_string}'")

# Integer to bytes
integer_value = 12345
bytes_value = integer_value.to_bytes(4, byteorder='big')
print(f"Integer {integer_value} to bytes: {bytes_value}")

# Bytes to integer
integer_value = int.from_bytes(bytes_value, byteorder='big')
print(f"Bytes {bytes_value} to integer: {integer_value}")

# 8. CUSTOM TYPE CONVERSION
print("\n8. CUSTOM TYPE CONVERSION")
print("-" * 30)

# Custom conversion function
def convert_to_percentage(value):
    """Convert various types to percentage string."""
    if isinstance(value, (int, float)):
        return f"{value * 100}%"
    elif isinstance(value, str):
        try:
            num = float(value)
            return f"{num * 100}%"
        except ValueError:
            return "Invalid input"
    else:
        return "Cannot convert"

# Testing custom conversion
print(f"convert_to_percentage(0.5): {convert_to_percentage(0.5)}")
print(f"convert_to_percentage(0.75): {convert_to_percentage(0.75)}")
print(f"convert_to_percentage('0.25'): {convert_to_percentage('0.25')}")
print(f"convert_to_percentage('invalid'): {convert_to_percentage('invalid')}")

# Custom class with conversion methods
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
    def __str__(self):
        return f"{self.celsius}°C"

# Using custom conversion
temp = Temperature(25)
print(f"Temperature: {temp}")
print(f"To Fahrenheit: {temp.to_fahrenheit():.1f}°F")
print(f"To Kelvin: {temp.to_kelvin():.1f}K")

# 9. IMPLICIT TYPE CONVERSION
print("\n9. IMPLICIT TYPE CONVERSION")
print("-" * 30)

# Numeric operations
print("Numeric operations:")
print(f"5 + 3.14 = {5 + 3.14}")  # int + float = float
print(f"10 / 3 = {10 / 3}")      # int / int = float
print(f"10 // 3 = {10 // 3}")    # int // int = int

# Boolean operations
print("\nBoolean operations:")
print(f"True + 1 = {True + 1}")  # bool + int = int
print(f"False * 5 = {False * 5}") # bool * int = int

# String operations
print("\nString operations:")
print(f"'Number: ' + str(42) = {'Number: ' + str(42)}")

# 10. ERROR HANDLING IN TYPE CONVERSION
print("\n10. ERROR HANDLING IN TYPE CONVERSION")
print("-" * 30)

# Safe conversion function
def safe_convert(value, target_type, default=None):
    """Safely convert value to target type."""
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default

# Testing safe conversion
print(f"safe_convert('42', int): {safe_convert('42', int)}")
print(f"safe_convert('not_a_number', int): {safe_convert('not_a_number', int)}")
print(f"safe_convert('3.14', float): {safe_convert('3.14', float)}")
print(f"safe_convert('invalid', float): {safe_convert('invalid', float)}")

# 11. ADVANCED TYPE CONVERSION PATTERNS
print("\n11. ADVANCED TYPE CONVERSION PATTERNS")
print("-" * 30)

# Pattern 1: Converting list of strings to list of integers
string_numbers = ['1', '2', '3', '4', '5']
integer_numbers = [int(x) for x in string_numbers]
print(f"String numbers {string_numbers} to integers: {integer_numbers}")

# Pattern 2: Converting mixed types to strings
mixed_data = [1, 2.5, 'hello', True, None]
string_data = [str(x) for x in mixed_data]
print(f"Mixed data {mixed_data} to strings: {string_data}")

# Pattern 3: Converting dictionary values
data_dict = {'a': '1', 'b': '2', 'c': '3'}
converted_dict = {k: int(v) for k, v in data_dict.items()}
print(f"Dict with string values {data_dict} to integers: {converted_dict}")

# 12. TYPE CONVERSION WITH VALIDATION
print("\n12. TYPE CONVERSION WITH VALIDATION")
print("-" * 30)

def validate_and_convert(value, target_type, min_value=None, max_value=None):
    """Convert value with validation."""
    try:
        converted = target_type(value)
        
        if min_value is not None and converted < min_value:
            raise ValueError(f"Value {converted} is below minimum {min_value}")
        
        if max_value is not None and converted > max_value:
            raise ValueError(f"Value {converted} is above maximum {max_value}")
        
        return converted
    except (ValueError, TypeError) as e:
        raise ValueError(f"Cannot convert {value} to {target_type.__name__}: {e}")

# Testing validation
try:
    result = validate_and_convert('42', int, 0, 100)
    print(f"Valid conversion: {result}")
except ValueError as e:
    print(f"Validation error: {e}")

try:
    result = validate_and_convert('150', int, 0, 100)
    print(f"Valid conversion: {result}")
except ValueError as e:
    print(f"Validation error: {e}")

# 13. TYPE CONVERSION PERFORMANCE
print("\n13. TYPE CONVERSION PERFORMANCE")
print("-" * 30)

import time

# Performance comparison
def performance_test():
    # Test list comprehension
    start = time.time()
    for _ in range(100000):
        [int(x) for x in ['1', '2', '3', '4', '5']]
    list_comp_time = time.time() - start
    
    # Test map function
    start = time.time()
    for _ in range(100000):
        list(map(int, ['1', '2', '3', '4', '5']))
    map_time = time.time() - start
    
    print(f"List comprehension time: {list_comp_time:.4f} seconds")
    print(f"Map function time: {map_time:.4f} seconds")

# 14. TYPE CONVERSION BEST PRACTICES
print("\n14. TYPE CONVERSION BEST PRACTICES")
print("-" * 30)

print("Type Conversion Best Practices:")
print("1. Always handle conversion errors")
print("2. Use appropriate conversion functions")
print("3. Validate input before conversion")
print("4. Consider performance for large datasets")
print("5. Use explicit conversions when needed")
print("6. Document expected input types")
print("7. Test edge cases")

# Good conversion practices
def good_conversion_example(data):
    """Good conversion example with error handling."""
    try:
        if isinstance(data, str):
            return int(data)
        elif isinstance(data, (int, float)):
            return int(data)
        else:
            raise ValueError(f"Cannot convert {type(data)} to int")
    except (ValueError, TypeError) as e:
        print(f"Conversion error: {e}")
        return None

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What is Type Conversion?")
print("- Converting one data type to another")
print("- Using built-in conversion functions")
print("- Handling conversion errors")
print("- Creating custom conversion logic")

print("\nBuilt-in Conversion Functions:")
print("- int(): Convert to integer")
print("- float(): Convert to float")
print("- str(): Convert to string")
print("- bool(): Convert to boolean")
print("- list(): Convert to list")
print("- tuple(): Convert to tuple")
print("- set(): Convert to set")
print("- dict(): Convert to dictionary")

print("\nCommon Conversion Patterns:")
print("- String to number")
print("- Number to string")
print("- List to tuple/set")
print("- Dictionary to list")
print("- Custom object conversion")

print("\nError Handling:")
print("- Use try-except blocks")
print("- Provide default values")
print("- Validate input data")
print("- Handle edge cases")

print("\nBest Practices:")
print("- Always handle conversion errors")
print("- Use appropriate conversion functions")
print("- Validate input before conversion")
print("- Consider performance implications")
print("- Document expected types")
print("- Test thoroughly")

print("\nUse Cases:")
print("- Data processing")
print("- Input validation")
print("- API integration")
print("- Database operations")
print("- File I/O operations")
print("- User interface handling") 