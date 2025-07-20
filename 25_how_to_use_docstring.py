"""
25. How do you use docstrings in Python?

Docstrings in Python are string literals that appear as the first statement in a
module, function, class, or method definition. They provide documentation for
Python objects and are accessible through the __doc__ attribute.
"""

print("=== DOCSTRINGS IN PYTHON ===\n")

# 1. BASIC DOCSTRING SYNTAX
print("1. BASIC DOCSTRING SYNTAX")
print("-" * 30)

# Docstring syntax: triple quotes immediately after definition
def simple_function():
    """This is a simple docstring."""
    return "Hello, World!"

# Accessing docstring
print(f"Function docstring: {simple_function.__doc__}")

# Function with parameters
def greet(name, greeting="Hello"):
    """Greet a person with a custom message.
    
    Args:
        name (str): The name of the person to greet
        greeting (str): The greeting message (default: "Hello")
    
    Returns:
        str: The formatted greeting message
    """
    return f"{greeting}, {name}!"

print(f"Greet function docstring: {greet.__doc__}")

# 2. DIFFERENT DOCSTRING STYLES
print("\n2. DIFFERENT DOCSTRING STYLES")
print("-" * 30)

# Google style docstring
def google_style_function(param1, param2):
    """Short description of the function.
    
    Longer description of the function if needed.
    
    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: Description of when this error occurs
    """
    return True

# NumPy style docstring
def numpy_style_function(param1, param2):
    """Short description of the function.
    
    Longer description of the function if needed.
    
    Parameters
    ----------
    param1 : int
        Description of param1
    param2 : str
        Description of param2
    
    Returns
    -------
    bool
        Description of return value
    
    Raises
    ------
    ValueError
        Description of when this error occurs
    """
    return True

# Sphinx style docstring
def sphinx_style_function(param1, param2):
    """Short description of the function.
    
    Longer description of the function if needed.
    
    :param param1: Description of param1
    :type param1: int
    :param param2: Description of param2
    :type param2: str
    :returns: Description of return value
    :rtype: bool
    :raises ValueError: Description of when this error occurs
    """
    return True

# 3. CLASS DOCSTRINGS
print("\n3. CLASS DOCSTRINGS")
print("-" * 30)

class Calculator:
    """A simple calculator class.
    
    This class provides basic arithmetic operations.
    
    Attributes:
        name (str): The name of the calculator
        history (list): List of previous calculations
    """
    
    def __init__(self, name="Calculator"):
        """Initialize the calculator.
        
        Args:
            name (str): The name of the calculator
        """
        self.name = name
        self.history = []
    
    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
        
        Returns:
            int/float: Sum of the two numbers
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history.
        
        Returns:
            list: List of previous calculations
        """
        return self.history

# Accessing class docstring
print(f"Class docstring: {Calculator.__doc__}")

# Accessing method docstring
calc = Calculator()
print(f"Add method docstring: {calc.add.__doc__}")

# 4. MODULE DOCSTRINGS
print("\n4. MODULE DOCSTRINGS")
print("-" * 30)

# This is a module-level docstring
"""
This module demonstrates various aspects of docstrings in Python.

This module contains examples of:
- Function docstrings
- Class docstrings
- Module docstrings
- Different docstring styles

