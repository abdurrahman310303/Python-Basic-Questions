"""
9. What are Python's arithmetic operators?

Python provides several arithmetic operators for performing mathematical operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Floor Division (//)
6. Modulo (%)
7. Exponentiation (**)
"""

print("=== PYTHON ARITHMETIC OPERATORS ===\n")

# 1. ADDITION OPERATOR (+)
print("1. ADDITION OPERATOR (+)")
print("-" * 30)

# Basic addition
a = 10
b = 5
result = a + b
print(f"{a} + {b} = {result}")

# Addition with different data types
integer_sum = 15 + 25
float_sum = 3.14 + 2.86
print(f"Integer addition: 15 + 25 = {integer_sum}")
print(f"Float addition: 3.14 + 2.86 = {float_sum}")

# String concatenation (also uses +)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"String concatenation: {first_name} + {last_name} = {full_name}")

# List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(f"List concatenation: {list1} + {list2} = {combined_list}")

# 2. SUBTRACTION OPERATOR (-)
print("\n2. SUBTRACTION OPERATOR (-)")
print("-" * 30)

# Basic subtraction
x = 20
y = 8
difference = x - y
print(f"{x} - {y} = {difference}")

# Negative numbers
negative_result = 5 - 10
print(f"5 - 10 = {negative_result}")

# Float subtraction
float_diff = 10.5 - 3.2
print(f"10.5 - 3.2 = {float_diff}")

# 3. MULTIPLICATION OPERATOR (*)
print("\n3. MULTIPLICATION OPERATOR (*)")
print("-" * 30)

# Basic multiplication
num1 = 6
num2 = 7
product = num1 * num2
print(f"{num1} * {num2} = {product}")

# Float multiplication
float_product = 2.5 * 3.0
print(f"2.5 * 3.0 = {float_product}")

# String repetition
repeated_string = "Hello " * 3
print(f"'Hello ' * 3 = '{repeated_string}'")

# List repetition
repeated_list = [1, 2] * 4
print(f"[1, 2] * 4 = {repeated_list}")

# 4. DIVISION OPERATOR (/)
print("\n4. DIVISION OPERATOR (/)")
print("-" * 30)

# Basic division
dividend = 15
divisor = 3
quotient = dividend / divisor
print(f"{dividend} / {divisor} = {quotient}")

# Division with remainder
result1 = 17 / 5
print(f"17 / 5 = {result1}")

# Float division
float_division = 10.0 / 3.0
print(f"10.0 / 3.0 = {float_division}")

# Division by zero (will cause error)
# result2 = 10 / 0  # ZeroDivisionError

# 5. FLOOR DIVISION OPERATOR (//)
print("\n5. FLOOR DIVISION OPERATOR (//)")
print("-" * 30)

# Floor division (returns integer result)
floor_result1 = 17 // 5
print(f"17 // 5 = {floor_result1}")

floor_result2 = 10 // 3
print(f"10 // 3 = {floor_result2}")

# Float floor division
float_floor = 10.5 // 3.0
print(f"10.5 // 3.0 = {float_floor}")

# Comparison with regular division
regular_div = 17 / 5
floor_div = 17 // 5
print(f"Regular division: 17 / 5 = {regular_div}")
print(f"Floor division: 17 // 5 = {floor_div}")

# 6. MODULO OPERATOR (%)
print("\n6. MODULO OPERATOR (%)")
print("-" * 30)

# Basic modulo (remainder)
modulo_result1 = 17 % 5
print(f"17 % 5 = {modulo_result1}")

modulo_result2 = 10 % 3
print(f"10 % 3 = {modulo_result2}")

# Checking if number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Float modulo
float_modulo = 10.5 % 3.0
print(f"10.5 % 3.0 = {float_modulo}")

# 7. EXPONENTIATION OPERATOR (**)
print("\n7. EXPONENTIATION OPERATOR (**)")
print("-" * 30)

# Basic exponentiation
base = 2
exponent = 3
power = base ** exponent
print(f"{base} ** {exponent} = {power}")

# Square and cube
square = 5 ** 2
cube = 3 ** 3
print(f"5 ** 2 = {square}")
print(f"3 ** 3 = {cube}")

# Square root using exponentiation
sqrt_16 = 16 ** 0.5
print(f"16 ** 0.5 = {sqrt_16}")

# Large numbers
large_power = 2 ** 10
print(f"2 ** 10 = {large_power}")

# 8. OPERATOR PRECEDENCE
print("\n8. OPERATOR PRECEDENCE")
print("-" * 30)

# Order of operations
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {result1} (multiplication first)")
print(f"(2 + 3) * 4 = {result2} (parentheses first)")

# Complex expression
complex_expr = 10 + 5 * 2 ** 3 - 6 // 2
print(f"10 + 5 * 2 ** 3 - 6 // 2 = {complex_expr}")

# Breaking down the complex expression
step1 = 2 ** 3  # 8
step2 = 5 * step1  # 40
step3 = 6 // 2  # 3
step4 = 10 + step2 - step3  # 10 + 40 - 3 = 47
print(f"Step by step: 2**3={step1}, 5*{step1}={step2}, 6//2={step3}, 10+{step2}-{step3}={step4}")

