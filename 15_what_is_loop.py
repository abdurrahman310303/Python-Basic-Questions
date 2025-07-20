"""
15. What is a loop? What are the types of loops in Python?

A loop is a programming construct that allows you to execute a block of code
repeatedly. Python has two main types of loops: for loops and while loops.
"""

print("=== LOOPS IN PYTHON ===\n")

# 1. FOR LOOPS
print("1. FOR LOOPS")
print("-" * 30)

# Basic for loop with range
for i in range(5):
    print(f"Loop iteration {i}")

# For loop with list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with string
for char in "Python":
    print(f"Character: {char}")

# 2. WHILE LOOPS
print("\n2. WHILE LOOPS")
print("-" * 30)

# Basic while loop
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# While loop with condition
number = 10
while number > 0:
    print(f"Number: {number}")
    number -= 2

# 3. LOOP CONTROL STATEMENTS
print("\n3. LOOP CONTROL STATEMENTS")
print("-" * 30)

# Break statement
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(f"i = {i}")

# Continue statement
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# Pass statement
for i in range(5):
    if i == 2:
        pass  # Do nothing, just continue
    else:
        print(f"Processing: {i}")

# 4. NESTED LOOPS
print("\n4. NESTED LOOPS")
print("-" * 30)

# Nested for loops
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Creating a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end="  ")
    print()  # New line after each row

# 5. LOOPING THROUGH DIFFERENT DATA TYPES
print("\n5. LOOPING THROUGH DIFFERENT DATA TYPES")
print("-" * 30)

# Lists
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# Tuples
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# Dictionaries
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Sets
unique_numbers = {1, 2, 3, 4, 5}
for num in unique_numbers:
    print(f"Unique number: {num}")

# 6. ENUMERATE FUNCTION
print("\n6. ENUMERATE FUNCTION")
print("-" * 30)

# Enumerate with list
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Enumerate with start parameter
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit #{index}: {fruit}")

# 7. ZIP FUNCTION
print("\n7. ZIP FUNCTION")
print("-" * 30)

# Zip two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Zip with different lengths
list1 = [1, 2, 3]
list2 = ["a", "b"]
for item1, item2 in zip(list1, list2):
    print(f"{item1} - {item2}")

# 8. LIST COMPREHENSIONS
print("\n8. LIST COMPREHENSIONS")
print("-" * 30)

# Basic list comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# 9. GENERATOR EXPRESSIONS
print("\n9. GENERATOR EXPRESSIONS")
print("-" * 30)

# Generator expression (memory efficient)
squares_gen = (x**2 for x in range(5))
print(f"Generator: {squares_gen}")

# Converting generator to list
squares_list = list(squares_gen)
print(f"From generator: {squares_list}")

# 10. PRACTICAL EXAMPLES
print("\n10. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Finding maximum value
numbers = [3, 7, 2, 9, 1, 8]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum number: {max_num}")

# Example 2: Counting occurrences
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"Character count: {char_count}")

# Example 3: Filtering data
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95}
]

high_achievers = []
for student in students:
    if student["grade"] >= 90:
        high_achievers.append(student["name"])
print(f"High achievers: {high_achievers}")

# 11. ADVANCED LOOP PATTERNS
print("\n11. ADVANCED LOOP PATTERNS")
print("-" * 30)

# Pattern 1: Loop with else clause
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")

# Pattern 2: Infinite loop with break
def get_user_input():
    while True:
        user_input = input("Enter 'quit' to exit: ")
        if user_input.lower() == 'quit':
            break
        print(f"You entered: {user_input}")

# Pattern 3: Loop with enumerate and conditional
fruits = ["apple", "banana", "orange", "grape"]
for index, fruit in enumerate(fruits):
    if index % 2 == 0:
        print(f"Even index {index}: {fruit}")

# 12. LOOP PERFORMANCE CONSIDERATIONS
print("\n12. LOOP PERFORMANCE CONSIDERATIONS")
print("-" * 30)

# Bad: Modifying list while iterating
numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # This can cause issues

# Good: Create new list
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(f"Odd numbers: {odd_numbers}")

# Using iterators for large datasets
def number_generator(n):
    for i in range(n):
        yield i

# Memory efficient iteration
for num in number_generator(1000000):
    if num > 10:
        break
    # Process number

# 13. COMMON LOOP IDIOMS
print("\n13. COMMON LOOP IDIOMS")
print("-" * 30)

# Idiom 1: Loop through range with step
for i in range(0, 10, 2):
    print(f"Even number: {i}")

# Idiom 2: Loop through reversed range
for i in range(5, 0, -1):
    print(f"Countdown: {i}")

# Idiom 3: Loop with multiple variables
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: ({x}, {y})")

# Idiom 4: Loop with index and value
fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits):
    print(f"Fruit {i+1}: {fruit}")

# 14. LOOP BEST PRACTICES
print("\n14. LOOP BEST PRACTICES")
print("-" * 30)

# Good: Use descriptive variable names
for student in students:
    print(f"Student: {student['name']}")

# Good: Use list comprehensions when appropriate
squares = [x**2 for x in range(5)]  # Instead of for loop

# Good: Use enumerate for index access
for index, item in enumerate(items):
    print(f"Item {index}: {item}")

# Good: Use zip for parallel iteration
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("Types of Loops in Python:")
print("1. for loop - iterate over sequences")
print("2. while loop - repeat while condition is True")

print("\nLoop Control Statements:")
print("- break - exit the loop")
print("- continue - skip current iteration")
print("- pass - do nothing, continue")

print("\nLoop Functions:")
print("- range() - generate sequence of numbers")
print("- enumerate() - get index and value")
print("- zip() - iterate over multiple sequences")

print("\nLoop Comprehensions:")
print("- List comprehensions - create lists")
print("- Generator expressions - memory efficient")
print("- Dictionary comprehensions - create dictionaries")

print("\nBest Practices:")
print("- Use appropriate loop type for the task")
print("- Use list comprehensions for simple transformations")
print("- Use enumerate() when you need index")
print("- Use zip() for parallel iteration")
print("- Avoid modifying lists while iterating")
print("- Use descriptive variable names")
print("- Consider performance for large datasets") 