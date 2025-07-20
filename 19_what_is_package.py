"""
19. What is a package in Python?

A package in Python is a way to organize related modules into a single directory hierarchy.
Packages help organize code, avoid naming conflicts, and make code more maintainable.
"""

print("=== PACKAGES IN PYTHON ===\n")

# 1. BASIC PACKAGE STRUCTURE
print("1. BASIC PACKAGE STRUCTURE")
print("-" * 30)

# A package is a directory containing an __init__.py file
# Example structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#     __init__.py
#     module3.py

print("Package Structure:")
print("mypackage/")
print("  __init__.py          # Makes the directory a package")
print("  module1.py           # Module in the package")
print("  module2.py           # Another module")
print("  subpackage/          # Subpackage")
print("    __init__.py        # Makes subdirectory a package")
print("    module3.py         # Module in subpackage")

# 2. CREATING A PACKAGE
print("\n2. CREATING A PACKAGE")
print("-" * 30)

import os

# Create package structure
def create_package_structure():
    """Create a demo package structure."""
    
    # Create main package directory
    os.makedirs("demo_package", exist_ok=True)
    os.makedirs("demo_package/subpackage", exist_ok=True)
    
    # Create __init__.py files
    with open("demo_package/__init__.py", "w") as f:
        f.write('''"""
Demo Package

This is a demonstration package.
"""

__version__ = "1.0.0"
__author__ = "Demo Author"

# Import main functions for easier access
from .module1 import greet
from .module2 import calculate_area

# Package-level variables
PACKAGE_NAME = "demo_package"
''')
    
    # Create module1.py
    with open("demo_package/module1.py", "w") as f:
        f.write('''"""
Module 1: Greeting functions
"""

def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"

def greet_formal(name, title="Mr."):
    """Greet a person formally."""
    return f"Good day, {title} {name}!"

def greet_informal(name):
    """Greet a person informally."""
    return f"Hey {name}!"
''')
    
    # Create module2.py
    with open("demo_package/module2.py", "w") as f:
        f.write('''"""
Module 2: Calculation functions
"""

import math

def calculate_area(length, width):
    """Calculate area of rectangle."""
    return length * width

def calculate_circle_area(radius):
    """Calculate area of circle."""
    return math.pi * radius ** 2

def calculate_perimeter(length, width):
    """Calculate perimeter of rectangle."""
    return 2 * (length + width)
''')
    
    # Create subpackage __init__.py
    with open("demo_package/subpackage/__init__.py", "w") as f:
        f.write('''"""
Subpackage: Advanced utilities
"""

from .module3 import advanced_function
''')
    
    # Create module3.py in subpackage
    with open("demo_package/subpackage/module3.py", "w") as f:
        f.write('''"""
Module 3: Advanced functions
"""

def advanced_function(data):
    """Process data in an advanced way."""
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, dict):
        return sum(data.values())
    else:
        return data

def complex_calculation(x, y, operation="add"):
    """Perform complex calculations."""
    if operation == "add":
        return x + y
    elif operation == "multiply":
        return x * y
    elif operation == "power":
        return x ** y
    else:
        raise ValueError(f"Unknown operation: {operation}")
''')

# Create the package
create_package_structure()

# 3. IMPORTING FROM PACKAGES
print("\n3. IMPORTING FROM PACKAGES")
print("-" * 30)

# Import the entire package
import demo_package
print(f"Package version: {demo_package.__version__}")
print(f"Package name: {demo_package.PACKAGE_NAME}")

# Import specific modules from package
from demo_package import module1, module2
print(f"Greeting: {module1.greet('Alice')}")
print(f"Area: {module2.calculate_area(5, 3)}")

# Import specific functions
from demo_package.module1 import greet, greet_formal
from demo_package.module2 import calculate_circle_area

print(f"Greeting: {greet('Bob')}")
print(f"Formal greeting: {greet_formal('Charlie', 'Dr.')}")
print(f"Circle area: {calculate_circle_area(5):.2f}")

