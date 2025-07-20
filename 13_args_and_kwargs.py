"""
13. What are *args and **kwargs?

*args and **kwargs are special syntax in Python that allow functions to accept
a variable number of arguments. *args is for positional arguments, **kwargs is for keyword arguments.
"""

print("=== *ARGS AND **KWARGS IN PYTHON ===\n")

# 1. *ARGS - ARBITRARY POSITIONAL ARGUMENTS
print("1. *ARGS - ARBITRARY POSITIONAL ARGUMENTS")
print("-" * 30)

def sum_all(*args):
    """Sum all provided numbers."""
    total = 0
    for num in args:
        total += num
    return total

# Using *args with different numbers of arguments
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40) = {sum_all(10, 20, 30, 40)}")
print(f"sum_all(5) = {sum_all(5)}")
print(f"sum_all() = {sum_all()}")

def print_args(*args):
    """Print all positional arguments."""
    print(f"Number of arguments: {len(args)}")
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")

print("\nTesting print_args:")
print_args("apple", "banana", "cherry")
print_args(1, 2, 3, 4, 5)

# 2. **KWARGS - ARBITRARY KEYWORD ARGUMENTS
print("\n2. **KWARGS - ARBITRARY KEYWORD ARGUMENTS")
print("-" * 30)

def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using **kwargs
print("Person information:")
print_info(name="John", age=30, city="New York", occupation="Engineer")

print("\nProduct information:")
print_info(product="Laptop", price=999.99, brand="Dell", warranty="2 years")

def create_profile(**kwargs):
    """Create a user profile from keyword arguments."""
    profile = {
        "name": kwargs.get("name", "Unknown"),
        "age": kwargs.get("age", 0),
        "email": kwargs.get("email", ""),
        "city": kwargs.get("city", "Unknown")
    }
    return profile

# Creating profiles with different arguments
profile1 = create_profile(name="Alice", age=25, email="alice@example.com")
profile2 = create_profile(name="Bob", city="Boston")
profile3 = create_profile()

print(f"\nProfile 1: {profile1}")
print(f"Profile 2: {profile2}")
print(f"Profile 3: {profile3}")

# 3. COMBINING *ARGS AND **KWARGS
print("\n3. COMBINING *ARGS AND **KWARGS")
print("-" * 30)

def flexible_function(*args, **kwargs):
    """Function that accepts both positional and keyword arguments."""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

# Using both *args and **kwargs
flexible_function(1, 2, 3, name="John", age=30)
flexible_function("hello", "world", city="New York", country="USA")

def process_data(*args, **kwargs):
    """Process data with both types of arguments."""
    result = {
        "positional_count": len(args),
        "keyword_count": len(kwargs),
        "positional_values": args,
        "keyword_values": kwargs
    }
    return result

data = process_data(1, 2, 3, name="Alice", age=25, city="Boston")
print(f"\nProcessed data: {data}")

# 4. UNPACKING WITH *ARGS AND **KWARGS
print("\n4. UNPACKING WITH *ARGS AND **KWARGS")
print("-" * 30)

# Unpacking lists with *args
numbers = [1, 2, 3, 4, 5]
print(f"Unpacking list: {sum_all(*numbers)}")

# Unpacking tuples with *args
coordinates = (10, 20, 30)
print(f"Unpacking tuple: {sum_all(*coordinates)}")

# Unpacking dictionaries with **kwargs
person_info = {"name": "John", "age": 30, "city": "New York"}
print_info(**person_info)

