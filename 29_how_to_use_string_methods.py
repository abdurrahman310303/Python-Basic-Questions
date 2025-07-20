"""
29. How do you use string methods in Python?

String methods in Python provide various operations for manipulating and analyzing
strings. Python strings are immutable, so methods return new strings rather than
modifying the original string.
"""

print("=== STRING METHODS IN PYTHON ===\n")

# 1. BASIC STRING METHODS
print("1. BASIC STRING METHODS")
print("-" * 30)

# Sample string for demonstrations
text = "  Hello, World!  "
print(f"Original text: '{text}'")

# strip() - Remove whitespace from both ends
stripped = text.strip()
print(f"strip(): '{stripped}'")

# lstrip() - Remove whitespace from left
left_stripped = text.lstrip()
print(f"lstrip(): '{left_stripped}'")

# rstrip() - Remove whitespace from right
right_stripped = text.rstrip()
print(f"rstrip(): '{right_stripped}'")

# 2. CASE CONVERSION METHODS
print("\n2. CASE CONVERSION METHODS")
print("-" * 30)

sample_text = "Hello, World!"

# upper() - Convert to uppercase
upper_text = sample_text.upper()
print(f"upper(): '{upper_text}'")

# lower() - Convert to lowercase
lower_text = sample_text.lower()
print(f"lower(): '{lower_text}'")

# capitalize() - Capitalize first letter
capitalized = sample_text.capitalize()
print(f"capitalize(): '{capitalized}'")

# title() - Capitalize first letter of each word
title_text = sample_text.title()
print(f"title(): '{title_text}'")

# swapcase() - Swap case of all characters
swapped = sample_text.swapcase()
print(f"swapcase(): '{swapped}'")

# 3. SEARCH AND REPLACE METHODS
print("\n3. SEARCH AND REPLACE METHODS")
print("-" * 30)

text = "Hello, World! Hello, Python!"

# find() - Find first occurrence
position = text.find("Hello")
print(f"find('Hello'): {position}")

# rfind() - Find last occurrence
last_position = text.rfind("Hello")
print(f"rfind('Hello'): {last_position}")

# index() - Find first occurrence (raises error if not found)
try:
    index_pos = text.index("Python")
    print(f"index('Python'): {index_pos}")
except ValueError as e:
    print(f"index() error: {e}")

# replace() - Replace substring
replaced = text.replace("Hello", "Hi")
print(f"replace('Hello', 'Hi'): '{replaced}'")

# count() - Count occurrences
count = text.count("Hello")
print(f"count('Hello'): {count}")

# 4. SPLITTING AND JOINING METHODS
print("\n4. SPLITTING AND JOINING METHODS")
print("-" * 30)

text = "apple,banana,orange,grape"

# split() - Split by delimiter
fruits = text.split(",")
print(f"split(','): {fruits}")

# split() with max splits
limited_split = text.split(",", 2)
print(f"split(',', 2): {limited_split}")

# rsplit() - Split from right
right_split = text.rsplit(",", 2)
print(f"rsplit(',', 2): {right_split}")

# join() - Join list into string
joined = "-".join(fruits)
print(f"join with '-': '{joined}'")

# splitlines() - Split by lines
multiline_text = "Line 1\nLine 2\nLine 3"
lines = multiline_text.splitlines()
print(f"splitlines(): {lines}")

# 5. CHECKING METHODS
print("\n5. CHECKING METHODS")
print("-" * 30)

# isalpha() - Check if all characters are alphabetic
alpha_text = "Hello"
print(f"'{alpha_text}'.isalpha(): {alpha_text.isalpha()}")

# isdigit() - Check if all characters are digits
digit_text = "12345"
print(f"'{digit_text}'.isdigit(): {digit_text.isdigit()}")

# isnumeric() - Check if all characters are numeric
numeric_text = "123.45"
print(f"'{numeric_text}'.isnumeric(): {numeric_text.isnumeric()}")

# isalnum() - Check if all characters are alphanumeric
alnum_text = "Hello123"
print(f"'{alnum_text}'.isalnum(): {alnum_text.isalnum()}")

