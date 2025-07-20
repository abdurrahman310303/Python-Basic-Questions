"""
18. How do you import a module in Python?

Importing modules in Python allows you to use code from other files or libraries.
Python provides several ways to import modules and their contents.
"""

print("=== IMPORTING MODULES IN PYTHON ===\n")

# 1. BASIC IMPORT STATEMENTS
print("1. BASIC IMPORT STATEMENTS")
print("-" * 30)

# Import entire module
import math
print(f"Pi value: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# Import specific functions/classes
from math import sqrt, pi
print(f"Pi: {pi}")
print(f"Square root of 25: {sqrt(25)}")

# Import with alias
import datetime as dt
print(f"Current time: {dt.datetime.now()}")

# Import specific items with alias
from math import sqrt as square_root
print(f"Square root of 9: {square_root(9)}")

# 2. DIFFERENT IMPORT METHODS
print("\n2. DIFFERENT IMPORT METHODS")
print("-" * 30)

# Method 1: Import entire module
import os
print(f"Current directory: {os.getcwd()}")

# Method 2: Import specific items
from random import randint, choice
print(f"Random number: {randint(1, 10)}")
print(f"Random choice: {choice(['apple', 'banana', 'orange'])}")

# Method 3: Import all (not recommended)
# from math import *  # Avoid this in production code

# Method 4: Import with alias
import json as js
data = {"name": "John", "age": 30}
json_string = js.dumps(data)
print(f"JSON string: {json_string}")

# 3. IMPORTING FROM PACKAGES
print("\n3. IMPORTING FROM PACKAGES")
print("-" * 30)

# Import from standard library packages
import urllib.request
import urllib.parse

# Import specific functions from packages
from urllib.request import urlopen
from urllib.parse import urlparse

# Import from nested packages
import os.path
print(f"File exists: {os.path.exists('nonexistent.txt')}")

# 4. RELATIVE IMPORTS
print("\n4. RELATIVE IMPORTS")
print("-" * 30)

# Relative imports (used within packages)
# from . import module_name
# from .. import module_name
# from .module_name import function_name

# Example structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#     __init__.py
#     module3.py

# In module1.py:
# from . import module2
# from .module2 import function_name
# from .subpackage import module3

# 5. IMPORTING CUSTOM MODULES
print("\n5. IMPORTING CUSTOM MODULES")
print("-" * 30)

# Creating a simple module for demonstration
def create_demo_module():
    """Create a demo module file."""
    module_content = '''
def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate area of rectangle."""
    return length * width

PI = 3.14159
'''
    
    with open("demo_module.py", "w") as f:
        f.write(module_content)

# Create the demo module
create_demo_module()

# Import the custom module
import demo_module
print(f"Greeting: {demo_module.greet('Alice')}")
print(f"Area: {demo_module.calculate_area(5, 3)}")
print(f"PI: {demo_module.PI}")

# Import specific items from custom module
from demo_module import greet, calculate_area
print(f"Greeting: {greet('Bob')}")
print(f"Area: {calculate_area(4, 6)}")

# Clean up
import os
if os.path.exists("demo_module.py"):
    os.remove("demo_module.py")

# 6. IMPORTING WITH CONDITIONS
print("\n6. IMPORTING WITH CONDITIONS")
print("-" * 30)

# Conditional imports
try:
    import numpy as np
    print("NumPy is available")
    print(f"NumPy version: {np.__version__}")
except ImportError:
    print("NumPy is not available")

# Import with fallback
try:
    from PIL import Image
    print("Pillow is available")
except ImportError:
    print("Pillow is not available, using alternative")

# 7. IMPORTING FROM DIFFERENT LOCATIONS
print("\n7. IMPORTING FROM DIFFERENT LOCATIONS")
print("-" * 30)

import sys

# Add custom path to sys.path
sys.path.append('/custom/path')

# Import from specific path
# import sys
# sys.path.insert(0, '/path/to/modules')
# import my_module

# 8. IMPORTING BUILT-IN MODULES
print("\n8. IMPORTING BUILT-IN MODULES")
print("-" * 30)

# Common built-in modules
import os
import sys
import math
import random
import datetime
import json
import re
import collections

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Current working directory: {os.getcwd()}")

# 9. IMPORTING THIRD-PARTY MODULES
print("\n9. IMPORTING THIRD-PARTY MODULES")
print("-" * 30)

# Example of third-party module import (if available)
try:
    import requests
    print("Requests library is available")
    # response = requests.get('https://api.github.com')
    # print(f"Status code: {response.status_code}")
except ImportError:
    print("Requests library is not available")

# 10. IMPORTING CLASSES AND FUNCTIONS
print("\n10. IMPORTING CLASSES AND FUNCTIONS")
print("-" * 30)

# Import specific classes
from datetime import datetime, timedelta
from collections import Counter, defaultdict

# Using imported classes
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f"Now: {now}")
print(f"Tomorrow: {tomorrow}")

