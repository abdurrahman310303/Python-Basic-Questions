"""
20. What is a script in Python?

A script in Python is a file containing Python code that can be executed directly.
Scripts are typically used for automation, data processing, and standalone programs.
"""

print("=== SCRIPTS IN PYTHON ===\n")

# 1. BASIC SCRIPT STRUCTURE
print("1. BASIC SCRIPT STRUCTURE")
print("-" * 30)

# A script is a Python file that can be run directly
# Example: hello_world.py
print("Hello, World!")
print("This is a simple Python script")

# Scripts can contain functions, classes, and executable code
def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"

# Executable code at module level
name = "Alice"
greeting = greet(name)
print(greeting)

# 2. SCRIPT VS MODULE
print("\n2. SCRIPT VS MODULE")
print("-" * 30)

# Script: Designed to be run directly
# Module: Designed to be imported

# Script example (this file)
print("This file can be run as a script")
print("python script_name.py")

# Module example
def utility_function():
    """This function is designed to be imported."""
    return "I'm a utility function"

# Check if this file is being run directly
if __name__ == "__main__":
    print("This script is being run directly")
    print("This code only runs when the file is executed as a script")
else:
    print("This module is being imported")

# 3. SCRIPT EXECUTION
print("\n3. SCRIPT EXECUTION")
print("-" * 30)

# Scripts can be executed in several ways:
# 1. python script.py
# 2. python -m script
# 3. ./script.py (if shebang is present)

# Shebang example (for Unix-like systems)
# #!/usr/bin/env python3

# Command line arguments
import sys
print(f"Script name: {sys.argv[0]}")
print(f"Number of arguments: {len(sys.argv)}")
print(f"Arguments: {sys.argv[1:]}")

# 4. SCRIPT PATTERNS
print("\n4. SCRIPT PATTERNS")
print("-" * 30)

# Pattern 1: Simple script
def simple_script():
    """Simple script pattern."""
    print("Performing simple task...")
    result = 2 + 2
    print(f"Result: {result}")

# Pattern 2: Script with main function
def main():
    """Main function pattern."""
    print("Starting main function...")
    process_data()
    print("Main function completed")

def process_data():
    """Process some data."""
    data = [1, 2, 3, 4, 5]
    total = sum(data)
    print(f"Total: {total}")

# Pattern 3: Script with command line arguments
def parse_arguments():
    """Parse command line arguments."""
    if len(sys.argv) > 1:
        return sys.argv[1:]
    return []

def argument_script():
    """Script that uses command line arguments."""
    args = parse_arguments()
    if args:
        print(f"Processing arguments: {args}")
    else:
        print("No arguments provided")

# 5. SCRIPT EXAMPLES
print("\n5. SCRIPT EXAMPLES")
print("-" * 30)

# Example 1: File processing script
def file_processing_script():
    """Example of a file processing script."""
    try:
        # Create a sample file
        with open("sample.txt", "w") as f:
            f.write("Line 1\nLine 2\nLine 3\n")
        
        # Process the file
        with open("sample.txt", "r") as f:
            lines = f.readlines()
        
        print(f"File has {len(lines)} lines")
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")
        
        # Clean up
        import os
        os.remove("sample.txt")
        
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {e}")