# 5. PRACTICAL EXAMPLES
print("\n5. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Calculator with *args
def calculate_average(*args):
    """Calculate average of any number of values."""
    if not args:
        return 0
    return sum(args) / len(args)

print(f"Average of 1, 2, 3, 4, 5: {calculate_average(1, 2, 3, 4, 5)}")
print(f"Average of 10, 20: {calculate_average(10, 20)}")

# Example 2: Database query builder with **kwargs
def build_query(table, **kwargs):
    """Build SQL WHERE clause from keyword arguments."""
    query = f"SELECT * FROM {table}"
    if kwargs:
        conditions = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = '{value}'")
        query += " WHERE " + " AND ".join(conditions)
    return query

print(f"Query 1: {build_query('users', name='John', age=30)}")
print(f"Query 2: {build_query('products', category='electronics', price=100)}")

# Example 3: Configuration function
def create_config(**kwargs):
    """Create configuration with defaults."""
    config = {
        "debug": False,
        "timeout": 30,
        "max_retries": 3,
        "host": "localhost",
        "port": 8080
    }
    config.update(kwargs)  # Override defaults with provided values
    return config

print(f"Default config: {create_config()}")
print(f"Custom config: {create_config(debug=True, timeout=60, host='example.com')}")

# 6. ADVANCED USAGE
print("\n6. ADVANCED USAGE")
print("-" * 30)

# Function decorator with *args and **kwargs
def timer(func):
    """Decorator to measure function execution time."""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    return wrapper

@timer
def slow_function(*args, **kwargs):
    """A function that takes time to execute."""
    import time
    time.sleep(0.1)
    return f"Processed {len(args)} args and {len(kwargs)} kwargs"

result = slow_function(1, 2, 3, name="test", value=42)
print(f"Result: {result}")

# 7. COMMON PATTERNS
print("\n7. COMMON PATTERNS")
print("-" * 30)

# Pattern 1: Wrapper functions
def safe_function(func, *args, **kwargs):
    """Safely execute a function with error handling."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error: {e}")
        return None

def divide(a, b):
    return a / b

print(f"Safe division: {safe_function(divide, 10, 2)}")
print(f"Safe division (error): {safe_function(divide, 10, 0)}")

# Pattern 2: Function composition
def compose(*functions):
    """Compose multiple functions."""
    def composed(*args, **kwargs):
        result = functions[0](*args, **kwargs)
        for func in functions[1:]:
            result = func(result)
        return result
    return composed

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def square(x):
    return x ** 2

composed_func = compose(add_one, multiply_by_two, square)
print(f"Composed function result: {composed_func(3)}")

# Pattern 3: Configuration merging
def merge_configs(*configs):
    """Merge multiple configuration dictionaries."""
    merged = {}
    for config in configs:
        merged.update(config)
    return merged

config1 = {"debug": True, "timeout": 30}
config2 = {"host": "localhost", "port": 8080}
config3 = {"timeout": 60, "max_retries": 5}

merged_config = merge_configs(config1, config2, config3)
print(f"Merged config: {merged_config}")

# 8. *ARGS AND **KWARGS IN CLASS METHODS
print("\n8. *ARGS AND **KWARGS IN CLASS METHODS")
print("-" * 30)

class DataProcessor:
    def __init__(self, **kwargs):
        """Initialize with keyword arguments."""
        self.config = kwargs
    
    def process_data(self, *args, **kwargs):
        """Process data with flexible arguments."""
        print(f"Processing {len(args)} data items")
        print(f"With {len(kwargs)} additional parameters")
        
        result = {
            "data_count": len(args),
            "data_items": args,
            "parameters": kwargs,
            "config": self.config
        }
        return result

processor = DataProcessor(debug=True, timeout=30)
result = processor.process_data(1, 2, 3, 4, 5, batch_size=10, validate=True)
print(f"Processing result: {result}")

# 9. UNPACKING IN FUNCTION CALLS
print("\n9. UNPACKING IN FUNCTION CALLS")
print("-" * 30)

def greet(name, age, city):
    """Greet a person with their details."""
    return f"Hello {name}, you are {age} years old from {city}"

# Using unpacking to call function
person_data = ["Alice", 25, "Boston"]
print(f"Greeting: {greet(*person_data)}")

person_info = {"name": "Bob", "age": 30, "city": "New York"}
print(f"Greeting: {greet(**person_info)}")

# 10. BEST PRACTICES
print("\n10. BEST PRACTICES")
print("-" * 30)

# Good: Clear parameter names
def process_items(*items, **options):
    """Process items with options."""
    print(f"Processing {len(items)} items")
    print(f"Options: {options}")

# Good: Document expected arguments
def create_user(*args, **kwargs):
    """
    Create a user with flexible arguments.
    
    Args:
        *args: Positional arguments (name, age, email, etc.)
        **kwargs: Keyword arguments (name, age, email, city, etc.)
    """
    user = {
        "name": kwargs.get("name", args[0] if args else "Unknown"),
        "age": kwargs.get("age", args[1] if len(args) > 1 else 0),
        "email": kwargs.get("email", args[2] if len(args) > 2 else ""),
        "city": kwargs.get("city", "Unknown")
    }
    return user

# Good: Use defaults appropriately
def flexible_config(**kwargs):
    """Create configuration with sensible defaults."""
    config = {
        "debug": False,
        "timeout": 30,
        "max_retries": 3
    }
    config.update(kwargs)
    return config

# 11. COMMON MISTAKES
print("\n11. COMMON MISTAKES")
print("-" * 30)

# Mistake 1: Forgetting that *args is a tuple
def bad_example(*args):
    # args[0] = "new value"  # This would cause an error - tuples are immutable
    pass

# Mistake 2: Not handling empty *args
def better_example(*args):
    if not args:
        return "No arguments provided"
    return f"Got {len(args)} arguments"

# Mistake 3: Not using .get() for **kwargs
def safe_kwargs(**kwargs):
    # Use .get() to avoid KeyError
    name = kwargs.get("name", "Unknown")
    age = kwargs.get("age", 0)
    return f"{name} is {age} years old"

# 12. SUMMARY
print("\n12. SUMMARY")
print("-" * 30)

print("Key Points about *args and **kwargs:")
print("1. *args collects positional arguments into a tuple")
print("2. **kwargs collects keyword arguments into a dictionary")
print("3. They allow functions to accept variable numbers of arguments")
print("4. They can be used together in the same function")
print("5. They can be unpacked when calling functions")

print("\nWhen to Use:")
print("- *args: When you need variable positional arguments")
print("- **kwargs: When you need variable keyword arguments")
print("- Both: When you need maximum flexibility")

print("\nBest Practices:")
print("- Use descriptive parameter names")
print("- Document expected arguments")
print("- Handle empty arguments appropriately")
print("- Use .get() for safe dictionary access")
print("- Consider function signature clarity")

print("\nCommon Use Cases:")
print("- Wrapper functions")
print("- Configuration functions")
print("- Decorators")
print("- Function composition")
print("- Data processing functions") 