Author: Python Developer
Version: 1.0.0
"""

# Accessing module docstring
print(f"Module docstring: {__doc__}")

# 5. MULTI-LINE DOCSTRINGS
print("\n5. MULTI-LINE DOCSTRINGS")
print("-" * 30)

def complex_function(param1, param2, param3=None):
    """Perform a complex operation with multiple parameters.
    
    This function demonstrates a multi-line docstring with detailed
    information about parameters, return values, and examples.
    
    Args:
        param1 (int): The first parameter. Must be a positive integer.
        param2 (str): The second parameter. Should be a valid string.
        param3 (list, optional): The third parameter. Defaults to None.
    
    Returns:
        dict: A dictionary containing the results of the operation.
            Keys:
                - 'result': The main result
                - 'status': Success or failure status
                - 'message': Additional information
    
    Raises:
        ValueError: If param1 is not positive
        TypeError: If param2 is not a string
    
    Example:
        >>> result = complex_function(5, "test")
        >>> print(result['result'])
        25
    """
    if param1 <= 0:
        raise ValueError("param1 must be positive")
    
    if not isinstance(param2, str):
        raise TypeError("param2 must be a string")
    
    result = param1 ** 2
    return {
        'result': result,
        'status': 'success',
        'message': f'Processed {param2}'
    }

# 6. DOCSTRING ACCESS METHODS
print("\n6. DOCSTRING ACCESS METHODS")
print("-" * 30)

# Method 1: Using __doc__ attribute
print(f"Function docstring via __doc__: {complex_function.__doc__}")

# Method 2: Using help() function
# help(complex_function)  # This would print the help

# Method 3: Using inspect module
import inspect
doc = inspect.getdoc(complex_function)
print(f"Function docstring via inspect: {doc}")

# Method 4: Using pydoc
import pydoc
# pydoc.help(complex_function)  # This would show formatted help

# 7. DOCSTRING FORMATTING
print("\n7. DOCSTRING FORMATTING")
print("-" * 30)

def formatted_function():
    """This is a well-formatted docstring.
    
    The first line should be a brief summary of the function's purpose.
    It should fit on one line and be separated from the rest of the
    docstring by a blank line.
    
    The rest of the docstring should provide detailed information about
    the function's behavior, parameters, return values, and examples.
    
    Returns:
        str: A simple message
    """
    return "Formatted function"

# 8. DOCSTRING WITH EXAMPLES
print("\n8. DOCSTRING WITH EXAMPLES")
print("-" * 30)

def example_function(x, y):
    """Add two numbers and return the result.
    
    This function demonstrates how to include examples in docstrings.
    
    Args:
        x (int): First number
        y (int): Second number
    
    Returns:
        int: Sum of x and y
    
    Examples:
        Basic usage:
            >>> example_function(2, 3)
            5
        
        With negative numbers:
            >>> example_function(-1, 5)
            4
        
        With zero:
            >>> example_function(0, 10)
            10
    """
    return x + y

# 9. DOCSTRING WITH TYPE HINTS
print("\n9. DOCSTRING WITH TYPE HINTS")
print("-" * 30)

def typed_function(name: str, age: int, scores: list[float]) -> dict[str, any]:
    """Process student information with type hints.
    
    This function demonstrates how to combine type hints with docstrings.
    
    Args:
        name: Student's name
        age: Student's age
        scores: List of student's scores
    
    Returns:
        Dictionary containing processed student information
    
    Note:
        Type hints are separate from docstrings but complement them well.
    """
    average = sum(scores) / len(scores) if scores else 0
    return {
        'name': name,
        'age': age,
        'average_score': average,
        'grade': 'A' if average >= 90 else 'B' if average >= 80 else 'C'
    }

# 10. DOCSTRING BEST PRACTICES
print("\n10. DOCSTRING BEST PRACTICES")
print("-" * 30)

print("Docstring Best Practices:")
print("1. Write docstrings for all public modules, functions, classes, and methods")
print("2. Use clear, concise language")
print("3. Follow a consistent style (Google, NumPy, Sphinx)")
print("4. Include parameter types and descriptions")
print("5. Document return values and exceptions")
print("6. Provide examples for complex functions")
print("7. Keep the first line brief and descriptive")
print("8. Use proper grammar and punctuation")

# Good docstring example
def good_docstring_example(param1: int, param2: str) -> bool:
    """Validate user input parameters.
    
    This function checks if the provided parameters meet the required
    criteria for processing.
    
    Args:
        param1: Numeric value to validate
        param2: String value to validate
    
    Returns:
        True if parameters are valid, False otherwise
    
    Raises:
        TypeError: If param1 is not an integer
        ValueError: If param2 is empty
    
    Example:
        >>> good_docstring_example(5, "valid")
        True
        >>> good_docstring_example(-1, "")
        False
    """
    if not isinstance(param1, int):
        raise TypeError("param1 must be an integer")
    
    if not param2:
        raise ValueError("param2 cannot be empty")
    
    return param1 > 0 and len(param2) > 3

# 11. DOCSTRING TOOLS
print("\n11. DOCSTRING TOOLS")
print("-" * 30)

# Using doctest for testing docstring examples
import doctest

def doctest_function(a, b):
    """Add two numbers.
    
    >>> doctest_function(2, 3)
    5
    >>> doctest_function(-1, 1)
    0
    >>> doctest_function(0, 0)
    0
    """
    return a + b

# Running doctest
# doctest.testmod()  # This would run all doctests in the module

# Using pydoc for documentation generation
# pydoc.writedoc('module_name')  # This would generate HTML documentation

# 12. DOCSTRING TEMPLATES
print("\n12. DOCSTRING TEMPLATES")
print("-" * 30)

# Function template
def function_template(param1, param2):
    """Brief description of what the function does.
    
    Longer description if needed, explaining the function's purpose,
    behavior, and any important details.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
    
    Returns:
        type: Description of return value
    
    Raises:
        ExceptionType: Description of when this exception occurs
    
    Example:
        >>> function_template(1, "test")
        expected_output
    """
    pass

# Class template
class ClassTemplate:
    """Brief description of the class.
    
    Longer description of the class if needed.
    
    Attributes:
        attr1 (type): Description of attr1
        attr2 (type): Description of attr2
    """
    
    def __init__(self, param1):
        """Initialize the class.
        
        Args:
            param1 (type): Description of param1
        """
        self.attr1 = param1
    
    def method_template(self, param1):
        """Brief description of the method.
        
        Args:
            param1 (type): Description of param1
        
        Returns:
            type: Description of return value
        """
        pass

# 13. DOCSTRING VALIDATION
print("\n13. DOCSTRING VALIDATION")
print("-" * 30)

# Using tools to validate docstrings
def validate_docstring_function(param1: int, param2: str) -> bool:
    """Validate parameters and return result.
    
    This function demonstrates proper docstring structure that can be
    validated by documentation tools.
    
    Args:
        param1: Integer parameter to validate
        param2: String parameter to validate
    
    Returns:
        True if validation passes, False otherwise
    
    Raises:
        ValueError: If param1 is negative
        TypeError: If param2 is not a string
    """
    if param1 < 0:
        raise ValueError("param1 must be non-negative")
    
    if not isinstance(param2, str):
        raise TypeError("param2 must be a string")
    
    return param1 > 0 and len(param2) > 0

# 14. DOCSTRING GENERATION
print("\n14. DOCSTRING GENERATION")
print("-" * 30)

# Auto-generating docstrings (conceptual)
def auto_docstring_function(name: str, age: int) -> str:
    """Auto-generated docstring for demonstration.
    
    This docstring could be generated automatically by tools like
    IDEs or documentation generators.
    
    Args:
        name: The name parameter
        age: The age parameter
    
    Returns:
        A formatted string
    """
    return f"{name} is {age} years old"

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What are Docstrings?")
print("- String literals that document Python objects")
print("- Accessible via __doc__ attribute")
print("- Used by help() and documentation tools")
print("- Support multiple formatting styles")

print("\nDocstring Locations:")
print("- Module level (first statement)")
print("- Function definitions")
print("- Class definitions")
print("- Method definitions")

print("\nDocstring Styles:")
print("- Google style")
print("- NumPy style")
print("- Sphinx style")
print("- Plain text")

print("\nDocstring Components:")
print("- Brief description (first line)")
print("- Detailed description")
print("- Parameters/Arguments")
print("- Return values")
print("- Exceptions/Raises")
print("- Examples")

print("\nBest Practices:")
print("- Write docstrings for all public objects")
print("- Use clear, concise language")
print("- Follow consistent style")
print("- Include type information")
print("- Provide examples")
print("- Keep first line brief")
print("- Use proper grammar")

print("\nTools and Utilities:")
print("- help() function")
print("- inspect module")
print("- pydoc module")
print("- doctest module")
print("- Documentation generators")
print("- IDE support")

print("\nCommon Use Cases:")
print("- API documentation")
print("- Code documentation")
print("- Testing with doctest")
print("- IDE intellisense")
print("- Documentation websites")
print("- Code reviews") 