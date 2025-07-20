"""
17. What is the difference between 'is' and '==' in Python?

'is' checks for identity (same object in memory), while '==' checks for equality (same values).
'is' compares object IDs, while '==' compares object values.
"""

print("=== 'IS' vs '==' IN PYTHON ===\n")

# 1. BASIC DIFFERENCE
print("1. BASIC DIFFERENCE")
print("-" * 30)

# Identity vs Equality
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Identity check (same object)
print(f"a is c: {a is c}")  # True - same object
print(f"a is b: {a is b}")  # False - different objects

# Equality check (same values)
print(f"a == b: {a == b}")  # True - same values
print(f"a == c: {a == c}")  # True - same values

# 2. OBJECT IDENTITY
print("\n2. OBJECT IDENTITY")
print("-" * 30)

import id

# Checking object IDs
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

# Objects with same ID are the same object
print(f"a is c: {a is c}")  # True
print(f"id(a) == id(c): {id(a) == id(c)}")  # True

# Objects with different IDs are different objects
print(f"a is b: {a is b}")  # False
print(f"id(a) == id(b): {id(a) == id(b)}")  # False

# 3. IMMUTABLE OBJECTS
print("\n3. IMMUTABLE OBJECTS")
print("-" * 30)

# Integers
x = 42
y = 42
print(f"x = {x}, y = {y}")
print(f"x is y: {x is y}")  # May be True due to integer caching
print(f"x == y: {x == y}")  # Always True

# Strings
str1 = "hello"
str2 = "hello"
print(f"str1 = '{str1}', str2 = '{str2}'")
print(f"str1 is str2: {str1 is str2}")  # May be True due to string interning
print(f"str1 == str2: {str1 == str2}")  # Always True

# Tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(f"tuple1 = {tuple1}, tuple2 = {tuple2}")
print(f"tuple1 is tuple2: {tuple1 is tuple2}")  # False
print(f"tuple1 == tuple2: {tuple1 == tuple2}")  # True

# 4. MUTABLE OBJECTS
print("\n4. MUTABLE OBJECTS")
print("-" * 30)

# Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 = {list1}, list2 = {list2}")
print(f"list1 is list2: {list1 is list2}")  # False
print(f"list1 == list2: {list1 == list2}")  # True

# Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2}
print(f"dict1 = {dict1}, dict2 = {dict2}")
print(f"dict1 is dict2: {dict1 is dict2}")  # False
print(f"dict1 == dict2: {dict1 == dict2}")  # True

# Sets
set1 = {1, 2, 3}
set2 = {1, 2, 3}
print(f"set1 = {set1}, set2 = {set2}")
print(f"set1 is set2: {set1 is set2}")  # False
print(f"set1 == set2: {set1 == set2}")  # True

# 5. NONE COMPARISON
print("\n5. NONE COMPARISON")
print("-" * 30)

# Always use 'is' for None
x = None
y = None

print(f"x is None: {x is None}")  # True
print(f"x == None: {x == None}")  # True (but not recommended)

# Checking for None
def check_none(value):
    if value is None:
        return "Value is None"
    else:
        return "Value is not None"

print(f"check_none(None): {check_none(None)}")
print(f"check_none(42): {check_none(42)}")

# 6. BOOLEAN COMPARISON
print("\n6. BOOLEAN COMPARISON")
print("-" * 30)

# Boolean values
true_val = True
false_val = False

print(f"true_val is True: {true_val is True}")  # True
print(f"true_val == True: {true_val == True}")  # True

print(f"false_val is False: {false_val is False}")  # True
print(f"false_val == False: {false_val == False}")  # True