# isspace() - Check if all characters are whitespace
space_text = "   "
print(f"'{space_text}'.isspace(): {space_text.isspace()}")

# islower() - Check if all characters are lowercase
lower_text = "hello"
print(f"'{lower_text}'.islower(): {lower_text.islower()}")

# isupper() - Check if all characters are uppercase
upper_text = "HELLO"
print(f"'{upper_text}'.isupper(): {upper_text.isupper()}")

# istitle() - Check if string is title case
title_text = "Hello World"
print(f"'{title_text}'.istitle(): {title_text.istitle()}")

# 6. PADDING AND ALIGNMENT METHODS
print("\n6. PADDING AND ALIGNMENT METHODS")
print("-" * 30)

text = "Hello"

# center() - Center string with padding
centered = text.center(10, "*")
print(f"center(10, '*'): '{centered}'")

# ljust() - Left justify with padding
left_justified = text.ljust(10, "-")
print(f"ljust(10, '-'): '{left_justified}'")

# rjust() - Right justify with padding
right_justified = text.rjust(10, "=")
print(f"rjust(10, '='): '{right_justified}'")

# zfill() - Zero fill
zero_filled = text.zfill(10)
print(f"zfill(10): '{zero_filled}'")

# 7. FORMATTING METHODS
print("\n7. FORMATTING METHODS")
print("-" * 30)

# format() - String formatting
name = "Alice"
age = 25
formatted = "Name: {}, Age: {}".format(name, age)
print(f"format(): '{formatted}'")

# f-string (modern formatting)
f_formatted = f"Name: {name}, Age: {age}"
print(f"f-string: '{f_formatted}'")

# 8. ENCODING AND DECODING METHODS
print("\n8. ENCODING AND DECODING METHODS")
print("-" * 30)

text = "Hello, World!"

# encode() - Encode string to bytes
encoded = text.encode('utf-8')
print(f"encode('utf-8'): {encoded}")

# decode() - Decode bytes to string
decoded = encoded.decode('utf-8')
print(f"decode('utf-8'): '{decoded}'")

# 9. ADVANCED STRING METHODS
print("\n9. ADVANCED STRING METHODS")
print("-" * 30)

text = "Hello, World! Hello, Python!"

# startswith() - Check if string starts with prefix
starts_with = text.startswith("Hello")
print(f"startswith('Hello'): {starts_with}")

# endswith() - Check if string ends with suffix
ends_with = text.endswith("Python!")
print(f"endswith('Python!'): {ends_with}")

# expandtabs() - Expand tab characters
tabbed_text = "Hello\tWorld\tPython"
expanded = tabbed_text.expandtabs(4)
print(f"expandtabs(4): '{expanded}'")

# 10. STRING METHODS WITH REGULAR EXPRESSIONS
print("\n10. STRING METHODS WITH REGULAR EXPRESSIONS")
print("-" * 30)

import re

text = "Hello123World456Python"

# Using re.split() for complex splitting
split_by_digits = re.split(r'\d+', text)
print(f"re.split(r'\\d+', text): {split_by_digits}")

# Using re.sub() for complex replacement
replaced_digits = re.sub(r'\d+', 'NUMBER', text)
print(f"re.sub(r'\\d+', 'NUMBER', text): '{replaced_digits}'")

# 11. PRACTICAL STRING METHOD EXAMPLES
print("\n11. PRACTICAL STRING METHOD EXAMPLES")
print("-" * 30)

# Example 1: Cleaning user input
user_input = "  John Doe  "
cleaned = user_input.strip().title()
print(f"Cleaned input: '{cleaned}'")

# Example 2: Checking email format
email = "user@example.com"
is_valid_email = "@" in email and "." in email and email.count("@") == 1
print(f"Valid email: {is_valid_email}")

# Example 3: Converting case for display
product_name = "python programming book"
display_name = product_name.title()
print(f"Display name: '{display_name}'")

# Example 4: Parsing CSV-like data
csv_line = "apple,banana,orange"
fruits = csv_line.split(",")
print(f"Parsed fruits: {fruits}")

# 12. STRING METHOD CHAINING
print("\n12. STRING METHOD CHAINING")
print("-" * 30)

