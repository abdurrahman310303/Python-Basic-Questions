"""
27. How do you use variable scope in Python?

Variable scope in Python determines where a variable can be accessed and modified.
Python has different scopes: local, enclosing (nonlocal), global, and built-in.
Understanding scope is crucial for writing clean, maintainable code.
"""

print("=== VARIABLE SCOPE IN PYTHON ===\n")

# 1. BASIC SCOPE CONCEPTS
print("1. BASIC SCOPE CONCEPTS")
print("-" * 30)

# Global variable
global_var = "I'm a global variable"

def demonstrate_scope():
    """Demonstrate different scopes."""
    local_var = "I'm a local variable"
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")

# Accessing variables
print(f"Outside function - global_var: {global_var}")
demonstrate_scope()

# 2. LOCAL SCOPE
print("\n2. LOCAL SCOPE")
print("-" * 30)

def local_scope_example():
    """Demonstrate local scope."""
    x = 10  # Local variable
    print(f"Inside function, x = {x}")
    
    def nested_function():
        y = 20  # Local to nested function
        print(f"Inside nested function, y = {y}")
        print(f"Inside nested function, x = {x}")  # Can access outer x
    
    nested_function()
    # print(f"Outside nested function, y = {y}")  # This would cause an error

local_scope_example()

# 3. GLOBAL SCOPE
print("\n3. GLOBAL SCOPE")
print("-" * 30)

# Global variable
counter = 0

def increment_counter():
    """Increment the global counter."""
    global counter  # Declare that we want to use the global variable
    counter += 1
    print(f"Counter incremented to: {counter}")

def read_global():
    """Read the global variable without modifying it."""
    print(f"Current counter value: {counter}")

# Using global variables
print(f"Initial counter: {counter}")
increment_counter()
increment_counter()
read_global()

# 4. NONLOCAL SCOPE
print("\n4. NONLOCAL SCOPE")
print("-" * 30)

def outer_function():
    """Demonstrate nonlocal scope."""
    x = 10  # Enclosing scope variable
    
    def inner_function():
        nonlocal x  # Declare that we want to use the enclosing variable
        x = 20  # Modify the enclosing variable
        print(f"Inner function, x = {x}")
    
    print(f"Before inner function, x = {x}")
    inner_function()
    print(f"After inner function, x = {x}")

outer_function()

# 5. BUILT-IN SCOPE
print("\n5. BUILT-IN SCOPE")
print("-" * 30)

# Built-in functions are always available
print(f"Built-in len function: {len}")
print(f"Built-in print function: {print}")

def demonstrate_builtin_scope():
    """Demonstrate built-in scope."""
    # We can use built-in functions without importing
    my_list = [1, 2, 3, 4, 5]
    print(f"Length of list: {len(my_list)}")
    print(f"Sum of list: {sum(my_list)}")
    print(f"Maximum value: {max(my_list)}")

demonstrate_builtin_scope()

# 6. SCOPE RULES (LEGB)
print("\n6. SCOPE RULES (LEGB)")
print("-" * 30)

# LEGB: Local, Enclosing, Global, Built-in

# Built-in scope (always available)
print("Built-in scope example:")
print(f"len function: {len}")

# Global scope
global_var = "Global variable"

def scope_demo():
    """Demonstrate LEGB scope rules."""
    # Local scope
    local_var = "Local variable"
    
    def nested_function():
        # Enclosing scope
        enclosing_var = "Enclosing variable"
        
        def inner_function():
            # Local scope
            inner_var = "Inner variable"
            print(f"Inner function can access:")
            print(f"  Local: {inner_var}")
            print(f"  Enclosing: {enclosing_var}")
            print(f"  Global: {global_var}")
            print(f"  Built-in: {len}")
        
        inner_function()
    
    nested_function()

scope_demo()

# 7. VARIABLE SHADOWING
print("\n7. VARIABLE SHADOWING")
print("-" * 30)

# Global variable
x = 100

def shadowing_example():
    """Demonstrate variable shadowing."""
    x = 200  # This shadows the global x
    print(f"Local x: {x}")
    
    def nested_function():
        x = 300  # This shadows the enclosing x
        print(f"Nested x: {x}")
    
    nested_function()
    print(f"After nested function, local x: {x}")

print(f"Global x: {x}")
shadowing_example()
print(f"After function, global x: {x}")

# 8. GLOBAL STATEMENT
print("\n8. GLOBAL STATEMENT")
print("-" * 30)

# Global variable
total = 0

def add_to_total(value):
    """Add value to global total."""
    global total  # Must declare global to modify
    total += value
    print(f"Added {value}, total is now {total}")

def get_total():
    """Get the global total."""
    return total  # Can read global without declaring

print(f"Initial total: {get_total()}")
add_to_total(10)
add_to_total(20)
print(f"Final total: {get_total()}")