# 9. ASSIGNMENT OPERATORS
print("\n9. ASSIGNMENT OPERATORS")
print("-" * 30)

# Basic assignment
x = 10
print(f"x = {x}")

# Addition assignment
x += 5  # Same as x = x + 5
print(f"x += 5: {x}")

# Subtraction assignment
x -= 3  # Same as x = x - 3
print(f"x -= 3: {x}")

# Multiplication assignment
x *= 2  # Same as x = x * 2
print(f"x *= 2: {x}")

# Division assignment
x /= 4  # Same as x = x / 4
print(f"x /= 4: {x}")

# Floor division assignment
x //= 2  # Same as x = x // 2
print(f"x //= 2: {x}")

# Modulo assignment
x %= 3  # Same as x = x % 3
print(f"x %= 3: {x}")

# Exponentiation assignment
x **= 2  # Same as x = x ** 2
print(f"x **= 2: {x}")

# 10. PRACTICAL EXAMPLES
print("\n10. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Calculator
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '//':
        return a // b
    elif operation == '%':
        return a % b
    elif operation == '**':
        return a ** b
    else:
        return "Invalid operation"

print("Calculator examples:")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"17 // 5 = {calculator(17, 5, '//')}")
print(f"17 % 5 = {calculator(17, 5, '%')}")
print(f"2 ** 8 = {calculator(2, 8, '**')}")

# Example 2: Area and perimeter calculations
def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

circle_area, circle_circumference = calculate_circle(5)
rect_area, rect_perimeter = calculate_rectangle(4, 6)

print(f"\nCircle (radius=5):")
print(f"  Area: {circle_area:.2f}")
print(f"  Circumference: {circle_circumference:.2f}")

print(f"\nRectangle (4x6):")
print(f"  Area: {rect_area}")
print(f"  Perimeter: {rect_perimeter}")

# Example 3: Number manipulation
def analyze_number(num):
    is_even = num % 2 == 0
    is_divisible_by_3 = num % 3 == 0
    is_divisible_by_5 = num % 5 == 0
    square = num ** 2
    cube = num ** 3
    
    return {
        'number': num,
        'is_even': is_even,
        'is_divisible_by_3': is_divisible_by_3,
        'is_divisible_by_5': is_divisible_by_5,
        'square': square,
        'cube': cube
    }

number_analysis = analyze_number(15)
print(f"\nNumber analysis for 15:")
for key, value in number_analysis.items():
    print(f"  {key}: {value}")

# 11. SPECIAL CASES AND EDGE CASES
print("\n11. SPECIAL CASES AND EDGE CASES")
print("-" * 30)

# Division by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Division by zero error: {e}")

# Modulo with zero
try:
    result = 10 % 0
except ZeroDivisionError as e:
    print(f"Modulo by zero error: {e}")

# Large numbers
large_number = 2 ** 100
print(f"2 ** 100 = {large_number}")

# Float precision
float_calc = 0.1 + 0.2
print(f"0.1 + 0.2 = {float_calc}")
print(f"0.1 + 0.2 == 0.3: {float_calc == 0.3}")

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
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = p1 + p2
p4 = p1 - p2

print(f"Point arithmetic:")
print(f"  p1 = {p1}")
print(f"  p2 = {p2}")
print(f"  p1 + p2 = {p3}")
print(f"  p1 - p2 = {p4}")

# 13. SUMMARY
print("\n13. SUMMARY")
print("-" * 30)

print("Python Arithmetic Operators:")
print("┌─────────────┬─────────────┬─────────────┐")
print("│ Operator    │ Operation   │ Example     │")
print("├─────────────┼─────────────┼─────────────┤")
print("│ +           │ Addition    │ 5 + 3 = 8   │")
print("│ -           │ Subtraction │ 5 - 3 = 2   │")
print("│ *           │ Multiplication│ 5 * 3 = 15 │")
print("│ /           │ Division    │ 10 / 3 = 3.33│")
print("│ //          │ Floor Div   │ 10 // 3 = 3 │")
print("│ %           │ Modulo      │ 10 % 3 = 1  │")
print("│ **          │ Exponentiation│ 2 ** 3 = 8 │")
print("└─────────────┴─────────────┴─────────────┘")

print("\nOperator Precedence (highest to lowest):")
print("1. Parentheses ()")
print("2. Exponentiation **")
print("3. Multiplication *, Division /, Floor Division //, Modulo %")
print("4. Addition +, Subtraction -")

print("\nAssignment Operators:")
print("- += (addition assignment)")
print("- -= (subtraction assignment)")
print("- *= (multiplication assignment)")
print("- /= (division assignment)")
print("- //= (floor division assignment)")
print("- %= (modulo assignment)")
print("- **= (exponentiation assignment)")

print("\nKey Points:")
print("- Division (/) always returns a float")
print("- Floor division (//) returns an integer")
print("- Modulo (%) returns the remainder")
print("- Exponentiation (**) has highest precedence")
print("- Parentheses () override operator precedence") 