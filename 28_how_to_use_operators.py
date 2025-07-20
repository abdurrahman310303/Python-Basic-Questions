"""
28. How do you use operators in Python?

Operators in Python are special symbols that perform operations on operands.
Python has various types of operators: arithmetic, comparison, logical,
assignment, bitwise, membership, and identity operators.
"""

print("=== OPERATORS IN PYTHON ===\n")

# 1. ARITHMETIC OPERATORS
print("1. ARITHMETIC OPERATORS")
print("-" * 30)

a, b = 10, 3

# Addition
print(f"Addition: {a} + {b} = {a + b}")

# Subtraction
print(f"Subtraction: {a} - {b} = {a - b}")

# Multiplication
print(f"Multiplication: {a} * {b} = {a * b}")

# Division (float result)
print(f"Division: {a} / {b} = {a / b}")

# Floor Division (integer result)
print(f"Floor Division: {a} // {b} = {a // b}")

# Modulus (remainder)
print(f"Modulus: {a} % {b} = {a % b}")

# Exponentiation
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# 2. COMPARISON OPERATORS
print("\n2. COMPARISON OPERATORS")
print("-" * 30)

x, y = 5, 10

# Equal to
print(f"Equal to: {x} == {y} = {x == y}")

# Not equal to
print(f"Not equal to: {x} != {y} = {x != y}")

# Greater than
print(f"Greater than: {x} > {y} = {x > y}")

# Less than
print(f"Less than: {x} < {y} = {x < y}")

# Greater than or equal to
print(f"Greater than or equal to: {x} >= {y} = {x >= y}")

# Less than or equal to
print(f"Less than or equal to: {x} <= {y} = {x <= y}")

# 3. LOGICAL OPERATORS
print("\n3. LOGICAL OPERATORS")
print("-" * 30)

p, q = True, False

# AND operator
print(f"AND: {p} and {q} = {p and q}")

# OR operator
print(f"OR: {p} or {q} = {p or q}")

# NOT operator
print(f"NOT: not {p} = {not p}")

# Complex logical expressions
print(f"Complex: ({p} and {q}) or (not {p}) = {(p and q) or (not p)}")

# 4. ASSIGNMENT OPERATORS
print("\n4. ASSIGNMENT OPERATORS")
print("-" * 30)

# Basic assignment
num = 10
print(f"Basic assignment: num = {num}")

# Addition assignment
num += 5
print(f"Addition assignment: num += 5, num = {num}")

# Subtraction assignment
num -= 3
print(f"Subtraction assignment: num -= 3, num = {num}")

# Multiplication assignment
num *= 2
print(f"Multiplication assignment: num *= 2, num = {num}")

# Division assignment
num /= 4
print(f"Division assignment: num /= 4, num = {num}")

# Modulus assignment
num %= 2
print(f"Modulus assignment: num %= 2, num = {num}")

# Exponentiation assignment
num = 3
num **= 2
print(f"Exponentiation assignment: num **= 2, num = {num}")

# Floor division assignment
num //= 2
print(f"Floor division assignment: num //= 2, num = {num}")

# 5. BITWISE OPERATORS
print("\n5. BITWISE OPERATORS")
print("-" * 30)

a, b = 5, 3  # Binary: 101, 011

# Bitwise AND
print(f"Bitwise AND: {a} & {b} = {a & b}")

# Bitwise OR
print(f"Bitwise OR: {a} | {b} = {a | b}")

# Bitwise XOR
print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")

# Bitwise NOT
print(f"Bitwise NOT: ~{a} = {~a}")

# Left shift
print(f"Left shift: {a} << 1 = {a << 1}")

# Right shift
print(f"Right shift: {a} >> 1 = {a >> 1}")

# 6. MEMBERSHIP OPERATORS
print("\n6. MEMBERSHIP OPERATORS")
print("-" * 30)

# IN operator
fruits = ["apple", "banana", "orange"]
print(f"IN: 'apple' in {fruits} = {'apple' in fruits}")
print(f"IN: 'grape' in {fruits} = {'grape' in fruits}")

# NOT IN operator
print(f"NOT IN: 'grape' not in {fruits} = {'grape' not in fruits}")

# String membership
text = "Hello, World!"
print(f"String IN: 'Hello' in '{text}' = {'Hello' in text}")

# 7. IDENTITY OPERATORS
print("\n7. IDENTITY OPERATORS")
print("-" * 30)

# IS operator
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"IS: x is z = {x is z}")
print(f"IS: x is y = {x is y}")

# IS NOT operator
print(f"IS NOT: x is not y = {x is not y}")

# Comparison vs Identity
print(f"Equality: x == y = {x == y}")
print(f"Identity: x is y = {x is y}")

# 8. OPERATOR PRECEDENCE
print("\n8. OPERATOR PRECEDENCE")
print("-" * 30)

# Example with multiple operators
result = 2 + 3 * 4 ** 2
print(f"2 + 3 * 4 ** 2 = {result}")

# Using parentheses to control precedence
result_with_parens = (2 + 3) * 4 ** 2
print(f"(2 + 3) * 4 ** 2 = {result_with_parens}")

# Complex expression
complex_expr = 10 + 5 * 2 - 3 / 2
print(f"10 + 5 * 2 - 3 / 2 = {complex_expr}")

# 9. COMPARISON WITH DIFFERENT TYPES
print("\n9. COMPARISON WITH DIFFERENT TYPES")
print("-" * 30)

# Numeric comparisons
print(f"5 > 3.14 = {5 > 3.14}")
print(f"10 == 10.0 = {10 == 10.0}")