# Import from subpackage
from demo_package.subpackage import module3
print(f"Advanced function result: {module3.advanced_function([1, 2, 3, 4, 5])}")

# 4. PACKAGE INITIALIZATION
print("\n4. PACKAGE INITIALIZATION")
print("-" * 30)

# The __init__.py file can contain initialization code
# It runs when the package is imported

# Example of what can be in __init__.py:
init_example = '''
# Package initialization
print("Initializing demo_package...")

# Import commonly used functions
from .module1 import greet
from .module2 import calculate_area

# Define package-level variables
__version__ = "1.0.0"
__author__ = "Demo Author"

# Package-level functions
def get_package_info():
    return {
        "name": "demo_package",
        "version": __version__,
        "author": __author__
    }

print("demo_package initialized successfully!")
'''

print("__init__.py can contain:")
print("- Package initialization code")
print("- Import statements")
print("- Package-level variables")
print("- Package-level functions")
print("- Version information")

# 5. RELATIVE IMPORTS
print("\n5. RELATIVE IMPORTS")
print("-" * 30)

# Relative imports are used within packages
# Example of relative imports in module1.py:
relative_import_example = '''
# In module1.py
from . import module2  # Import sibling module
from .module2 import calculate_area  # Import from sibling module
from .. import other_package  # Import from parent package
from .subpackage import module3  # Import from subpackage
'''

print("Relative Import Syntax:")
print("- from . import module_name")
print("- from .module_name import function_name")
print("- from .. import parent_module")
print("- from .subpackage import module_name")

# 6. PACKAGE HIERARCHY
print("\n6. PACKAGE HIERARCHY")
print("-" * 30)

# Complex package structure
complex_structure = '''
mypackage/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── database.py
│   └── utils.py
├── web/
│   ├── __init__.py
│   ├── views.py
│   └── models.py
├── api/
│   ├── __init__.py
│   ├── endpoints.py
│   └── authentication.py
└── tests/
    ├── __init__.py
    ├── test_core.py
    └── test_web.py
'''

print("Complex Package Structure:")
print(complex_structure)

# 7. PACKAGE NAMESPACE
print("\n7. PACKAGE NAMESPACE")
print("-" * 30)

# Packages create namespaces
import demo_package.module1 as m1
import demo_package.module2 as m2

print(f"Module1 greeting: {m1.greet('Alice')}")
print(f"Module2 area: {m2.calculate_area(4, 6)}")

# Access package attributes
print(f"Package version: {demo_package.__version__}")
print(f"Package author: {demo_package.__author__}")

# 8. PACKAGE DISTRIBUTION
print("\n8. PACKAGE DISTRIBUTION")
print("-" * 30)

# setup.py for package distribution
setup_py_example = '''
from setuptools import setup, find_packages

setup(
    name="demo_package",
    version="1.0.0",
    author="Demo Author",
    author_email="demo@example.com",
    description="A demonstration package",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.20.0",
    ],
    python_requires=">=3.7",
)
'''

print("Package Distribution:")
print("- Use setup.py for package distribution")
print("- Use find_packages() to automatically find packages")
print("- Specify dependencies in install_requires")
print("- Use python_requires to specify Python version")

# 9. PACKAGE METADATA
print("\n9. PACKAGE METADATA")
print("-" * 30)

# Package metadata in __init__.py
metadata_example = '''
"""
Demo Package

A demonstration package showing package structure and usage.
"""

__version__ = "1.0.0"
__author__ = "Demo Author"
__email__ = "demo@example.com"
__description__ = "A demonstration package"
__url__ = "https://github.com/demo/demo_package"
__license__ = "MIT"

# Import main functions
from .module1 import greet
from .module2 import calculate_area

# Package-level configuration
DEFAULT_GREETING = "Hello"
DEFAULT_CALCULATION_PRECISION = 2
'''

print("Package Metadata:")
print("- __version__: Package version")
print("- __author__: Package author")
print("- __description__: Package description")
print("- __url__: Package URL")
print("- __license__: Package license")

