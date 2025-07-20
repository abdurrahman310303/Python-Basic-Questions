"""
4. What is the difference between a list and a tuple?

Lists and tuples are both sequence data types in Python, but they have key differences:
1. Mutability: Lists are mutable, tuples are immutable
2. Syntax: Lists use [], tuples use ()
3. Performance: Tuples are slightly faster
4. Use cases: Lists for dynamic data, tuples for fixed data
"""

print("=== LISTS vs TUPLES ===\n")

# 1. SYNTAX DIFFERENCES
print("1. SYNTAX DIFFERENCES")
print("-" * 30)

# List syntax
my_list = [1, 2, 3, 4, 5]
print(f"List syntax: {my_list} (type: {type(my_list)})")

# Tuple syntax
my_tuple = (1, 2, 3, 4, 5)
print(f"Tuple syntax: {my_tuple} (type: {type(my_tuple)})")

# Single element tuple (note the comma)
single_tuple = (42,)
print(f"Single element tuple: {single_tuple} (type: {type(single_tuple)})")

# 2. MUTABILITY - THE KEY DIFFERENCE
print("\n2. MUTABILITY - THE KEY DIFFERENCE")
print("-" * 30)

# Lists are MUTABLE (can be changed)
print("LISTS ARE MUTABLE:")
fruits_list = ["apple", "banana", "orange"]
print(f"Original list: {fruits_list}")

# Adding elements
fruits_list.append("grape")
fruits_list.insert(1, "mango")
print(f"After append and insert: {fruits_list}")

# Modifying elements
fruits_list[0] = "pear"
print(f"After modifying first element: {fruits_list}")

# Removing elements
fruits_list.remove("banana")
del fruits_list[1]
print(f"After removing elements: {fruits_list}")

# Tuples are IMMUTABLE (cannot be changed)
print("\nTUPLES ARE IMMUTABLE:")
coordinates = (10, 20)
print(f"Original tuple: {coordinates}")

# This would cause an error:
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment
# coordinates.append(30)  # AttributeError: 'tuple' object has no attribute 'append'

print("Attempting to modify tuple will cause errors!")
print("Tuples cannot be modified after creation.")

# 3. PERFORMANCE COMPARISON
print("\n3. PERFORMANCE COMPARISON")
print("-" * 30)

import time
import sys

# Memory usage comparison
list_memory = sys.getsizeof([1, 2, 3, 4, 5])
tuple_memory = sys.getsizeof((1, 2, 3, 4, 5))

print(f"Memory usage:")
print(f"  List: {list_memory} bytes")
print(f"  Tuple: {tuple_memory} bytes")

# Speed comparison
def test_list_creation():
    start = time.time()
    for _ in range(1000000):
        [1, 2, 3, 4, 5]
    return time.time() - start

def test_tuple_creation():
    start = time.time()
    for _ in range(1000000):
        (1, 2, 3, 4, 5)
    return time.time() - start

list_time = test_list_creation()
tuple_time = test_tuple_creation()

print(f"\nCreation speed (1 million iterations):")
print(f"  List creation: {list_time:.4f} seconds")
print(f"  Tuple creation: {tuple_time:.4f} seconds")
print(f"  Tuples are {list_time/tuple_time:.2f}x faster")

# 4. USE CASES
print("\n4. USE CASES")
print("-" * 30)

print("LISTS - Use when you need:")
print("- Dynamic collections that change over time")
print("- Storing data that needs to be modified")
print("- Building collections incrementally")

# Example: Shopping cart (changes over time)
shopping_cart = []
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
shopping_cart.remove("bread")
shopping_cart.append("cheese")
print(f"Shopping cart (list): {shopping_cart}")

print("\nTUPLES - Use when you need:")
print("- Fixed collections that don't change")
print("- Data that represents a single entity")
print("- Dictionary keys (tuples are hashable)")
print("- Return multiple values from functions")

# Example: Person coordinates (fixed)
person_location = (40.7128, -74.0060)  # New York coordinates
print(f"Person location (tuple): {person_location}")

# Example: RGB color (fixed)
rgb_color = (255, 128, 0)  # Orange
print(f"RGB color (tuple): {rgb_color}")

