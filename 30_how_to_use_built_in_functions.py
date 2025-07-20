"""
30. How do you use built-in functions in Python?

Built-in functions in Python are functions that are available without importing
any module. They provide essential functionality for common operations like
type conversion, mathematical operations, sequence operations, and more.
"""

print("=== BUILT-IN FUNCTIONS IN PYTHON ===\n")

# 1. TYPE CONVERSION FUNCTIONS
print("1. TYPE CONVERSION FUNCTIONS")
print("-" * 30)

# int() - Convert to integer
print(f"int(3.14): {int(3.14)}")
print(f"int('42'): {int('42')}")
print(f"int(True): {int(True)}")

# float() - Convert to float
print(f"float(42): {float(42)}")
print(f"float('3.14'): {float('3.14')}")

# str() - Convert to string
print(f"str(123): '{str(123)}'")
print(f"str([1, 2, 3]): '{str([1, 2, 3])}'")

# bool() - Convert to boolean
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hello'): {bool('hello')}")

# list(), tuple(), set(), dict() - Convert to collections
print(f"list('hello'): {list('hello')}")
print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}")
print(f"set([1, 2, 2, 3]): {set([1, 2, 2, 3])}")

# 2. MATHEMATICAL FUNCTIONS
print("\n2. MATHEMATICAL FUNCTIONS")
print("-" * 30)

# abs() - Absolute value
print(f"abs(-5): {abs(-5)}")
print(f"abs(-3.14): {abs(-3.14)}")

# round() - Round to nearest integer
print(f"round(3.14): {round(3.14)}")
print(f"round(3.14, 1): {round(3.14, 1)}")

# pow() - Power function
print(f"pow(2, 3): {pow(2, 3)}")
print(f"pow(2, 3, 5): {pow(2, 3, 5)}")  # With modulus

# divmod() - Division and modulus
quotient, remainder = divmod(17, 5)
print(f"divmod(17, 5): quotient={quotient}, remainder={remainder}")

# 3. SEQUENCE FUNCTIONS
print("\n3. SEQUENCE FUNCTIONS")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]

# len() - Length of sequence
print(f"len(numbers): {len(numbers)}")
print(f"len('hello'): {len('hello')}")

# max() - Maximum value
print(f"max(numbers): {max(numbers)}")
print(f"max('hello'): {max('hello')}")

# min() - Minimum value
print(f"min(numbers): {min(numbers)}")
print(f"min('hello'): {min('hello')}")

# sum() - Sum of numbers
print(f"sum(numbers): {sum(numbers)}")

# sorted() - Sort sequence
print(f"sorted([3, 1, 4, 1, 5]): {sorted([3, 1, 4, 1, 5])}")
print(f"sorted('hello'): {sorted('hello')}")

# reversed() - Reverse sequence
print(f"list(reversed(numbers)): {list(reversed(numbers))}")

# 4. ITERATION FUNCTIONS
print("\n4. ITERATION FUNCTIONS")
print("-" * 30)

# range() - Generate sequence of numbers
print(f"list(range(5)): {list(range(5))}")
print(f"list(range(1, 6)): {list(range(1, 6))}")
print(f"list(range(0, 10, 2)): {list(range(0, 10, 2))}")

# enumerate() - Add index to iterable
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"enumerate: {index}: {fruit}")

# zip() - Combine iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"zip: {name} is {age} years old")

# 5. OBJECT FUNCTIONS
print("\n5. OBJECT FUNCTIONS")
print("-" * 30)

# type() - Get type of object
print(f"type(42): {type(42)}")
print(f"type('hello'): {type('hello')}")
print(f"type([1, 2, 3]): {type([1, 2, 3])}")

# isinstance() - Check if object is instance of type
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance('hello', str): {isinstance('hello', str)}")
print(f"isinstance([1, 2], list): {isinstance([1, 2], list)}")

# id() - Get object identity
x = [1, 2, 3]
y = [1, 2, 3]
print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")
print(f"x is y: {x is y}")

# 6. INPUT/OUTPUT FUNCTIONS
print("\n6. INPUT/OUTPUT FUNCTIONS")
print("-" * 30)

# print() - Print to console
print("print(): Hello, World!")
print("print():", "Multiple", "arguments", sep=" | ")

# input() - Get user input (commented to avoid blocking)
# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")

# 7. EVALUATION FUNCTIONS
print("\n7. EVALUATION FUNCTIONS")
print("-" * 30)

# eval() - Evaluate expression (use with caution)
expression = "2 + 3 * 4"
result = eval(expression)
print(f"eval('{expression}'): {result}")

# exec() - Execute code (use with caution)
code = "x = 10; y = 20; print(f'x + y = {x + y}')"
print("exec():", end=" ")
exec(code)

# 8. ATTRIBUTE FUNCTIONS
print("\n8. ATTRIBUTE FUNCTIONS")
print("-" * 30)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)

# getattr() - Get attribute value
name = getattr(person, 'name')
print(f"getattr(person, 'name'): {name}")

# setattr() - Set attribute value
setattr(person, 'age', 26)
print(f"After setattr: person.age = {person.age}")

# hasattr() - Check if attribute exists
print(f"hasattr(person, 'name'): {hasattr(person, 'name')}")
print(f"hasattr(person, 'height'): {hasattr(person, 'height')}")

# 9. MAP AND FILTER FUNCTIONS
print("\n9. MAP AND FILTER FUNCTIONS")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]

# map() - Apply function to all items
squared = list(map(lambda x: x ** 2, numbers))
print(f"map(lambda x: x ** 2, numbers): {squared}")