# Using Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word count: {word_count}")

# 11. IMPORTING WITH __ALL__
print("\n11. IMPORTING WITH __ALL__")
print("-" * 30)

# Creating a module with __all__ defined
def create_module_with_all():
    """Create a module with __all__ defined."""
    module_content = '''
__all__ = ['greet', 'calculate_area', 'PI']

def greet(name):
    return f"Hello, {name}!"

def calculate_area(length, width):
    return length * width

def _private_function():
    return "This is private"

PI = 3.14159
SECRET = "secret"
'''
    
    with open("module_with_all.py", "w") as f:
        f.write(module_content)

# Create the module
create_module_with_all()

# Import from module with __all__
from module_with_all import *
print(f"Greeting: {greet('Alice')}")
print(f"Area: {calculate_area(5, 3)}")
print(f"PI: {PI}")

# Clean up
if os.path.exists("module_with_all.py"):
    os.remove("module_with_all.py")

# 12. IMPORTING WITH INITIALIZATION
print("\n12. IMPORTING WITH INITIALIZATION")
print("-" * 30)

# Creating a module with initialization
def create_init_module():
    """Create a module with initialization code."""
    module_content = '''
print("Module is being imported!")

def greet(name):
    return f"Hello, {name}!"

# This runs when module is imported
print("Module initialization complete")
'''
    
    with open("init_module.py", "w") as f:
        f.write(module_content)

# Create the module
create_init_module()

# Import the module (will run initialization)
import init_module
print(f"Greeting: {init_module.greet('Bob')}")

# Clean up
if os.path.exists("init_module.py"):
    os.remove("init_module.py")

# 13. IMPORTING BEST PRACTICES
print("\n13. IMPORTING BEST PRACTICES")
print("-" * 30)

# Good: Import at the top of the file
import os
import sys
import math
from datetime import datetime

# Good: Use specific imports
from math import sqrt, pi
from datetime import datetime, timedelta

# Good: Use aliases for clarity
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Good: Group imports
# Standard library imports
import os
import sys
import math

# Third-party imports
import requests
import numpy as np

# Local imports
# from . import my_module

# 14. COMMON IMPORT PATTERNS
print("\n14. COMMON IMPORT PATTERNS")
print("-" * 30)

# Pattern 1: Lazy imports
def lazy_import_example():
    """Import only when needed."""
    try:
        import heavy_module
        return heavy_module.do_something()
    except ImportError:
        return "Heavy module not available"

# Pattern 2: Import with error handling
def safe_import(module_name):
    """Safely import a module."""
    try:
        module = __import__(module_name)
        return module
    except ImportError:
        print(f"Module {module_name} not found")
        return None

# Pattern 3: Dynamic imports
def dynamic_import(module_name, function_name):
    """Dynamically import a function."""
    try:
        module = __import__(module_name)
        function = getattr(module, function_name)
        return function
    except (ImportError, AttributeError):
        return None

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("Import Methods:")
print("1. import module_name")
print("2. from module_name import item")
print("3. from module_name import item as alias")
print("4. import module_name as alias")
print("5. from module_name import * (avoid in production)")

print("\nImport Locations:")
print("- Built-in modules (os, sys, math, etc.)")
print("- Standard library modules")
print("- Third-party modules (installed via pip)")
print("- Custom modules (your own code)")
print("- Relative imports (within packages)")

print("\nBest Practices:")
print("- Import at the top of the file")
print("- Use specific imports when possible")
print("- Use aliases for clarity")
print("- Group imports logically")
print("- Handle import errors gracefully")
print("- Avoid 'from module import *'")
print("- Use relative imports within packages")

print("\nCommon Import Errors:")
print("- ModuleNotFoundError: Module not found")
print("- ImportError: Import failed")
print("- AttributeError: Item not found in module")
print("- SyntaxError: Invalid import syntax")

print("\nImport Tips:")
print("- Use virtual environments for project isolation")
print("- Check module availability before importing")
print("- Use __all__ to control what gets imported with *")
print("- Use __init__.py files to make directories into packages")
print("- Use relative imports within packages")
print("- Use absolute imports for external modules") 