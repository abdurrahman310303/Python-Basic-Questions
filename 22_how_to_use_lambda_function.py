"""
22. How do you use lambda functions in Python?

Lambda functions in Python are small, anonymous functions that can have any number
of arguments but only one expression. They are useful for simple operations and
are often used with higher-order functions like map(), filter(), and reduce().
"""

print("=== LAMBDA FUNCTIONS IN PYTHON ===\n")

# 1. BASIC LAMBDA SYNTAX
print("1. BASIC LAMBDA SYNTAX")
print("-" * 30)

# Basic lambda function
add = lambda x, y: x + y
print(f"Lambda add(5, 3): {add(5, 3)}")

# Lambda with single argument
square = lambda x: x ** 2
print(f"Lambda square(4): {square(4)}")

# Lambda with no arguments
get_hello = lambda: "Hello, World!"
print(f"Lambda get_hello(): {get_hello()}")

# Lambda with default arguments
multiply = lambda x, y=2: x * y
print(f"Lambda multiply(3): {multiply(3)}")
print(f"Lambda multiply(3, 4): {multiply(3, 4)}")

# 2. LAMBDA VS REGULAR FUNCTIONS
print("\n2. LAMBDA VS REGULAR FUNCTIONS")
print("-" * 30)

# Regular function
def add_function(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

print(f"Regular function: {add_function(5, 3)}")
print(f"Lambda function: {add_lambda(5, 3)}")

# Comparison
print(f"Functions are equal: {add_function(5, 3) == add_lambda(5, 3)}")

# 3. LAMBDA WITH CONDITIONAL EXPRESSIONS
print("\n3. LAMBDA WITH CONDITIONAL EXPRESSIONS")
print("-" * 30)

# Lambda with conditional expression
is_even = lambda x: True if x % 2 == 0 else False
print(f"is_even(4): {is_even(4)}")
print(f"is_even(7): {is_even(7)}")

# Lambda with multiple conditions
grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"grade(95): {grade(95)}")
print(f"grade(85): {grade(85)}")
print(f"grade(75): {grade(75)}")
print(f"grade(55): {grade(55)}")

# Lambda with comparison
is_positive = lambda x: x > 0
print(f"is_positive(5): {is_positive(5)}")
print(f"is_positive(-3): {is_positive(-3)}")

# 4. LAMBDA WITH HIGHER-ORDER FUNCTIONS
print("\n4. LAMBDA WITH HIGHER-ORDER FUNCTIONS")
print("-" * 30)

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared}")

# Lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Lambda with sorted()
names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda x: len(x))
print(f"Original names: {names}")
print(f"Sorted by length: {sorted_names}")

# Lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product}")

# 5. PRACTICAL LAMBDA EXAMPLES
print("\n5. PRACTICAL LAMBDA EXAMPLES")
print("-" * 30)

# Example 1: Sorting with custom key
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 19, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78}
]

# Sort by age
sorted_by_age = sorted(students, key=lambda s: s["age"])
print(f"Sorted by age: {sorted_by_age}")

# Sort by grade (descending)
sorted_by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print(f"Sorted by grade (descending): {sorted_by_grade}")

# Example 2: Data transformation
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers and square them
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, data)))
print(f"Even numbers squared: {result}")

# Example 3: String operations
words = ["python", "lambda", "function", "programming"]
capitalized = list(map(lambda word: word.upper(), words))
print(f"Capitalized words: {capitalized}")

# 6. LAMBDA WITH MULTIPLE ARGUMENTS
print("\n6. LAMBDA WITH MULTIPLE ARGUMENTS")
print("-" * 30)

# Lambda with multiple arguments
calculate = lambda x, y, z: x * y + z
print(f"calculate(2, 3, 1): {calculate(2, 3, 1)}")

# Lambda with unpacking
points = [(1, 2), (3, 4), (5, 6)]
distances = list(map(lambda p: (p[0] ** 2 + p[1] ** 2) ** 0.5, points))
print(f"Points: {points}")
print(f"Distances from origin: {distances}")

# Lambda with multiple operations
process_data = lambda x, y: (x + y, x - y, x * y)
result = process_data(10, 3)
print(f"process_data(10, 3): {result}")

# 7. LAMBDA WITH CLOSURES
print("\n7. LAMBDA WITH CLOSURES")
print("-" * 30)

# Lambda with closure
def create_multiplier(factor):
    return lambda x: x * factor

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")