# 10. PACKAGE PATTERNS
print("\n10. PACKAGE PATTERNS")
print("-" * 30)

# Pattern 1: Simple package
simple_package = '''
simple_package/
├── __init__.py
├── utils.py
└── helpers.py
'''

# Pattern 2: Feature-based package
feature_package = '''
feature_package/
├── __init__.py
├── database/
│   ├── __init__.py
│   ├── models.py
│   └── connection.py
├── web/
│   ├── __init__.py
│   ├── views.py
│   └── templates.py
└── utils/
    ├── __init__.py
    ├── helpers.py
    └── validators.py
'''

# Pattern 3: Layer-based package
layer_package = '''
layer_package/
├── __init__.py
├── presentation/
│   ├── __init__.py
│   └── views.py
├── business/
│   ├── __init__.py
│   └── services.py
└── data/
    ├── __init__.py
    └── repositories.py
'''

print("Common Package Patterns:")
print("1. Simple package: Basic organization")
print("2. Feature-based: Organize by features")
print("3. Layer-based: Organize by architectural layers")

# 11. PACKAGE BEST PRACTICES
print("\n11. PACKAGE BEST PRACTICES")
print("-" * 30)

print("Package Best Practices:")
print("1. Use descriptive package names")
print("2. Include __init__.py in every package directory")
print("3. Use relative imports within packages")
print("4. Keep packages focused and cohesive")
print("5. Document package purpose and usage")
print("6. Use version numbers in __init__.py")
print("7. Provide clear import interfaces")
print("8. Handle package dependencies properly")

# 12. PACKAGE TESTING
print("\n12. PACKAGE TESTING")
print("-" * 30)

# Test package structure
test_structure = '''
test_package/
├── __init__.py
├── module1.py
├── module2.py
└── tests/
    ├── __init__.py
    ├── test_module1.py
    └── test_module2.py
'''

print("Package Testing:")
print("- Include tests directory in package")
print("- Use unittest or pytest for testing")
print("- Test each module independently")
print("- Test package-level functionality")
print("- Use relative imports in tests")

# 13. PACKAGE DOCUMENTATION
print("\n13. PACKAGE DOCUMENTATION")
print("-" * 30)

# Package documentation
package_docs = '''
# Demo Package

A demonstration package showing Python package structure and usage.

## Installation

```bash
pip install demo-package
```

## Usage

```python
from demo_package import greet, calculate_area

# Use the functions
greeting = greet("Alice")
area = calculate_area(5, 3)
```

## API Reference

### Functions

- `greet(name)`: Greet a person
- `calculate_area(length, width)`: Calculate rectangle area

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request
'''

print("Package Documentation:")
print("- README.md for package overview")
print("- Docstrings in __init__.py")
print("- API documentation")
print("- Installation instructions")
print("- Usage examples")

# 14. CLEANUP
print("\n14. CLEANUP")
print("-" * 30)

# Clean up the demo package
import shutil
if os.path.exists("demo_package"):
    shutil.rmtree("demo_package")
    print("Demo package cleaned up")

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What is a Package?")
print("- A directory containing an __init__.py file")
print("- A way to organize related modules")
print("- A namespace for Python modules")
print("- A unit of distribution")

print("\nPackage Benefits:")
print("- Organize code logically")
print("- Avoid naming conflicts")
print("- Make code more maintainable")
print("- Enable code distribution")
print("- Provide clear import interfaces")

print("\nPackage Components:")
print("- __init__.py: Makes directory a package")
print("- Modules: Python files with code")
print("- Subpackages: Nested package directories")
print("- Metadata: Version, author, description")

print("\nPackage Usage:")
print("- Import entire package: import package_name")
print("- Import specific modules: from package import module")
print("- Import specific functions: from package.module import function")
print("- Use relative imports within packages")

print("\nBest Practices:")
print("- Use descriptive package names")
print("- Include __init__.py files")
print("- Use relative imports within packages")
print("- Document package purpose")
print("- Provide clear import interfaces")
print("- Handle dependencies properly")
print("- Include tests and documentation") 