# 5. COMMON OPERATIONS
print("\n5. COMMON OPERATIONS")
print("-" * 30)

# Both support similar operations
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (1, 2, 3, 4, 5)

print("Common operations (both support):")
print(f"  Length: len(list) = {len(numbers_list)}, len(tuple) = {len(numbers_tuple)}")
print(f"  Indexing: list[0] = {numbers_list[0]}, tuple[0] = {numbers_tuple[0]}")
print(f"  Slicing: list[1:3] = {numbers_list[1:3]}, tuple[1:3] = {numbers_tuple[1:3]}")
print(f"  Concatenation: list + [6] = {numbers_list + [6]}")
print(f"  Repetition: tuple * 2 = {numbers_tuple * 2}")

# 6. CONVERSION BETWEEN LISTS AND TUPLES
print("\n6. CONVERSION BETWEEN LISTS AND TUPLES")
print("-" * 30)

# List to tuple
my_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(my_list)
print(f"List to tuple: {my_list} -> {converted_tuple}")

# Tuple to list
my_tuple = (1, 2, 3, 4, 5)
converted_list = list(my_tuple)
print(f"Tuple to list: {my_tuple} -> {converted_list}")

# 7. NESTED STRUCTURES
print("\n7. NESTED STRUCTURES")
print("-" * 30)

# Nested lists
matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Nested list (matrix): {matrix_list}")
print(f"Access element: matrix_list[1][1] = {matrix_list[1][1]}")

# Nested tuples
coordinates_list = [(0, 0), (1, 1), (2, 2)]
print(f"List of tuples: {coordinates_list}")

# Tuple of lists
tuple_of_lists = ([1, 2], [3, 4], [5, 6])
print(f"Tuple of lists: {tuple_of_lists}")

# 8. PRACTICAL EXAMPLES
print("\n8. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Function returning multiple values (tuple)
def get_user_info():
    return ("John", "Doe", 30, "john@example.com")

name, lastname, age, email = get_user_info()
print(f"Function returning tuple: {name} {lastname}, age {age}")

# Example 2: Dictionary with tuple keys
point_scores = {(0, 0): 10, (1, 1): 20, (2, 2): 30}
print(f"Dictionary with tuple keys: {point_scores}")

# Example 3: List for dynamic data
todo_list = []
todo_list.append("Learn Python")
todo_list.append("Practice coding")
todo_list.append("Build projects")
todo_list[1] = "Practice Python coding"
print(f"Dynamic todo list: {todo_list}")

# Example 4: Tuple for fixed data
person_info = ("Alice", "Johnson", 25, "Engineer")
print(f"Fixed person info: {person_info}")

# 9. WHEN TO USE WHICH
print("\n9. WHEN TO USE WHICH")
print("-" * 30)

print("USE LISTS WHEN:")
print("- You need to modify the collection")
print("- You're building a collection incrementally")
print("- You need to add/remove elements")
print("- You're storing homogeneous data that changes")

print("\nUSE TUPLES WHEN:")
print("- The data is fixed and won't change")
print("- You need to use it as a dictionary key")
print("- You're returning multiple values from a function")
print("- You want slightly better performance")
print("- The data represents a single logical entity")

# 10. SUMMARY
print("\n10. SUMMARY")
print("-" * 30)

print("Key Differences:")
print("┌─────────────┬─────────────┬─────────────┐")
print("│ Feature     │ List        │ Tuple       │")
print("├─────────────┼─────────────┼─────────────┤")
print("│ Syntax      │ [1, 2, 3]   │ (1, 2, 3)   │")
print("│ Mutability  │ Mutable     │ Immutable   │")
print("│ Performance │ Slower      │ Faster      │")
print("│ Memory      │ More memory │ Less memory │")
print("│ Use case    │ Dynamic     │ Fixed       │")
print("└─────────────┴─────────────┴─────────────┘")

print("\nRemember:")
print("- Lists: Use for collections that change")
print("- Tuples: Use for fixed collections")
print("- Both: Support similar operations (indexing, slicing, etc.)")
print("- Tuples: Can be used as dictionary keys")
print("- Lists: Cannot be used as dictionary keys") 