# Lambda with multiple closures
def create_calculator(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "multiply":
        return lambda x, y: x * y
    elif operation == "power":
        return lambda x, y: x ** y
    else:
        return lambda x, y: x

add_func = create_calculator("add")
multiply_func = create_calculator("multiply")
power_func = create_calculator("power")

print(f"add_func(3, 4): {add_func(3, 4)}")
print(f"multiply_func(3, 4): {multiply_func(3, 4)}")
print(f"power_func(2, 3): {power_func(2, 3)}")

# 8. LAMBDA WITH BUILT-IN FUNCTIONS
print("\n8. LAMBDA WITH BUILT-IN FUNCTIONS")
print("-" * 30)

# Lambda with max()
numbers = [3, 7, 2, 9, 1, 8]
max_number = max(numbers, key=lambda x: x)
print(f"Max number: {max_number}")

# Lambda with min()
min_number = min(numbers, key=lambda x: x)
print(f"Min number: {min_number}")

# Lambda with any()
has_even = any(lambda x: x % 2 == 0, numbers)
print(f"Has even number: {has_even}")

# Lambda with all()
all_positive = all(lambda x: x > 0, numbers)
print(f"All positive: {all_positive}")

# 9. ADVANCED LAMBDA PATTERNS
print("\n9. ADVANCED LAMBDA PATTERNS")
print("-" * 30)

# Pattern 1: Lambda with default values
create_greeting = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(f"create_greeting('Alice'): {create_greeting('Alice')}")
print(f"create_greeting('Bob', 'Hi'): {create_greeting('Bob', 'Hi')}")

# Pattern 2: Lambda with unpacking
process_coordinates = lambda x, y, z: f"Point({x}, {y}, {z})"
coords = (1, 2, 3)
result = process_coordinates(*coords)
print(f"process_coordinates{coords}: {result}")

# Pattern 3: Lambda with conditional logic
classify_number = lambda x: (
    "positive" if x > 0 else
    "negative" if x < 0 else
    "zero"
)
print(f"classify_number(5): {classify_number(5)}")
print(f"classify_number(-3): {classify_number(-3)}")
print(f"classify_number(0): {classify_number(0)}")

# 10. LAMBDA WITH DATA STRUCTURES
print("\n10. LAMBDA WITH DATA STRUCTURES")
print("-" * 30)

# Lambda with lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter and map in one line
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
even_squares_lambda = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(f"Even squares (list comprehension): {even_squares}")
print(f"Even squares (lambda): {even_squares_lambda}")

# Lambda with dictionaries
people = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Boston"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Sort by different keys
sort_by_age = sorted(people, key=lambda p: p["age"])
sort_by_name = sorted(people, key=lambda p: p["name"])
sort_by_city = sorted(people, key=lambda p: p["city"])

print(f"Sorted by age: {sort_by_age}")
print(f"Sorted by name: {sort_by_name}")
print(f"Sorted by city: {sort_by_city}")

# 11. LAMBDA PERFORMANCE CONSIDERATIONS
print("\n11. LAMBDA PERFORMANCE CONSIDERATIONS")
print("-" * 30)

import time

# Performance comparison
def regular_function(x):
    return x ** 2

lambda_function = lambda x: x ** 2

# Test regular function
start = time.time()
for i in range(1000000):
    regular_function(i)
regular_time = time.time() - start

# Test lambda function
start = time.time()
for i in range(1000000):
    lambda_function(i)
lambda_time = time.time() - start

print(f"Regular function time: {regular_time:.4f} seconds")
print(f"Lambda function time: {lambda_time:.4f} seconds")

# 12. LAMBDA BEST PRACTICES
print("\n12. LAMBDA BEST PRACTICES")
print("-" * 30)

print("Lambda Best Practices:")
print("1. Keep lambdas simple and readable")
print("2. Use lambdas for simple operations")
print("3. Use regular functions for complex logic")
print("4. Avoid deeply nested lambdas")
print("5. Use descriptive variable names")
print("6. Consider readability over brevity")

# Good lambda usage
good_lambda = lambda x: x * 2  # Simple and clear

# Avoid complex lambdas
# bad_lambda = lambda x: (x * 2 if x > 0 else x * 3) if x % 2 == 0 else (x + 1 if x < 10 else x - 1)

# 13. COMMON LAMBDA PATTERNS
print("\n13. COMMON LAMBDA PATTERNS")
print("-" * 30)

# Pattern 1: Simple transformation
transform = lambda x: x.upper()
names = ["alice", "bob", "charlie"]
upper_names = list(map(transform, names))
print(f"Upper names: {upper_names}")

# Pattern 2: Filtering
is_adult = lambda age: age >= 18
ages = [15, 20, 17, 25, 16, 30]
adults = list(filter(is_adult, ages))
print(f"Adults: {adults}")

# Pattern 3: Custom sorting
sort_by_length = lambda items: sorted(items, key=lambda x: len(x))
words = ["cat", "dog", "elephant", "ant", "giraffe"]
sorted_words = sort_by_length(words)
print(f"Words sorted by length: {sorted_words}")

# 14. LAMBDA DEBUGGING
print("\n14. LAMBDA DEBUGGING")
print("-" * 30)

# Debugging lambdas
def debug_lambda(func, *args):
    """Debug a lambda function."""
    try:
        result = func(*args)
        print(f"Lambda result: {result}")
        return result
    except Exception as e:
        print(f"Lambda error: {e}")
        return None

# Test lambda debugging
test_lambda = lambda x, y: x / y
debug_lambda(test_lambda, 10, 2)
debug_lambda(test_lambda, 10, 0)  # This will cause an error

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What are Lambda Functions?")
print("- Anonymous functions")
print("- Single expression")
print("- Can have multiple arguments")
print("- Return value automatically")

print("\nLambda Syntax:")
print("- lambda arguments: expression")
print("- lambda x: x * 2")
print("- lambda x, y: x + y")
print("- lambda: 'Hello'")

print("\nCommon Use Cases:")
print("- Higher-order functions (map, filter, reduce)")
print("- Sorting with custom keys")
print("- Simple transformations")
print("- Quick calculations")
print("- Callback functions")

print("\nLambda Benefits:")
print("- Concise syntax")
print("- Inline function definition")
print("- Functional programming style")
print("- No function name needed")

print("\nLambda Limitations:")
print("- Single expression only")
print("- No statements allowed")
print("- Limited readability for complex logic")
print("- No docstrings")
print("- No annotations")

print("\nBest Practices:")
print("- Keep lambdas simple")
print("- Use for simple operations")
print("- Use regular functions for complex logic")
print("- Consider readability")
print("- Use descriptive variable names")
print("- Test thoroughly")

print("\nWhen to Use Lambdas:")
print("- Simple transformations")
print("- Filtering data")
print("- Custom sorting")
print("- Callback functions")
print("- One-time operations")
print("- Functional programming patterns") 