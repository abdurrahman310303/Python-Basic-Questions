"""
24. How do you use slicing in Python?

Slicing in Python allows you to extract a portion of a sequence (list, tuple, string)
using the syntax [start:stop:step]. It's a powerful and efficient way to work with
sequences without modifying the original data.
"""

print("=== SLICING IN PYTHON ===\n")

# 1. BASIC SLICING SYNTAX
print("1. BASIC SLICING SYNTAX")
print("-" * 30)

# Basic syntax: sequence[start:stop:step]
# start: beginning index (inclusive)
# stop: ending index (exclusive)
# step: step size (optional, default is 1)

# Example with list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Basic slicing
first_three = numbers[0:3]
print(f"First three elements: {first_three}")

# Using default start (0)
first_five = numbers[:5]
print(f"First five elements: {first_five}")

# Using default stop (end of sequence)
last_three = numbers[7:]
print(f"Last three elements: {last_three}")

# 2. SLICING WITH STRINGS
print("\n2. SLICING WITH STRINGS")
print("-" * 30)

# String slicing
text = "Hello, World!"
print(f"Original string: '{text}'")

# Get first 5 characters
first_five_chars = text[:5]
print(f"First 5 characters: '{first_five_chars}'")

# Get last 6 characters
last_six_chars = text[-6:]
print(f"Last 6 characters: '{last_six_chars}'")

# Get characters from index 2 to 8
middle_chars = text[2:8]
print(f"Characters from index 2 to 8: '{middle_chars}'")

# 3. NEGATIVE INDICES
print("\n3. NEGATIVE INDICES")
print("-" * 30)

# Negative indices count from the end
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Last element
last_element = numbers[-1]
print(f"Last element: {last_element}")

# Last three elements
last_three = numbers[-3:]
print(f"Last three elements: {last_three}")

# All elements except last three
all_except_last_three = numbers[:-3]
print(f"All except last three: {all_except_last_three}")

# From third to last to second to last
middle_negative = numbers[-3:-1]
print(f"From third to last to second to last: {middle_negative}")

# 4. STEP PARAMETER
print("\n4. STEP PARAMETER")
print("-" * 30)

# Step parameter controls the stride
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Every second element
every_second = numbers[::2]
print(f"Every second element: {every_second}")

# Every third element
every_third = numbers[::3]
print(f"Every third element: {every_third}")

# Reverse the sequence
reversed_list = numbers[::-1]
print(f"Reversed list: {reversed_list}")

# Every second element in reverse
reverse_every_second = numbers[::-2]
print(f"Every second element in reverse: {reverse_every_second}")

# 5. SLICING WITH DIFFERENT DATA TYPES
print("\n5. SLICING WITH DIFFERENT DATA TYPES")
print("-" * 30)

# Lists
list_data = [1, 2, 3, 4, 5]
print(f"List slice [1:4]: {list_data[1:4]}")

# Tuples
tuple_data = (1, 2, 3, 4, 5)
print(f"Tuple slice [1:4]: {tuple_data[1:4]}")

# Strings
string_data = "Python"
print(f"String slice [1:4]: '{string_data[1:4]}'")

# Bytes
bytes_data = b'Python'
print(f"Bytes slice [1:4]: {bytes_data[1:4]}")

# 6. ADVANCED SLICING PATTERNS
print("\n6. ADVANCED SLICING PATTERNS")
print("-" * 30)

# Pattern 1: Get middle portion
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle = data[3:7]
print(f"Middle portion [3:7]: {middle}")

# Pattern 2: Get every nth element
every_fourth = data[::4]
print(f"Every fourth element: {every_fourth}")

# Pattern 3: Get elements in reverse order
reverse_order = data[::-1]
print(f"Reverse order: {reverse_order}")

# Pattern 4: Get last n elements
last_five = data[-5:]
print(f"Last five elements: {last_five}")

# Pattern 5: Get all elements except first and last
without_ends = data[1:-1]
print(f"Without first and last: {without_ends}")

# 7. SLICING WITH STRINGS - ADVANCED
print("\n7. SLICING WITH STRINGS - ADVANCED")
print("-" * 30)

# String manipulation
text = "Hello, World!"
print(f"Original text: '{text}'")

# Get word "Hello"
hello = text[:5]
print(f"Word 'Hello': '{hello}'")

# Get word "World"
world = text[7:12]
print(f"Word 'World': '{world}'")

# Reverse string
reversed_text = text[::-1]
print(f"Reversed text: '{reversed_text}'")

# Get every second character
every_second_char = text[::2]
print(f"Every second character: '{every_second_char}'")

# Remove punctuation
no_punctuation = text[:-1]
print(f"Without exclamation mark: '{no_punctuation}'")

# 8. PRACTICAL SLICING EXAMPLES
print("\n8. PRACTICAL SLICING EXAMPLES")
print("-" * 30)