# filter() - Filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(lambda x: x % 2 == 0, numbers): {evens}")

# 10. REDUCE FUNCTION
print("\n10. REDUCE FUNCTION")
print("-" * 30)

from functools import reduce

# reduce() - Reduce sequence to single value
product = reduce(lambda x, y: x * y, numbers)
print(f"reduce(lambda x, y: x * y, numbers): {product}")

sum_result = reduce(lambda x, y: x + y, numbers)
print(f"reduce(lambda x, y: x + y, numbers): {sum_result}")

# 11. ANY AND ALL FUNCTIONS
print("\n11. ANY AND ALL FUNCTIONS")
print("-" * 30)

# any() - Check if any item is True
conditions = [False, True, False, True]
print(f"any(conditions): {any(conditions)}")

# all() - Check if all items are True
all_true = [True, True, True]
print(f"all(all_true): {all(all_true)}")

some_false = [True, False, True]
print(f"all(some_false): {all(some_false)}")

# 12. OPEN FUNCTION
print("\n12. OPEN FUNCTION")
print("-" * 30)

# open() - Open file (demonstration without actual file)
print("open() function is used to open files:")
print("- open('filename.txt', 'r') for reading")
print("- open('filename.txt', 'w') for writing")
print("- open('filename.txt', 'a') for appending")

# Example file operations (commented to avoid file creation)
# with open('test.txt', 'w') as f:
#     f.write('Hello, World!')
# 
# with open('test.txt', 'r') as f:
#     content = f.read()
#     print(f"File content: {content}")

# 13. DIR AND HELP FUNCTIONS
print("\n13. DIR AND HELP FUNCTIONS")
print("-" * 30)

# dir() - Get object attributes
print(f"dir([]): {dir([])[:5]}...")  # Show first 5 attributes

# help() - Get help on object
# help(str)  # This would show help for string class

# 14. COMPLEX BUILT-IN FUNCTIONS
print("\n14. COMPLEX BUILT-IN FUNCTIONS")
print("-" * 30)

# format() - Format value
formatted = format(3.14159, '.2f')
print(f"format(3.14159, '.2f'): {formatted}")

# repr() - String representation
print(f"repr('hello'): {repr('hello')}")
print(f"repr([1, 2, 3]): {repr([1, 2, 3])}")

# ascii() - ASCII representation
print(f"ascii('hello'): {ascii('hello')}")
print(f"ascii('café'): {ascii('café')}")

# 15. PRACTICAL EXAMPLES
print("\n15. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Data processing
data = ['1', '2', '3', '4', '5']
numbers = list(map(int, data))
print(f"Converted strings to integers: {numbers}")

# Example 2: Filtering data
ages = [18, 25, 30, 15, 35, 40]
adults = list(filter(lambda age: age >= 18, ages))
print(f"Adults (age >= 18): {adults}")

# Example 3: Finding maximum with custom key
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
best_student = max(students, key=lambda s: s['score'])
print(f"Best student: {best_student}")

# Example 4: Grouping data
from itertools import groupby

data = [1, 1, 2, 2, 2, 3, 3, 4]
grouped = {k: list(v) for k, v in groupby(data)}
print(f"Grouped data: {grouped}")

# 16. BUILT-IN FUNCTIONS BEST PRACTICES
print("\n16. BUILT-IN FUNCTIONS BEST PRACTICES")
print("-" * 30)

print("Built-in Functions Best Practices:")
print("1. Use built-in functions when available")
print("2. Understand function signatures and return types")
print("3. Use appropriate functions for the task")
print("4. Be careful with eval() and exec()")
print("5. Use map/filter/reduce for functional programming")
print("6. Leverage any() and all() for boolean operations")
print("7. Use enumerate() for indexed iteration")

# Good practice: Use built-in functions
def good_practice_example(data):
    """Good practice: Use built-in functions."""
    if not data:
        return []
    return list(map(str, filter(lambda x: x > 0, data)))

# Bad practice: Manual implementation
def bad_practice_example(data):
    """Bad practice: Manual implementation."""
    result = []
    for item in data:
        if item > 0:
            result.append(str(item))
    return result

# 17. SUMMARY
print("\n17. SUMMARY")
print("-" * 30)

print("What are Built-in Functions?")
print("- Functions available without importing")
print("- Provide essential functionality")
print("- Optimized for performance")
print("- Part of Python's standard library")

print("\nCommon Built-in Function Categories:")
print("- Type conversion: int(), float(), str(), bool(), list(), etc.")
print("- Mathematical: abs(), round(), pow(), divmod()")
print("- Sequence: len(), max(), min(), sum(), sorted(), reversed()")
print("- Iteration: range(), enumerate(), zip()")
print("- Object: type(), isinstance(), id()")
print("- I/O: print(), input(), open()")
print("- Evaluation: eval(), exec()")
print("- Attributes: getattr(), setattr(), hasattr()")
print("- Functional: map(), filter(), reduce()")
print("- Boolean: any(), all()")

print("\nBest Practices:")
print("- Use built-in functions when available")
print("- Understand function signatures")
print("- Use appropriate functions for the task")
print("- Be careful with eval() and exec()")
print("- Leverage functional programming functions")
print("- Use any() and all() for boolean operations")
print("- Use enumerate() for indexed iteration")

print("\nCommon Use Cases:")
print("- Data type conversion")
print("- Mathematical calculations")
print("- Sequence operations")
print("- Object inspection")
print("- File operations")
print("- Functional programming")
print("- Data processing")
print("- Input/output handling") 