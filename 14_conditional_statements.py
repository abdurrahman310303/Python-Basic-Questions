"""
14. What are conditional statements in Python?

Conditional statements in Python allow you to execute different blocks of code
based on whether certain conditions are true or false. The main conditional
statements are if, elif, and else.
"""

print("=== CONDITIONAL STATEMENTS IN PYTHON ===\n")

# 1. BASIC IF STATEMENT
print("1. BASIC IF STATEMENT")
print("-" * 30)

age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")

# Simple condition
x = 10
if x > 5:
    print("x is greater than 5")

# 2. IF-ELSE STATEMENT
print("\n2. IF-ELSE STATEMENT")
print("-" * 30)

age = 16

if age >= 18:
    print("You are an adult")
    print("You can vote")
else:
    print("You are a minor")
    print("You cannot vote")

# Another example
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 3. IF-ELIF-ELSE STATEMENT
print("\n3. IF-ELIF-ELSE STATEMENT")
print("-" * 30)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Temperature example
temperature = 25

if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's warm")
elif temperature > 10:
    print("It's cool")
else:
    print("It's cold")

# 4. NESTED CONDITIONAL STATEMENTS
print("\n4. NESTED CONDITIONAL STATEMENTS")
print("-" * 30)

age = 25
income = 50000

if age >= 18:
    print("You are an adult")
    if income >= 50000:
        print("You have a good income")
        if income >= 100000:
            print("You are in the high-income bracket")
        else:
            print("You are in the middle-income bracket")
    else:
        print("You have a lower income")
else:
    print("You are a minor")

# 5. COMPARISON OPERATORS
print("\n5. COMPARISON OPERATORS")
print("-" * 30)

a = 10
b = 5

# Equal to
if a == b:
    print("a equals b")
else:
    print("a does not equal b")

# Not equal to
if a != b:
    print("a is not equal to b")

# Greater than
if a > b:
    print("a is greater than b")

# Less than
if b < a:
    print("b is less than a")

# Greater than or equal to
if a >= b:
    print("a is greater than or equal to b")

# Less than or equal to
if b <= a:
    print("b is less than or equal to a")

# 6. LOGICAL OPERATORS
print("\n6. LOGICAL OPERATORS")
print("-" * 30)

age = 25
income = 60000
has_credit = True

# AND operator
if age >= 18 and income >= 50000:
    print("You qualify for the loan")

# OR operator
if age >= 18 or has_credit:
    print("You can apply for credit")

# NOT operator
if not has_credit:
    print("You need to build credit first")

# Complex logical expressions
if (age >= 18 and income >= 50000) or has_credit:
    print("You qualify for the premium card")

# 7. MEMBERSHIP OPERATORS
print("\n7. MEMBERSHIP OPERATORS")
print("-" * 30)

fruits = ["apple", "banana", "orange"]
user_fruit = "apple"

# IN operator
if user_fruit in fruits:
    print(f"{user_fruit} is available")

# NOT IN operator
if "grape" not in fruits:
    print("Grape is not available")

# String membership
text = "Hello, World!"
if "Hello" in text:
    print("'Hello' is in the text")

# 8. IDENTITY OPERATORS
print("\n8. IDENTITY OPERATORS")
print("-" * 30)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# IS operator (identity)
if x is z:
    print("x and z are the same object")

# IS NOT operator
if x is not y:
    print("x and y are different objects")

# Comparison vs Identity
if x == y:
    print("x and y have the same values")

if x is y:
    print("x and y are the same object")

# 9. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
print("\n9. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)")
print("-" * 30)

age = 20

# Traditional if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator
status = "adult" if age >= 18 else "minor"

print(f"Status: {status}")

# More examples
x = 10
y = 5
max_value = x if x > y else y
print(f"Maximum value: {max_value}")

number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}")

# 10. PRACTICAL EXAMPLES
print("\n10. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Grade calculator
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"Grade for 85: {calculate_grade(85)}")
print(f"Grade for 92: {calculate_grade(92)}")
print(f"Grade for 55: {calculate_grade(55)}")