# String comparisons
print(f"'apple' < 'banana' = {'apple' < 'banana'}")
print(f"'Hello' == 'hello' = {'Hello' == 'hello'}")

# Mixed type comparisons
try:
    result = 5 < "hello"
    print(f"5 < 'hello' = {result}")
except TypeError as e:
    print(f"Error comparing int and str: {e}")

# 10. LOGICAL OPERATOR SHORT-CIRCUITING
print("\n10. LOGICAL OPERATOR SHORT-CIRCUITING")
print("-" * 30)

# Short-circuiting with AND
def expensive_function():
    print("Expensive function called")
    return False

# This won't call expensive_function due to short-circuiting
result = False and expensive_function()
print(f"False and expensive_function() = {result}")

# This will call expensive_function
result = True and expensive_function()
print(f"True and expensive_function() = {result}")

# Short-circuiting with OR
def another_expensive_function():
    print("Another expensive function called")
    return True

# This will call the function due to short-circuiting
result = True or another_expensive_function()
print(f"True or another_expensive_function() = {result}")

# 11. BITWISE OPERATIONS ON INTEGERS
print("\n11. BITWISE OPERATIONS ON INTEGERS")
print("-" * 30)

# Binary representation
num = 42
print(f"Number: {num}")
print(f"Binary: {bin(num)}")

# Bitwise operations
print(f"Left shift by 1: {num << 1} ({bin(num << 1)})")
print(f"Right shift by 1: {num >> 1} ({bin(num >> 1)})")
print(f"Bitwise AND with 15: {num & 15} ({bin(num & 15)})")

# Setting and clearing bits
# Set bit at position 2
num_set = num | (1 << 2)
print(f"Set bit at position 2: {num_set} ({bin(num_set)})")

# Clear bit at position 1
num_clear = num & ~(1 << 1)
print(f"Clear bit at position 1: {num_clear} ({bin(num_clear)})")

# 12. OPERATOR OVERLOADING
print("\n12. OPERATOR OVERLOADING")
print("-" * 30)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Using overloaded operators
p1 = Point(1, 2)
p2 = Point(3, 4)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Addition: {p1 + p2}")
print(f"Subtraction: {p1 - p2}")
print(f"Equality: {p1 == p2}")

# 13. OPERATOR FUNCTIONS
print("\n13. OPERATOR FUNCTIONS")
print("-" * 30)

import operator

# Using operator functions
a, b = 10, 3

print(f"operator.add({a}, {b}) = {operator.add(a, b)}")
print(f"operator.sub({a}, {b}) = {operator.sub(a, b)}")
print(f"operator.mul({a}, {b}) = {operator.mul(a, b)}")
print(f"operator.truediv({a}, {b}) = {operator.truediv(a, b)}")
print(f"operator.floordiv({a}, {b}) = {operator.floordiv(a, b)}")
print(f"operator.mod({a}, {b}) = {operator.mod(a, b)}")
print(f"operator.pow({a}, {b}) = {operator.pow(a, b)}")

# Logical operators
print(f"operator.and_({True}, {False}) = {operator.and_(True, False)}")
print(f"operator.or_({True}, {False}) = {operator.or_(True, False)}")
print(f"operator.not_({True}) = {operator.not_(True)}")

# 14. OPERATOR BEST PRACTICES
print("\n14. OPERATOR BEST PRACTICES")
print("-" * 30)

print("Operator Best Practices:")
print("1. Use parentheses to clarify precedence")
print("2. Be aware of short-circuiting behavior")
print("3. Use appropriate operators for the task")
print("4. Consider readability over cleverness")
print("5. Test edge cases with operators")
print("6. Use operator functions for complex operations")

# Good practice: Clear precedence
good_example = (2 + 3) * 4
print(f"Good: (2 + 3) * 4 = {good_example}")

# Bad practice: Unclear precedence
bad_example = 2 + 3 * 4
print(f"Bad: 2 + 3 * 4 = {bad_example}")

# Good practice: Using operator functions
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(operator.mul, numbers)
print(f"Product using operator.mul: {product}")

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What are Operators?")
print("- Special symbols that perform operations")
print("- Work on operands (values)")
print("- Have precedence and associativity")
print("- Can be overloaded for custom types")

print("\nOperator Types:")
print("- Arithmetic: +, -, *, /, //, %, **")
print("- Comparison: ==, !=, >, <, >=, <=")
print("- Logical: and, or, not")
print("- Assignment: =, +=, -=, *=, /=, etc.")
print("- Bitwise: &, |, ^, ~, <<, >>")
print("- Membership: in, not in")
print("- Identity: is, is not")

print("\nOperator Precedence (highest to lowest):")
print("- ** (exponentiation)")
print("- +x, -x, ~x (unary)")
print("- *, /, //, %")
print("- +, -")
print("- <<, >> (bitwise shifts)")
print("- & (bitwise AND)")
print("- ^ (bitwise XOR)")
print("- | (bitwise OR)")
print("- ==, !=, >, <, >=, <=")
print("- is, is not")
print("- in, not in")
print("- not")
print("- and")
print("- or")

print("\nBest Practices:")
print("- Use parentheses for clarity")
print("- Understand short-circuiting")
print("- Use appropriate operators")
print("- Consider readability")
print("- Test edge cases")
print("- Use operator functions when needed")

print("\nCommon Use Cases:")
print("- Mathematical calculations")
print("- Boolean logic")
print("- Bit manipulation")
print("- Data structure operations")
print("- Custom type operations")
print("- Performance optimization") 