# 9. NONLOCAL STATEMENT
print("\n9. NONLOCAL STATEMENT")
print("-" * 30)

def create_counter():
    """Create a counter function using nonlocal."""
    count = 0  # Enclosing scope variable
    
    def increment():
        nonlocal count  # Must declare nonlocal to modify
        count += 1
        return count
    
    def get_count():
        return count  # Can read without declaring nonlocal
    
    return increment, get_count

# Using the counter
increment_func, get_count_func = create_counter()
print(f"Initial count: {get_count_func()}")
print(f"After increment: {increment_func()}")
print(f"After another increment: {increment_func()}")
print(f"Final count: {get_count_func()}")

# 10. SCOPE IN CLASSES
print("\n10. SCOPE IN CLASSES")
print("-" * 30)

class ScopeExample:
    """Demonstrate scope in classes."""
    
    class_var = "Class variable"  # Class-level variable
    
    def __init__(self):
        self.instance_var = "Instance variable"  # Instance variable
    
    def method(self):
        local_var = "Local variable"  # Local variable
        print(f"Class variable: {self.class_var}")
        print(f"Instance variable: {self.instance_var}")
        print(f"Local variable: {local_var}")

# Using the class
obj = ScopeExample()
obj.method()

# 11. SCOPE IN MODULES
print("\n11. SCOPE IN MODULES")
print("-" * 30)

# Module-level variables
module_var = "Module variable"

def module_function():
    """Function in module scope."""
    print(f"Module function can access: {module_var}")

# Importing and using module scope
module_function()

# 12. SCOPE BEST PRACTICES
print("\n12. SCOPE BEST PRACTICES")
print("-" * 30)

print("Scope Best Practices:")
print("1. Minimize use of global variables")
print("2. Use function parameters instead of global variables")
print("3. Use nonlocal for nested functions when needed")
print("4. Keep variable names descriptive")
print("5. Avoid variable shadowing when possible")
print("6. Use classes to encapsulate related data")

# Good practice: Use parameters instead of globals
def good_practice_example(data):
    """Good practice: Use parameters instead of globals."""
    result = data * 2
    return result

# Bad practice: Using globals
bad_global = 0

def bad_practice_example():
    """Bad practice: Using global variables."""
    global bad_global
    bad_global += 1
    return bad_global

# 13. SCOPE DEBUGGING
print("\n13. SCOPE DEBUGGING")
print("-" * 30)

def debug_scope():
    """Demonstrate scope debugging."""
    x = 10
    
    def inner_function():
        # This would cause an error if we tried to access x before defining it
        # print(x)  # UnboundLocalError
        x = 20  # This creates a local variable
        print(f"Local x: {x}")
    
    inner_function()
    print(f"Outer x: {x}")

debug_scope()

# 14. SCOPE PATTERNS
print("\n14. SCOPE PATTERNS")
print("-" * 30)

# Pattern 1: Factory functions
def create_multiplier(factor):
    """Create a function that multiplies by the given factor."""
    def multiply(x):
        return x * factor
    return multiply

# Using the factory function
double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double of 5: {double(5)}")
print(f"Triple of 5: {triple(5)}")

# Pattern 2: Closure with state
def create_counter():
    """Create a counter with state."""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    return increment, decrement, get_count

# Using the counter
inc, dec, get = create_counter()
print(f"Initial count: {get()}")
print(f"After increment: {inc()}")
print(f"After increment: {inc()}")
print(f"After decrement: {dec()}")
print(f"Final count: {get()}")

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What is Variable Scope?")
print("- Determines where variables can be accessed")
print("- Controls variable lifetime and visibility")
print("- Prevents naming conflicts")
print("- Enables encapsulation")

print("\nScope Types (LEGB):")
print("- Local: Variables defined inside a function")
print("- Enclosing: Variables in outer functions")
print("- Global: Variables at module level")
print("- Built-in: Python's built-in names")

print("\nScope Keywords:")
print("- global: Access/modify global variables")
print("- nonlocal: Access/modify enclosing variables")
print("- No keyword needed for local variables")

print("\nScope Rules:")
print("- Inner scopes can read outer variables")
print("- Outer scopes cannot read inner variables")
print("- Local variables shadow outer variables")
print("- global/nonlocal required to modify outer variables")

print("\nBest Practices:")
print("- Minimize global variable usage")
print("- Use function parameters")
print("- Use classes for related data")
print("- Keep variable names descriptive")
print("- Avoid variable shadowing")
print("- Use nonlocal for nested functions")

print("\nCommon Patterns:")
print("- Factory functions")
print("- Closures with state")
print("- Module-level configuration")
print("- Class encapsulation")
print("- Function decorators")

print("\nDebugging Tips:")
print("- Use print statements to trace variable values")
print("- Check variable names for typos")
print("- Verify global/nonlocal declarations")
print("- Use IDEs with scope highlighting")
print("- Test functions in isolation") 