# Example 2: Password validation
def validate_password(password):
    if len(password) < 8:
        return "Password too short"
    elif not any(c.isupper() for c in password):
        return "Password needs uppercase letter"
    elif not any(c.islower() for c in password):
        return "Password needs lowercase letter"
    elif not any(c.isdigit() for c in password):
        return "Password needs a number"
    else:
        return "Password is valid"

print(f"Password 'abc': {validate_password('abc')}")
print(f"Password 'Abc123': {validate_password('Abc123')}")
print(f"Password 'Abc12345': {validate_password('Abc12345')}")

# Example 3: Discount calculator
def calculate_discount(amount, customer_type):
    if customer_type == "premium":
        if amount >= 1000:
            discount = 0.20
        else:
            discount = 0.15
    elif customer_type == "regular":
        if amount >= 500:
            discount = 0.10
        else:
            discount = 0.05
    else:
        discount = 0.02
    
    final_amount = amount * (1 - discount)
    return final_amount

print(f"Premium customer, $1200: ${calculate_discount(1200, 'premium'):.2f}")
print(f"Regular customer, $600: ${calculate_discount(600, 'regular'):.2f}")
print(f"New customer, $300: ${calculate_discount(300, 'new'):.2f}")

# 11. ADVANCED CONDITIONAL PATTERNS
print("\n11. ADVANCED CONDITIONAL PATTERNS")
print("-" * 30)

# Pattern 1: Multiple conditions with any/all
numbers = [2, 4, 6, 8, 10]

if all(num % 2 == 0 for num in numbers):
    print("All numbers are even")

if any(num > 5 for num in numbers):
    print("At least one number is greater than 5")

# Pattern 2: Dictionary-based conditions
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

# Pattern 3: Chained comparisons
age = 25
if 18 <= age <= 65:
    print("Working age")

x = 5
if 0 < x < 10:
    print("x is between 0 and 10")

# 12. COMMON MISTAKES
print("\n12. COMMON MISTAKES")
print("-" * 30)

# Mistake 1: Using = instead of ==
x = 5
# if x = 5:  # This would cause an error
if x == 5:
    print("x equals 5")

# Mistake 2: Not using proper indentation
# if x > 0:
# print("Positive")  # This would cause an error
if x > 0:
    print("Positive")

# Mistake 3: Forgetting else clause
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"  # Don't forget the else case

# 13. CONDITIONAL STATEMENTS WITH DATA STRUCTURES
print("\n13. CONDITIONAL STATEMENTS WITH DATA STRUCTURES")
print("-" * 30)

# Lists
numbers = [1, 2, 3, 4, 5]
if numbers:  # Check if list is not empty
    print(f"List has {len(numbers)} items")
else:
    print("List is empty")

# Dictionaries
person = {"name": "John", "age": 30}
if "age" in person:
    print(f"Age: {person['age']}")

# Sets
fruits = {"apple", "banana", "orange"}
if "apple" in fruits:
    print("Apple is available")

# 14. SUMMARY
print("\n14. SUMMARY")
print("-" * 30)

print("Conditional Statement Types:")
print("1. if - executes if condition is True")
print("2. elif - executes if previous conditions were False and this condition is True")
print("3. else - executes if all previous conditions were False")

print("\nComparison Operators:")
print("- == (equal to)")
print("- != (not equal to)")
print("- > (greater than)")
print("- < (less than)")
print("- >= (greater than or equal to)")
print("- <= (less than or equal to)")

print("\nLogical Operators:")
print("- and (both conditions must be True)")
print("- or (at least one condition must be True)")
print("- not (inverts the condition)")

print("\nMembership Operators:")
print("- in (checks if value is in sequence)")
print("- not in (checks if value is not in sequence)")

print("\nIdentity Operators:")
print("- is (checks if objects are the same)")
print("- is not (checks if objects are different)")

print("\nBest Practices:")
print("- Use clear, descriptive conditions")
print("- Avoid deeply nested conditions")
print("- Use parentheses for complex expressions")
print("- Consider using early returns")
print("- Use appropriate comparison operators")
print("- Handle all possible cases") 