"""
23. How do you use list comprehensions in Python?

List comprehensions in Python provide a concise way to create lists based on
existing sequences or iterables. They are more readable and often more efficient
than traditional for loops for creating lists.
"""

print("=== LIST COMPREHENSIONS IN PYTHON ===\n")

# 1. BASIC LIST COMPREHENSION SYNTAX
print("1. BASIC LIST COMPREHENSION SYNTAX")
print("-" * 30)

# Basic syntax: [expression for item in iterable]

# Simple list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared}")

# List comprehension with range
squares = [x ** 2 for x in range(5)]
print(f"Squares from range(5): {squares}")

# List comprehension with strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Original words: {words}")
print(f"Upper words: {upper_words}")

# 2. LIST COMPREHENSION WITH CONDITIONS
print("\n2. LIST COMPREHENSION WITH CONDITIONS")
print("-" * 30)

# Basic condition: [expression for item in iterable if condition]

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

# Filter positive numbers
mixed_numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = [x for x in mixed_numbers if x > 0]
print(f"Mixed numbers: {mixed_numbers}")
print(f"Positive numbers: {positive_numbers}")

# Filter strings by length
words = ["cat", "dog", "elephant", "ant", "giraffe"]
long_words = [word for word in words if len(word) > 3]
print(f"All words: {words}")
print(f"Long words: {long_words}")

# 3. NESTED LIST COMPREHENSIONS
print("\n3. NESTED LIST COMPREHENSIONS")
print("-" * 30)

# Nested comprehension: [expression for item in iterable for subitem in item]

# Flatten a list of lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(f"Nested list: {nested_list}")
print(f"Flattened list: {flattened}")

# Create a matrix
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"3x3 matrix: {matrix}")

# Nested comprehension with condition
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_numbers = [item for sublist in numbers for item in sublist if item % 2 == 0]
print(f"Even numbers from nested list: {even_numbers}")

# 4. LIST COMPREHENSION WITH MULTIPLE CONDITIONS
print("\n4. LIST COMPREHENSION WITH MULTIPLE CONDITIONS")
print("-" * 30)

# Multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [x for x in numbers if x % 2 == 0 and x > 5]
print(f"Numbers divisible by 2 and greater than 5: {filtered}")

# Multiple conditions with different logic
words = ["apple", "banana", "cherry", "date", "elderberry"]
filtered_words = [word for word in words if len(word) > 4 and 'a' in word]
print(f"Words longer than 4 chars and containing 'a': {filtered_words}")

# 5. LIST COMPREHENSION WITH EXPRESSIONS
print("\n5. LIST COMPREHENSION WITH EXPRESSIONS")
print("-" * 30)

# Complex expressions
numbers = [1, 2, 3, 4, 5]
result = [x * 2 if x % 2 == 0 else x * 3 for x in numbers]
print(f"Original numbers: {numbers}")
print(f"Even numbers doubled, odd numbers tripled: {result}")

# String operations
names = ["alice", "bob", "charlie", "david"]
formatted_names = [name.capitalize() + "!" for name in names]
print(f"Original names: {names}")
print(f"Formatted names: {formatted_names}")

# Mathematical operations
coordinates = [(1, 2), (3, 4), (5, 6)]
distances = [(x**2 + y**2)**0.5 for x, y in coordinates]
print(f"Coordinates: {coordinates}")
print(f"Distances from origin: {distances}")

# 6. LIST COMPREHENSION VS FOR LOOPS
print("\n6. LIST COMPREHENSION VS FOR LOOPS")
print("-" * 30)

# Traditional for loop
numbers = [1, 2, 3, 4, 5]
squared_traditional = []
for num in numbers:
    squared_traditional.append(num ** 2)

# List comprehension
squared_comprehension = [num ** 2 for num in numbers]

print(f"Traditional for loop result: {squared_traditional}")
print(f"List comprehension result: {squared_comprehension}")
print(f"Results are equal: {squared_traditional == squared_comprehension}")

# Performance comparison
import time

# Test traditional for loop
start = time.time()
result_traditional = []
for i in range(100000):
    result_traditional.append(i ** 2)
traditional_time = time.time() - start

# Test list comprehension
start = time.time()
result_comprehension = [i ** 2 for i in range(100000)]
comprehension_time = time.time() - start

print(f"Traditional for loop time: {traditional_time:.4f} seconds")
print(f"List comprehension time: {comprehension_time:.4f} seconds")

# 7. PRACTICAL EXAMPLES
print("\n7. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Data processing
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
processed_data = [x * 1.5 if x < 50 else x * 0.8 for x in data]
print(f"Original data: {data}")
print(f"Processed data: {processed_data}")

# Example 2: Text processing
text = "Hello World Python Programming"
words = text.split()
word_lengths = [len(word) for word in words]
print(f"Text: {text}")
print(f"Word lengths: {word_lengths}")

# Example 3: Dictionary processing
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95}
]

high_achievers = [student["name"] for student in students if student["grade"] >= 90]
print(f"High achievers: {high_achievers}")

# 8. ADVANCED LIST COMPREHENSIONS
print("\n8. ADVANCED LIST COMPREHENSIONS")
print("-" * 30)

# Multiple iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = [(x, y) for x in list1 for y in list2]
print(f"Combined lists: {combined}")

# Conditional expressions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
categorized = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Number categorization: {categorized}")

# Nested conditions
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [
    "small" if x < 5 else "medium" if x < 8 else "large"
    for x in data
]
print(f"Size categorization: {result}")