# 7. PRACTICAL EXAMPLES
print("\n7. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Function parameter checking
def process_data(data):
    if data is None:
        return "No data provided"
    elif data == []:
        return "Empty list provided"
    else:
        return f"Processing {len(data)} items"

print(f"process_data(None): {process_data(None)}")
print(f"process_data([]): {process_data([])}")
print(f"process_data([1, 2, 3]): {process_data([1, 2, 3])}")

# Example 2: Object comparison
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

person1 = Person("John", 30)
person2 = Person("John", 30)
person3 = person1

print(f"person1 == person2: {person1 == person2}")  # True (same values)
print(f"person1 is person2: {person1 is person2}")  # False (different objects)
print(f"person1 is person3: {person1 is person3}")  # True (same object)

# 8. STRING INTERNING
print("\n8. STRING INTERNING")
print("-" * 30)

# String interning (Python may reuse string objects)
str1 = "hello"
str2 = "hello"
str3 = "hello" + ""

print(f"str1 is str2: {str1 is str2}")  # May be True
print(f"str1 == str2: {str1 == str2}")  # Always True

# Different strings
str4 = "hello world"
str5 = "hello" + " world"
print(f"str4 is str5: {str4 is str5}")  # May be False
print(f"str4 == str5: {str4 == str5}")  # Always True

# 9. INTEGER CACHING
print("\n9. INTEGER CACHING")
print("-" * 30)

# Small integers are cached (typically -5 to 256)
a = 42
b = 42
c = 42

print(f"a is b: {a is b}")  # True (cached)
print(f"a == b: {a == b}")  # True

# Large integers are not cached
x = 1000
y = 1000
print(f"x is y: {x is y}")  # May be False
print(f"x == y: {x == y}")  # True

# 10. CUSTOM OBJECTS
print("\n10. CUSTOM OBJECTS")
print("-" * 30)

class CustomObject:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, CustomObject):
            return False
        return self.value == other.value

obj1 = CustomObject(42)
obj2 = CustomObject(42)
obj3 = obj1

print(f"obj1 == obj2: {obj1 == obj2}")  # True (same values)
print(f"obj1 is obj2: {obj1 is obj2}")  # False (different objects)
print(f"obj1 is obj3: {obj1 is obj3}")  # True (same object)

# 11. COMMON MISTAKES
print("\n11. COMMON MISTAKES")
print("-" * 30)

# Mistake 1: Using == for None
def bad_none_check(value):
    if value == None:  # Bad practice
        return "None"
    return "Not None"

def good_none_check(value):
    if value is None:  # Good practice
        return "None"
    return "Not None"

# Mistake 2: Using is for value comparison
def bad_value_check(a, b):
    if a is b:  # Bad for value comparison
        return "Same object"
    return "Different objects"

def good_value_check(a, b):
    if a == b:  # Good for value comparison
        return "Same values"
    return "Different values"

# 12. PERFORMANCE CONSIDERATIONS
print("\n12. PERFORMANCE CONSIDERATIONS")
print("-" * 30)

import time

# Performance comparison
def performance_test():
    # Test 'is' operator
    start = time.time()
    for _ in range(1000000):
        result = a is b
    is_time = time.time() - start
    
    # Test '==' operator
    start = time.time()
    for _ in range(1000000):
        result = a == b
    eq_time = time.time() - start
    
    return is_time, eq_time

is_time, eq_time = performance_test()
print(f"'is' operator time: {is_time:.6f} seconds")
print(f"'==' operator time: {eq_time:.6f} seconds")

# 13. BEST PRACTICES
print("\n13. BEST PRACTICES")
print("-" * 30)

# Good: Use 'is' for identity checks
def check_identity(obj1, obj2):
    return obj1 is obj2

# Good: Use '==' for value checks
def check_equality(obj1, obj2):
    return obj1 == obj2

# Good: Use 'is None' for None checks
def check_none_good(value):
    return value is None

# Good: Use 'is' for boolean checks
def check_boolean(value):
    return value is True or value is False

# 14. SUMMARY
print("\n14. SUMMARY")
print("-" * 30)

print("Key Differences:")
print("┌─────────────┬─────────────┬─────────────┐")
print("│ Operator    │ Checks      │ Use Case    │")
print("├─────────────┼─────────────┼─────────────┤")
print("│ is          │ Identity    │ Same object │")
print("│ ==          │ Equality    │ Same values │")
print("└─────────────┴─────────────┴─────────────┘")

print("\nWhen to Use 'is':")
print("- Comparing with None")
print("- Comparing with True/False")
print("- Checking if two variables reference the same object")
print("- Identity checks")

print("\nWhen to Use '==':")
print("- Comparing values")
print("- Checking if two objects have the same content")
print("- Value equality checks")
print("- Comparing custom objects")

print("\nBest Practices:")
print("- Use 'is' for None, True, False comparisons")
print("- Use '==' for value comparisons")
print("- Use 'is' for identity checks")
print("- Use '==' for equality checks")
print("- Be aware of string interning and integer caching")
print("- Don't rely on 'is' for value comparisons")

print("\nCommon Gotchas:")
print("- String interning can make 'is' True for different strings")
print("- Integer caching can make 'is' True for different integers")
print("- Mutable objects are never 'is' equal unless they're the same object")
print("- Custom objects need __eq__ method for proper '==' comparison") 