# Example 2: Data analysis script
def data_analysis_script():
    """Example of a data analysis script."""
    # Simulate data
    data = [10, 20, 30, 40, 50]
    
    # Calculate statistics
    total = sum(data)
    average = total / len(data)
    maximum = max(data)
    minimum = min(data)
    
    print("Data Analysis Results:")
    print(f"Data: {data}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

# Example 3: Web scraping script
def web_scraping_script():
    """Example of a web scraping script."""
    print("Web scraping script example")
    print("(In a real script, this would use requests/BeautifulSoup)")
    
    # Simulate web scraping
    urls = ["https://example.com", "https://google.com"]
    for url in urls:
        print(f"Scraping: {url}")
        # In real script: response = requests.get(url)

# 6. SCRIPT BEST PRACTICES
print("\n6. SCRIPT BEST PRACTICES")
print("-" * 30)

# Best Practice 1: Use main function
def main():
    """Main function for the script."""
    print("Script execution started")
    
    # Parse arguments
    args = sys.argv[1:]
    
    # Perform tasks
    if args:
        process_arguments(args)
    else:
        perform_default_task()
    
    print("Script execution completed")

def process_arguments(args):
    """Process command line arguments."""
    print(f"Processing arguments: {args}")

def perform_default_task():
    """Perform default task when no arguments provided."""
    print("Performing default task")

# Best Practice 2: Error handling
def robust_script():
    """Script with proper error handling."""
    try:
        # Main script logic
        print("Executing main logic...")
        result = 10 / 2
        print(f"Result: {result}")
        
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Script cleanup completed")

# Best Practice 3: Logging
import logging

def logging_script():
    """Script with logging."""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    logger.info("Script started")
    logger.info("Processing data...")
    logger.info("Script completed")

# 7. SCRIPT TYPES
print("\n7. SCRIPT TYPES")
print("-" * 30)

# Type 1: Automation scripts
def automation_script():
    """Automation script example."""
    print("Automation script:")
    print("- File processing")
    print("- Data backup")
    print("- System maintenance")
    print("- Report generation")

# Type 2: Data processing scripts
def data_processing_script():
    """Data processing script example."""
    print("Data processing script:")
    print("- CSV file processing")
    print("- Database operations")
    print("- Data transformation")
    print("- Statistical analysis")

# Type 3: Utility scripts
def utility_script():
    """Utility script example."""
    print("Utility script:")
    print("- File renaming")
    print("- Directory cleanup")
    print("- Configuration management")
    print("- System monitoring")

# Type 4: Web scripts
def web_script():
    """Web script example."""
    print("Web script:")
    print("- API interactions")
    print("- Web scraping")
    print("- Server monitoring")
    print("- Content generation")

# 8. SCRIPT EXECUTION METHODS
print("\n8. SCRIPT EXECUTION METHODS")
print("-" * 30)

# Method 1: Direct execution
print("Method 1: python script.py")

# Method 2: Module execution
print("Method 2: python -m script")

# Method 3: Executable script (Unix)
print("Method 3: ./script.py (with shebang)")

# Method 4: Interactive execution
print("Method 4: python -i script.py")

# Method 5: One-liner execution
print("Method 5: python -c 'print(\"Hello\")'")

# 9. SCRIPT DEVELOPMENT
print("\n9. SCRIPT DEVELOPMENT")
print("-" * 30)

# Development workflow
def development_workflow():
    """Script development workflow."""
    print("1. Plan the script functionality")
    print("2. Write the script code")
    print("3. Test the script")
    print("4. Debug and refine")
    print("5. Document the script")
    print("6. Deploy the script")

# Testing scripts
def test_script():
    """Test script functionality."""
    print("Testing script...")
    
    # Test cases
    test_cases = [
        ("normal", "Expected behavior"),
        ("edge_case", "Handle edge cases"),
        ("error_case", "Handle errors gracefully")
    ]
    
    for test_name, description in test_cases:
        print(f"Test: {test_name} - {description}")

# 10. SCRIPT DEPLOYMENT
print("\n10. SCRIPT DEPLOYMENT")
print("-" * 30)

# Deployment considerations
def deployment_considerations():
    """Script deployment considerations."""
    print("Deployment Considerations:")
    print("- Environment setup")
    print("- Dependencies management")
    print("- Error handling")
    print("- Logging and monitoring")
    print("- Security considerations")
    print("- Performance optimization")

# Environment setup
def environment_setup():
    """Script environment setup."""
    print("Environment Setup:")
    print("- Python version compatibility")
    print("- Required packages")
    print("- Configuration files")
    print("- File permissions")
    print("- System requirements")

# 11. SCRIPT MONITORING
print("\n11. SCRIPT MONITORING")
print("-" * 30)

# Monitoring and logging
def script_monitoring():
    """Script monitoring and logging."""
    print("Script Monitoring:")
    print("- Execution time tracking")
    print("- Error logging")
    print("- Performance metrics")
    print("- Resource usage")
    print("- Success/failure reporting")

# Performance monitoring
def performance_monitoring():
    """Performance monitoring example."""
    import time
    
    start_time = time.time()
    
    # Simulate work
    for i in range(1000000):
        pass
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Script execution time: {execution_time:.4f} seconds")

# 12. SCRIPT SECURITY
print("\n12. SCRIPT SECURITY")
print("-" * 30)

# Security considerations
def security_considerations():
    """Script security considerations."""
    print("Security Considerations:")
    print("- Input validation")
    print("- File path security")
    print("- Command injection prevention")
    print("- Sensitive data handling")
    print("- Access control")

# Secure script example
def secure_script():
    """Example of a secure script."""
    import os
    
    # Validate input
    user_input = "safe_input"
    if not user_input.isalnum():
        print("Invalid input")
        return
    
    # Safe file operations
    safe_path = os.path.abspath(user_input)
    if not safe_path.startswith(os.getcwd()):
        print("Path traversal attempt detected")
        return
    
    print("Secure operation completed")

# 13. SCRIPT OPTIMIZATION
print("\n13. SCRIPT OPTIMIZATION")
print("-" * 30)

# Performance optimization
def script_optimization():
    """Script optimization techniques."""
    print("Optimization Techniques:")
    print("- Use appropriate data structures")
    print("- Minimize I/O operations")
    print("- Use generators for large datasets")
    print("- Profile and optimize bottlenecks")
    print("- Use multiprocessing when appropriate")

# Memory efficient script
def memory_efficient_script():
    """Memory efficient script example."""
    # Use generator instead of list for large datasets
    def number_generator(n):
        for i in range(n):
            yield i
    
    # Process numbers one at a time
    total = 0
    for num in number_generator(1000000):
        total += num
    
    print(f"Total: {total}")

# 14. SCRIPT DOCUMENTATION
print("\n14. SCRIPT DOCUMENTATION")
print("-" * 30)

# Documentation best practices
def script_documentation():
    """Script documentation best practices."""
    print("Documentation Best Practices:")
    print("- Clear script purpose")
    print("- Usage instructions")
    print("- Parameter descriptions")
    print("- Example usage")
    print("- Dependencies list")
    print("- Error handling documentation")

# Example documented script
def documented_script():
    """
    Example documented script.
    
    This script demonstrates proper documentation practices.
    
    Usage:
        python documented_script.py [options]
    
    Arguments:
        --input: Input file path
        --output: Output file path
    
    Examples:
        python documented_script.py --input data.txt --output result.txt
    
    Dependencies:
        - Python 3.7+
        - pandas
    
    Author: Script Author
    Version: 1.0.0
    """
    print("Documented script executed")

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What is a Script?")
print("- A Python file designed to be executed directly")
print("- Contains executable code at module level")
print("- Can be run from command line")
print("- Typically performs specific tasks")

print("\nScript Characteristics:")
print("- Standalone execution")
print("- Command line interface")
print("- Task automation")
print("- Data processing")
print("- System interaction")

print("\nScript vs Module:")
print("- Script: Designed to be run directly")
print("- Module: Designed to be imported")
print("- Script: Contains executable code")
print("- Module: Contains reusable functions/classes")

print("\nScript Best Practices:")
print("- Use main() function")
print("- Handle errors gracefully")
print("- Use proper logging")
print("- Validate inputs")
print("- Document thoroughly")
print("- Test thoroughly")
print("- Consider security")
print("- Optimize performance")

print("\nCommon Script Types:")
print("- Automation scripts")
print("- Data processing scripts")
print("- Utility scripts")
print("- Web scripts")
print("- System administration scripts")
print("- Reporting scripts")

print("\nExecution Methods:")
print("- python script.py")
print("- python -m script")
print("- ./script.py (with shebang)")
print("- python -i script.py")
print("- python -c 'code'") 