# Chain multiple string methods
messy_text = "  HELLO world  "
cleaned_text = messy_text.strip().lower().title()
print(f"Original: '{messy_text}'")
print(f"Chained methods: '{cleaned_text}'")

# Complex chaining example
data = "  USER123@EXAMPLE.COM  "
processed = data.strip().lower().replace("@", " at ")
print(f"Original: '{data}'")
print(f"Processed: '{processed}'")

# 13. STRING METHODS WITH CUSTOM FUNCTIONS
print("\n13. STRING METHODS WITH CUSTOM FUNCTIONS")
print("-" * 30)

def clean_and_format(text):
    """Clean and format text using string methods."""
    return text.strip().lower().title()

def extract_numbers(text):
    """Extract numbers from text."""
    return ''.join(char for char in text if char.isdigit())

def validate_phone(phone):
    """Validate phone number format."""
    cleaned = phone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    return cleaned.isdigit() and len(cleaned) == 10

# Testing custom functions
sample_text = "  hello world  "
print(f"clean_and_format('{sample_text}'): '{clean_and_format(sample_text)}'")

phone_text = "123-456-7890"
print(f"validate_phone('{phone_text}'): {validate_phone(phone_text)}")

mixed_text = "abc123def456"
print(f"extract_numbers('{mixed_text}'): '{extract_numbers(mixed_text)}'")

# 14. STRING METHODS PERFORMANCE
print("\n14. STRING METHODS PERFORMANCE")
print("-" * 30)

import time

# Performance comparison
large_text = "Hello, World! " * 1000

# Method 1: Using strip()
start = time.time()
for _ in range(1000):
    result = large_text.strip()
strip_time = time.time() - start

# Method 2: Using replace() for whitespace
start = time.time()
for _ in range(1000):
    result = large_text.replace(" ", "")
replace_time = time.time() - start

print(f"strip() time: {strip_time:.4f} seconds")
print(f"replace() time: {replace_time:.4f} seconds")

# 15. STRING METHODS BEST PRACTICES
print("\n15. STRING METHODS BEST PRACTICES")
print("-" * 30)

print("String Methods Best Practices:")
print("1. Remember that strings are immutable")
print("2. Use appropriate methods for the task")
print("3. Chain methods for complex operations")
print("4. Handle encoding properly")
print("5. Use raw strings for regex patterns")
print("6. Consider performance for large strings")
print("7. Validate input before processing")

# Good practice: Handle encoding
def safe_encode(text, encoding='utf-8'):
    """Safely encode text with error handling."""
    try:
        return text.encode(encoding)
    except UnicodeEncodeError:
        return text.encode(encoding, errors='ignore')

# Good practice: Validate before processing
def safe_process(text):
    """Safely process text with validation."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip().lower()

# 16. SUMMARY
print("\n16. SUMMARY")
print("-" * 30)

print("What are String Methods?")
print("- Built-in functions for string manipulation")
print("- Return new strings (strings are immutable)")
print("- Provide various text processing capabilities")
print("- Support different encodings and formats")

print("\nCommon String Method Categories:")
print("- Case conversion: upper(), lower(), title(), capitalize()")
print("- Whitespace: strip(), lstrip(), rstrip()")
print("- Search: find(), index(), count(), startswith(), endswith()")
print("- Replace: replace()")
print("- Split/Join: split(), join(), splitlines()")
print("- Check: isalpha(), isdigit(), isalnum(), etc.")
print("- Format: format(), f-strings")
print("- Padding: center(), ljust(), rjust(), zfill()")

print("\nBest Practices:")
print("- Remember strings are immutable")
print("- Use appropriate methods for the task")
print("- Chain methods for complex operations")
print("- Handle encoding properly")
print("- Validate input before processing")
print("- Consider performance for large strings")
print("- Use raw strings for regex patterns")

print("\nCommon Use Cases:")
print("- Data cleaning and validation")
print("- Text processing and analysis")
print("- User input handling")
print("- File and data parsing")
print("- Text formatting and display")
print("- Encoding and decoding")
print("- Pattern matching and replacement") 