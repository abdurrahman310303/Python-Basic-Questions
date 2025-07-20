"""
5. How do you create a dictionary in Python?

A dictionary in Python is a mutable, unordered collection of key-value pairs.
Dictionaries are created using curly braces {} or the dict() constructor.
"""

print("=== CREATING DICTIONARIES IN PYTHON ===\n")

# 1. BASIC DICTIONARY CREATION
print("1. BASIC DICTIONARY CREATION")
print("-" * 30)

# Method 1: Using curly braces {}
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Dictionary using {{}}: {person}")

# Method 2: Using dict() constructor
person2 = dict(name="Alice", age=25, city="Boston")
print(f"Dictionary using dict(): {person2}")

# Method 3: Using dict() with list of tuples
person3 = dict([("name", "Bob"), ("age", 35), ("city", "Chicago")])
print(f"Dictionary using dict() with tuples: {person3}")

# 2. DIFFERENT KEY AND VALUE TYPES
print("\n2. DIFFERENT KEY AND VALUE TYPES")
print("-" * 30)

# String keys with various value types
mixed_dict = {
    "string": "Hello World",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3, 4, 5],
    "tuple": (10, 20),
    "none": None
}
print(f"Mixed types dictionary: {mixed_dict}")

# Integer keys
number_dict = {
    1: "one",
    2: "two",
    3: "three"
}
print(f"Integer keys: {number_dict}")

# Tuple keys (tuples are immutable, so they can be keys)
tuple_dict = {
    (1, 2): "point1",
    (3, 4): "point2",
    (5, 6): "point3"
}
print(f"Tuple keys: {tuple_dict}")

# 3. NESTED DICTIONARIES
print("\n3. NESTED DICTIONARIES")
print("-" * 30)

# Dictionary containing other dictionaries
nested_dict = {
    "person1": {
        "name": "John",
        "age": 30,
        "skills": ["Python", "JavaScript", "SQL"]
    },
    "person2": {
        "name": "Alice",
        "age": 25,
        "skills": ["Java", "C++", "Python"]
    }
}
print(f"Nested dictionary: {nested_dict}")

# Accessing nested values
print(f"Person1 name: {nested_dict['person1']['name']}")
print(f"Person2 skills: {nested_dict['person2']['skills']}")

# 4. DICTIONARY COMPREHENSIONS
print("\n4. DICTIONARY COMPREHENSIONS")
print("-" * 30)

# Creating dictionary from range
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares}")

# Creating dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age_dict = {name: age for name, age in zip(names, ages)}
print(f"Name-age dictionary: {name_age_dict}")

# Conditional dictionary comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# 5. DICTIONARY METHODS FOR CREATION
print("\n5. DICTIONARY METHODS FOR CREATION")
print("-" * 30)

# fromkeys() - creates dictionary with default values
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"fromkeys() with default 0: {default_dict}")

# fromkeys() with different default values
default_dict2 = dict.fromkeys(keys, [])
print(f"fromkeys() with empty list: {default_dict2}")

# 6. MERGING DICTIONARIES
print("\n6. MERGING DICTIONARIES")
print("-" * 30)

# Method 1: Using update()
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(f"Merged using update(): {dict1}")

# Method 2: Using | operator (Python 3.9+)
dict3 = {"e": 5, "f": 6}
dict4 = {"g": 7, "h": 8}
merged_dict = dict3 | dict4
print(f"Merged using | operator: {merged_dict}")

# Method 3: Using ** unpacking
dict5 = {"i": 9, "j": 10}
dict6 = {"k": 11, "l": 12}
unpacked_dict = {**dict5, **dict6}
print(f"Merged using ** unpacking: {unpacked_dict}")

# 7. DICTIONARY OPERATIONS
print("\n7. DICTIONARY OPERATIONS")
print("-" * 30)

# Creating and accessing
student = {
    "name": "Emma",
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print(f"Student dictionary: {student}")
print(f"Student name: {student['name']}")
print(f"Student grade: {student['grade']}")
print(f"Student subjects: {student['subjects']}")

# Adding new key-value pairs
student["age"] = 16
student["school"] = "High School"
print(f"After adding new keys: {student}")

# Modifying values
student["grade"] = "A+"
print(f"After modifying grade: {student}")

# Removing key-value pairs
del student["school"]
print(f"After removing 'school': {student}")

# 8. DICTIONARY METHODS
print("\n8. DICTIONARY METHODS")
print("-" * 30)

# keys(), values(), items()
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# get() method (safe access)
print(f"Age using get(): {student.get('age')}")
print(f"Non-existent key using get(): {student.get('height', 'Not found')}")

# pop() method
removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")
print(f"Dictionary after pop: {student}")

# 9. PRACTICAL EXAMPLES
print("\n9. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Configuration settings
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp",
        "user": "admin"
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": True
    }
}
print(f"Configuration: {config}")

# Example 2: Word frequency counter
text = "hello world hello python world"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"Word frequency: {word_count}")

# Example 3: Student grades
grades = {
    "Alice": {"Math": 95, "Science": 88, "English": 92},
    "Bob": {"Math": 78, "Science": 85, "English": 90},
    "Charlie": {"Math": 92, "Science": 90, "English": 85}
}

print(f"Student grades: {grades}")

# 10. COMMON PATTERNS
print("\n10. COMMON PATTERNS")
print("-" * 30)

# Pattern 1: Default dictionary
def count_letters(text):
    letter_count = {}
    for letter in text.lower():
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

result = count_letters("Hello World")
print(f"Letter count: {result}")

# Pattern 2: Dictionary as switch/case
def get_day_name(day_number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day_number, "Invalid day")

print(f"Day 3: {get_day_name(3)}")
print(f"Day 9: {get_day_name(9)}")

# Pattern 3: Dictionary for data transformation
roman_numerals = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

def roman_to_int(roman):
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

print(f"Roman 'XIV' to integer: {roman_to_int('XIV')}")

# 11. SUMMARY
print("\n11. SUMMARY")
print("-" * 30)

print("Dictionary Creation Methods:")
print("1. Curly braces: {'key': 'value'}")
print("2. dict() constructor: dict(key='value')")
print("3. dict() with tuples: dict([('key', 'value')])")
print("4. Dictionary comprehensions: {x: x**2 for x in range(5)}")
print("5. fromkeys(): dict.fromkeys(keys, default_value)")

print("\nKey Features:")
print("- Mutable: Can be modified after creation")
print("- Unordered: Keys don't maintain insertion order (before Python 3.7)")
print("- Key uniqueness: Each key must be unique")
print("- Hashable keys: Keys must be immutable")
print("- Flexible values: Values can be any type")

print("\nCommon Use Cases:")
print("- Configuration settings")
print("- Data lookup tables")
print("- Caching and memoization")
print("- JSON-like data structures")
print("- Function parameter storage") 