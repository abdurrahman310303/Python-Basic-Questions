"""
3. What are Python's data types?

Python has several built-in data types that can be categorized into:
1. Numeric Types
2. Sequence Types
3. Mapping Types
4. Set Types
5. Boolean Type
6. None Type
"""

print("=== PYTHON DATA TYPES ===\n")

# 1. NUMERIC TYPES
print("1. NUMERIC TYPES")
print("-" * 20)

# Integer (int)
age = 25
year = 2024
print(f"Integer examples: age = {age} (type: {type(age)})")
print(f"Integer examples: year = {year} (type: {type(year)})")

# Float
height = 5.9
pi = 3.14159
print(f"Float examples: height = {height} (type: {type(height)})")
print(f"Float examples: pi = {pi} (type: {type(pi)})")

# Complex
complex_num = 3 + 4j
print(f"Complex example: {complex_num} (type: {type(complex_num)})")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")

# 2. SEQUENCE TYPES
print("\n2. SEQUENCE TYPES")
print("-" * 20)

# String (str)
name = "John Doe"
message = 'Hello, World!'
multi_line = """This is a
multi-line string"""
print(f"String examples:")
print(f"  name = '{name}' (type: {type(name)})")
print(f"  message = '{message}' (type: {type(message)})")
print(f"  multi_line = '{multi_line}'")

# String operations
print(f"\nString operations:")
print(f"  Length of name: {len(name)}")
print(f"  Uppercase: {name.upper()}")
print(f"  Lowercase: {name.lower()}")
print(f"  Split: {name.split()}")
print(f"  Replace: {name.replace('John', 'Jane')}")

# List
fruits = ["apple", "banana", "orange"]
mixed_list = [1, "hello", 3.14, True]
print(f"\nList examples:")
print(f"  fruits = {fruits} (type: {type(fruits)})")
print(f"  mixed_list = {mixed_list} (type: {type(mixed_list)})")

# List operations
fruits.append("grape")
fruits.insert(1, "mango")
print(f"  After append and insert: {fruits}")
print(f"  First fruit: {fruits[0]}")
print(f"  Last fruit: {fruits[-1]}")
print(f"  Slicing [1:3]: {fruits[1:3]}")

# Tuple
coordinates = (10, 20)
rgb_color = (255, 128, 0)
print(f"\nTuple examples:")
print(f"  coordinates = {coordinates} (type: {type(coordinates)})")
print(f"  rgb_color = {rgb_color} (type: {type(rgb_color)})")

# Tuple operations
print(f"  First coordinate: {coordinates[0]}")
print(f"  Tuple length: {len(coordinates)}")
# Note: Tuples are immutable - cannot be modified after creation

# 3. MAPPING TYPE
print("\n3. MAPPING TYPE")
print("-" * 20)

# Dictionary (dict)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}
print(f"Dictionary example:")
print(f"  person = {person} (type: {type(person)})")

# Dictionary operations
print(f"\nDictionary operations:")
print(f"  Name: {person['name']}")
print(f"  Age: {person['age']}")
print(f"  Keys: {list(person.keys())}")
print(f"  Values: {list(person.values())}")
print(f"  Items: {list(person.items())}")

# Adding/updating dictionary
person["email"] = "alice@example.com"
person["age"] = 31
print(f"  After updates: {person}")

# 4. SET TYPES
print("\n4. SET TYPES")
print("-" * 20)

# Set
unique_numbers = {1, 2, 3, 4, 5, 5, 4}  # Duplicates are automatically removed
fruits_set = {"apple", "banana", "apple", "orange"}
print(f"Set examples:")
print(f"  unique_numbers = {unique_numbers} (type: {type(unique_numbers)})")
print(f"  fruits_set = {fruits_set} (type: {type(fruits_set)})")

# Set operations
fruits_set.add("grape")
fruits_set.remove("apple")
print(f"  After add and remove: {fruits_set}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet operations:")
print(f"  set1 = {set1}")
print(f"  set2 = {set2}")
print(f"  Union: {set1 | set2}")
print(f"  Intersection: {set1 & set2}")
print(f"  Difference: {set1 - set2}")

# 5. BOOLEAN TYPE
print("\n5. BOOLEAN TYPE")
print("-" * 20)

# Boolean
is_active = True
is_admin = False
print(f"Boolean examples:")
print(f"  is_active = {is_active} (type: {type(is_active)})")
print(f"  is_admin = {is_admin} (type: {type(is_admin)})")

# Boolean operations
print(f"\nBoolean operations:")
print(f"  True and True: {True and True}")
print(f"  True or False: {True or False}")
print(f"  not True: {not True}")

# Truthy and Falsy values
print(f"\nTruthy and Falsy values:")
print(f"  bool(0): {bool(0)}")
print(f"  bool(1): {bool(1)}")
print(f"  bool(''): {bool('')}")
print(f"  bool('hello'): {bool('hello')}")
print(f"  bool([]): {bool([])}")
print(f"  bool([1, 2]): {bool([1, 2])}")

# 6. NONE TYPE
print("\n6. NONE TYPE")
print("-" * 20)

# None
empty_value = None
print(f"None example:")
print(f"  empty_value = {empty_value} (type: {type(empty_value)})")

# Common use of None
def find_user(user_id):
    # Simulate database lookup
    if user_id == 1:
        return {"id": 1, "name": "John"}
    else:
        return None

result = find_user(1)
print(f"  User found: {result}")
result = find_user(999)
print(f"  User not found: {result}")

# 7. TYPE CHECKING AND CONVERSION
print("\n7. TYPE CHECKING AND CONVERSION")
print("-" * 20)

# Type checking
x = 42
y = "42"
z = 3.14

print(f"Type checking:")
print(f"  x = {x}, type: {type(x)}")
print(f"  y = {y}, type: {type(y)}")
print(f"  z = {z}, type: {type(z)}")

# Type conversion
print(f"\nType conversion:")
print(f"  int('42'): {int('42')}")
print(f"  str(42): {str(42)}")
print(f"  float(42): {float(42)}")
print(f"  list('hello'): {list('hello')}")
print(f"  tuple([1, 2, 3]): {tuple([1, 2, 3])}")
print(f"  set([1, 2, 2, 3]): {set([1, 2, 2, 3])}")

# 8. MUTABLE VS IMMUTABLE TYPES
print("\n8. MUTABLE VS IMMUTABLE TYPES")
print("-" * 20)

print("Mutable types (can be changed):")
print("- Lists")
print("- Dictionaries")
print("- Sets")

print("\nImmutable types (cannot be changed):")
print("- Numbers (int, float, complex)")
print("- Strings")
print("- Tuples")
print("- Frozen sets")

# Example of mutability
print(f"\nMutability example:")
numbers = [1, 2, 3]
print(f"  Original list: {numbers}")
numbers.append(4)
print(f"  After append: {numbers}")

name = "John"
print(f"  Original string: {name}")
# name[0] = "J"  # This would cause an error - strings are immutable
new_name = name.replace("J", "J")
print(f"  String methods return new strings: {new_name}")

print("\n=== SUMMARY ===")
print("Python's data types provide:")
print("- Flexibility for different use cases")
print("- Built-in methods for common operations")
print("- Automatic memory management")
print("- Type safety and conversion capabilities") 