# 9. LIST COMPREHENSION WITH FUNCTIONS
print("\n9. LIST COMPREHENSION WITH FUNCTIONS")
print("-" * 30)

# Using built-in functions
numbers = [1, 2, 3, 4, 5]
squared = [pow(x, 2) for x in numbers]
print(f"Squared using pow(): {squared}")

# Using custom functions
def process_number(x):
    return x * 2 + 1

processed = [process_number(x) for x in numbers]
print(f"Processed numbers: {processed}")

# Using lambda functions
squared_lambda = [(lambda x: x ** 2)(x) for x in numbers]
print(f"Squared using lambda: {squared_lambda}")

# 10. LIST COMPREHENSION PATTERNS
print("\n10. LIST COMPREHENSION PATTERNS")
print("-" * 30)

# Pattern 1: Transformation
original = [1, 2, 3, 4, 5]
transformed = [x * 2 for x in original]
print(f"Transformation pattern: {transformed}")

# Pattern 2: Filtering
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [x for x in all_numbers if x % 2 == 0]
print(f"Filtering pattern: {filtered}")

# Pattern 3: Combination
combined = [x * 2 for x in all_numbers if x % 2 == 0]
print(f"Combination pattern: {combined}")

# Pattern 4: Nested iteration
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [cell for row in matrix for cell in row]
print(f"Nested iteration pattern: {flattened}")

# 11. LIST COMPREHENSION BEST PRACTICES
print("\n11. LIST COMPREHENSION BEST PRACTICES")
print("-" * 30)

print("Best Practices:")
print("1. Keep comprehensions readable")
print("2. Use for simple transformations")
print("3. Avoid deeply nested comprehensions")
print("4. Use descriptive variable names")
print("5. Consider using traditional loops for complex logic")
print("6. Test comprehensions thoroughly")

# Good comprehension
good_comprehension = [x * 2 for x in range(5) if x % 2 == 0]

# Avoid overly complex comprehensions
# bad_comprehension = [x * 2 if x % 2 == 0 else x * 3 for x in range(10) if x > 5 and x < 8]

# 12. COMMON MISTAKES
print("\n12. COMMON MISTAKES")
print("-" * 30)

# Mistake 1: Forgetting the expression
# wrong = [for x in range(5)]  # This will cause a syntax error

# Mistake 2: Using wrong variable names
numbers = [1, 2, 3, 4, 5]
# This works but is confusing
confusing = [x for x in numbers if x % 2 == 0]

# Better approach
clear = [num for num in numbers if num % 2 == 0]

# Mistake 3: Overly complex comprehensions
# Avoid this:
# complex = [x * 2 if x % 2 == 0 else x * 3 for x in range(10) if x > 5]

# Use this instead:
def process_number(x):
    if x % 2 == 0:
        return x * 2
    else:
        return x * 3

clear_comprehension = [process_number(x) for x in range(10) if x > 5]

# 13. LIST COMPREHENSION WITH DIFFERENT DATA TYPES
print("\n13. LIST COMPREHENSION WITH DIFFERENT DATA TYPES")
print("-" * 30)

# Tuples
coordinates = [(1, 2), (3, 4), (5, 6)]
x_coords = [coord[0] for coord in coordinates]
print(f"X coordinates: {x_coords}")

# Dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
names = [person["name"] for person in people]
ages = [person["age"] for person in people]
print(f"Names: {names}")
print(f"Ages: {ages}")

# Sets
numbers_set = {1, 2, 3, 4, 5}
squared_set = [x ** 2 for x in numbers_set]
print(f"Squared from set: {squared_set}")

# 14. PERFORMANCE CONSIDERATIONS
print("\n14. PERFORMANCE CONSIDERATIONS")
print("-" * 30)

# Memory efficiency
def memory_efficient():
    """Demonstrate memory efficiency."""
    # Generator expression (memory efficient)
    generator = (x ** 2 for x in range(1000000))
    
    # List comprehension (uses more memory)
    list_comp = [x ** 2 for x in range(1000000)]
    
    print("Generator expression uses less memory")
    print("List comprehension stores all values in memory")

# When to use each
print("Use list comprehension when:")
print("- You need all values at once")
print("- You need to iterate multiple times")
print("- You need list methods")

print("Use generator expression when:")
print("- You only need to iterate once")
print("- Memory is a concern")
print("- You're processing large datasets")

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What are List Comprehensions?")
print("- Concise way to create lists")
print("- Based on existing sequences")
print("- More readable than for loops")
print("- Often more efficient")

print("\nBasic Syntax:")
print("- [expression for item in iterable]")
print("- [expression for item in iterable if condition]")
print("- [expression for item in iterable for subitem in item]")

print("\nCommon Use Cases:")
print("- Data transformation")
print("- Filtering data")
print("- Creating lists from iterables")
print("- Mathematical operations")
print("- String processing")

print("\nBenefits:")
print("- More readable than for loops")
print("- Often more efficient")
print("- Functional programming style")
print("- Concise syntax")

print("\nBest Practices:")
print("- Keep comprehensions simple")
print("- Use descriptive variable names")
print("- Avoid deeply nested comprehensions")
print("- Use traditional loops for complex logic")
print("- Test thoroughly")

print("\nWhen to Use:")
print("- Simple transformations")
print("- Filtering data")
print("- Creating lists from iterables")
print("- Mathematical operations")
print("- When readability is important")

print("\nWhen to Avoid:")
print("- Complex logic")
print("- Deeply nested operations")
print("- When traditional loops are clearer")
print("- When performance is critical")
print("- When debugging is difficult") 