# Example 1: Data processing
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Get first half
first_half = data[:len(data)//2]
print(f"First half: {first_half}")

# Get second half
second_half = data[len(data)//2:]
print(f"Second half: {second_half}")

# Get every other element
alternating = data[::2]
print(f"Every other element: {alternating}")

# Example 2: String processing
filename = "document.txt"

# Get name without extension
name_without_ext = filename[:-4]
print(f"Filename without extension: '{name_without_ext}'")

# Get extension
extension = filename[-3:]
print(f"Extension: '{extension}'")

# Example 3: URL processing
url = "https://www.example.com/path"

# Get domain
domain_start = url.find("://") + 3
domain_end = url.find("/", domain_start)
domain = url[domain_start:domain_end]
print(f"Domain: '{domain}'")

# 9. SLICING WITH NEGATIVE STEP
print("\n9. SLICING WITH NEGATIVE STEP")
print("-" * 30)

# Negative step reverses the order
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}")

# Reverse the entire list
reversed_list = numbers[::-1]
print(f"Reversed list: {reversed_list}")

# Get last 5 elements in reverse
last_five_reverse = numbers[-1:-6:-1]
print(f"Last 5 elements in reverse: {last_five_reverse}")

# Get every second element in reverse
reverse_every_second = numbers[::-2]
print(f"Every second element in reverse: {reverse_every_second}")

# 10. SLICING WITH COMPLEX PATTERNS
print("\n10. SLICING WITH COMPLEX PATTERNS")
print("-" * 30)

# Pattern 1: Extract sublists
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get first, middle, and last thirds
first_third = data[:len(data)//3]
middle_third = data[len(data)//3:2*len(data)//3]
last_third = data[2*len(data)//3:]

print(f"First third: {first_third}")
print(f"Middle third: {middle_third}")
print(f"Last third: {last_third}")

# Pattern 2: Extract alternating elements
alternating_pairs = data[::2]  # Even indices
alternating_pairs_odd = data[1::2]  # Odd indices

print(f"Even-indexed elements: {alternating_pairs}")
print(f"Odd-indexed elements: {alternating_pairs_odd}")

# Pattern 3: Extract palindrome check
def is_palindrome(text):
    return text == text[::-1]

test_strings = ["racecar", "hello", "anna", "python"]
for s in test_strings:
    print(f"'{s}' is palindrome: {is_palindrome(s)}")

# 11. SLICING PERFORMANCE
print("\n11. SLICING PERFORMANCE")
print("-" * 30)

# Slicing creates a new object (shallow copy)
original = [1, 2, 3, 4, 5]
sliced = original[1:4]

print(f"Original: {original}")
print(f"Sliced: {sliced}")

# Modifying sliced doesn't affect original
sliced[0] = 99
print(f"After modifying sliced: {sliced}")
print(f"Original unchanged: {original}")

# Memory efficiency
import sys
large_list = list(range(1000000))
slice_small = large_list[:1000]
print(f"Original list size: {sys.getsizeof(large_list)} bytes")
print(f"Small slice size: {sys.getsizeof(slice_small)} bytes")

# 12. SLICING WITH CUSTOM OBJECTS
print("\n12. SLICING WITH CUSTOM OBJECTS")
print("-" * 30)

# Custom class with slicing support
class SliceableList:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return SliceableList(self.data[key])
        return self.data[key]
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)

# Using custom sliceable object
custom_list = SliceableList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Custom list: {custom_list}")

sliced_custom = custom_list[2:7]
print(f"Sliced custom list: {sliced_custom}")

# 13. COMMON SLICING PATTERNS
print("\n13. COMMON SLICING PATTERNS")
print("-" * 30)

# Pattern 1: Get first n elements
def get_first_n(sequence, n):
    return sequence[:n]

# Pattern 2: Get last n elements
def get_last_n(sequence, n):
    return sequence[-n:]

# Pattern 3: Remove first n elements
def remove_first_n(sequence, n):
    return sequence[n:]

# Pattern 4: Remove last n elements
def remove_last_n(sequence, n):
    return sequence[:-n]

# Pattern 5: Get middle portion
def get_middle(sequence, start, end):
    return sequence[start:end]

# Testing patterns
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {test_data}")
print(f"First 3: {get_first_n(test_data, 3)}")
print(f"Last 3: {get_last_n(test_data, 3)}")
print(f"Remove first 2: {remove_first_n(test_data, 2)}")
print(f"Remove last 2: {remove_last_n(test_data, 2)}")
print(f"Middle [3:7]: {get_middle(test_data, 3, 7)}")

# 14. SLICING BEST PRACTICES
print("\n14. SLICING BEST PRACTICES")
print("-" * 30)

print("Slicing Best Practices:")
print("1. Use descriptive variable names for slices")
print("2. Be aware that slicing creates a copy")
print("3. Use negative indices for end-relative access")
print("4. Use step parameter for efficient iteration")
print("5. Test edge cases (empty sequences, single elements)")
print("6. Consider memory usage for large sequences")
print("7. Use slicing for read-only operations")

# Good slicing practices
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Good: Descriptive names
first_half = data[:len(data)//2]
second_half = data[len(data)//2:]

# Good: Use negative indices
last_three = data[-3:]
all_except_last = data[:-1]

# Good: Use step for efficiency
every_second = data[::2]

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What is Slicing?")
print("- Way to extract portions of sequences")
print("- Uses [start:stop:step] syntax")
print("- Creates a new object (shallow copy)")
print("- Works with lists, tuples, strings, bytes")

print("\nBasic Syntax:")
print("- sequence[start:stop:step]")
print("- start: beginning index (inclusive)")
print("- stop: ending index (exclusive)")
print("- step: step size (optional)")

print("\nIndex Types:")
print("- Positive: count from beginning")
print("- Negative: count from end")
print("- Zero: first element")
print("- None: use default")

print("\nCommon Patterns:")
print("- sequence[:n] - first n elements")
print("- sequence[-n:] - last n elements")
print("- sequence[n:] - all except first n")
print("- sequence[:-n] - all except last n")
print("- sequence[::2] - every second element")
print("- sequence[::-1] - reverse")

print("\nUse Cases:")
print("- Data extraction")
print("- String manipulation")
print("- List processing")
print("- Palindrome checking")
print("- Data partitioning")
print("- Efficient iteration")

print("\nBest Practices:")
print("- Use descriptive variable names")
print("- Be aware of memory usage")
print("- Test edge cases")
print("- Use negative indices when appropriate")
print("- Consider performance for large sequences")
print("- Use for read-only operations") 