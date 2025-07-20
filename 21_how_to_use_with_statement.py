"""
21. How do you use the 'with' statement in Python?

The 'with' statement in Python is used for context management, ensuring proper
resource management and cleanup. It's commonly used with file operations, database
connections, and other resources that need to be properly closed or cleaned up.
"""

print("=== 'WITH' STATEMENT IN PYTHON ===\n")

# 1. BASIC WITH STATEMENT
print("1. BASIC WITH STATEMENT")
print("-" * 30)

# File handling with 'with' statement
with open("temp_file.txt", "w") as file:
    file.write("Hello, World!")
    print("File written successfully")

# Reading file with 'with' statement
with open("temp_file.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# Clean up
import os
if os.path.exists("temp_file.txt"):
    os.remove("temp_file.txt")

# 2. WITH STATEMENT BENEFITS
print("\n2. WITH STATEMENT BENEFITS")
print("-" * 30)

# Automatic resource management
print("Benefits of 'with' statement:")
print("- Automatic resource cleanup")
print("- Exception-safe")
print("- Cleaner code")
print("- No need to manually close resources")

# Example: Without 'with' statement (manual management)
def manual_file_handling():
    """Manual file handling without 'with' statement."""
    file = None
    try:
        file = open("temp_file.txt", "w")
        file.write("Manual handling")
        print("File written manually")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if file:
            file.close()
            print("File closed manually")

# Example: With 'with' statement (automatic management)
def automatic_file_handling():
    """Automatic file handling with 'with' statement."""
    try:
        with open("temp_file.txt", "w") as file:
            file.write("Automatic handling")
            print("File written automatically")
    except Exception as e:
        print(f"Error: {e}")
    # File is automatically closed, no finally needed

# 3. COMMON USE CASES
print("\n3. COMMON USE CASES")
print("-" * 30)

# File operations
def file_operations():
    """File operations with 'with' statement."""
    
    # Writing to file
    with open("data.txt", "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")
    
    # Reading from file
    with open("data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(f"Read: {line.strip()}")
    
    # Clean up
    if os.path.exists("data.txt"):
        os.remove("data.txt")

# Database connections (simulated)
def database_operations():
    """Simulated database operations with 'with' statement."""
    
    class DatabaseConnection:
        def __init__(self, name):
            self.name = name
            self.connected = False
        
        def __enter__(self):
            print(f"Connecting to {self.name}...")
            self.connected = True
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"Disconnecting from {self.name}...")
            self.connected = False
        
        def execute(self, query):
            print(f"Executing: {query}")
    
    # Using the database connection
    with DatabaseConnection("my_database") as db:
        db.execute("SELECT * FROM users")
        db.execute("INSERT INTO logs VALUES ('operation completed')")

# 4. CUSTOM CONTEXT MANAGERS
print("\n4. CUSTOM CONTEXT MANAGERS")
print("-" * 30)

# Creating custom context managers
class Timer:
    """Context manager for timing operations."""
    
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        print(f"Starting {self.name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        print(f"{self.name} completed in {duration:.4f} seconds")

# Using custom context manager
with Timer("data processing"):
    # Simulate some work
    import time
    time.sleep(0.1)

# 5. MULTIPLE CONTEXT MANAGERS
print("\n5. MULTIPLE CONTEXT MANAGERS")
print("-" * 30)

# Multiple 'with' statements
def multiple_files():
    """Working with multiple files."""
    
    # Create two files
    with open("file1.txt", "w") as f1:
        f1.write("Content from file 1")
    
    with open("file2.txt", "w") as f2:
        f2.write("Content from file 2")
    
    # Read both files
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        content1 = f1.read()
        content2 = f2.read()
        print(f"File 1: {content1}")
        print(f"File 2: {content2}")
    
    # Clean up
    for filename in ["file1.txt", "file2.txt"]:
        if os.path.exists(filename):
            os.remove(filename)

# 6. EXCEPTION HANDLING WITH 'WITH'
print("\n6. EXCEPTION HANDLING WITH 'WITH'")
print("-" * 30)

# Exception handling in 'with' statement
def exception_handling():
    """Exception handling with 'with' statement."""
    
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found, but resources were properly cleaned up")
    
    # Even if exception occurs, file is properly closed
    print("Exception handled, cleanup completed")

# 7. CONTEXT MANAGER PROTOCOL
print("\n7. CONTEXT MANAGER PROTOCOL")
print("-" * 30)

# Understanding the context manager protocol
class CustomContextManager:
    """Custom context manager implementing the protocol."""
    
    def __init__(self, name):
        self.name = name
        self.resource = None
    
    def __enter__(self):
        """Called when entering the context."""
        print(f"Entering {self.name} context")
        self.resource = f"Resource for {self.name}"
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the context."""
        print(f"Exiting {self.name} context")
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        self.resource = None
        # Return False to re-raise the exception, True to suppress it
        return False

# Using the custom context manager
with CustomContextManager("test") as resource:
    print(f"Using resource: {resource}")
    # This would raise an exception
    # raise ValueError("Test exception")

# 8. PRACTICAL EXAMPLES
print("\n8. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Logging context
class LoggingContext:
    """Context manager for logging operations."""
    
    def __init__(self, operation_name):
        self.operation_name = operation_name
    
    def __enter__(self):
        print(f"Starting operation: {self.operation_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"Operation {self.operation_name} completed successfully")
        else:
            print(f"Operation {self.operation_name} failed: {exc_type.__name__}")

# Example 2: Temporary directory
class TemporaryDirectory:
    """Context manager for temporary directory."""
    
    def __init__(self, prefix="temp"):
        self.prefix = prefix
        self.path = None
    
    def __enter__(self):
        import tempfile
        self.path = tempfile.mkdtemp(prefix=self.prefix)
        print(f"Created temporary directory: {self.path}")
        return self.path
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import shutil
        shutil.rmtree(self.path)
        print(f"Removed temporary directory: {self.path}")

# Using the practical examples
with LoggingContext("data processing"):
    print("Processing data...")
    # Simulate work
    import time
    time.sleep(0.05)

with TemporaryDirectory("demo_") as temp_dir:
    print(f"Working in: {temp_dir}")
    # Create a file in the temp directory
    with open(f"{temp_dir}/test.txt", "w") as f:
        f.write("Temporary file content")

# 9. ADVANCED PATTERNS
print("\n9. ADVANCED PATTERNS")
print("-" * 30)

# Pattern 1: Resource pooling
class ConnectionPool:
    """Simulated connection pool."""
    
    def __init__(self, pool_size=5):
        self.pool_size = pool_size
        self.connections = []
    
    def get_connection(self):
        """Get a connection from the pool."""
        if not self.connections:
            print("Creating new connection...")
            return "connection"
        else:
            print("Reusing connection from pool...")
            return self.connections.pop()
    
    def return_connection(self, connection):
        """Return a connection to the pool."""
        if len(self.connections) < self.pool_size:
            self.connections.append(connection)
            print("Connection returned to pool")
        else:
            print("Pool full, closing connection")

class PooledConnection:
    """Context manager for pooled connections."""
    
    def __init__(self, pool):
        self.pool = pool
        self.connection = None
    
    def __enter__(self):
        self.connection = self.pool.get_connection()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.return_connection(self.connection)

# Using the connection pool
pool = ConnectionPool(3)

with PooledConnection(pool) as conn:
    print(f"Using connection: {conn}")

# Pattern 2: Transaction management
class Transaction:
    """Simulated transaction context manager."""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.committed = False
    
    def __enter__(self):
        print(f"Starting transaction in {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"Committing transaction in {self.db_name}")
            self.committed = True
        else:
            print(f"Rolling back transaction in {self.db_name}")
            self.committed = False

# Using transaction
with Transaction("my_database") as tx:
    print("Performing database operations...")
    # If an exception occurs here, transaction will be rolled back

# 10. CONTEXT MANAGER UTILITIES
print("\n10. CONTEXT MANAGER UTILITIES")
print("-" * 30)

# Using contextlib utilities
from contextlib import contextmanager

@contextmanager
def simple_context_manager(name):
    """Simple context manager using decorator."""
    print(f"Entering {name}")
    try:
        yield f"Resource for {name}"
    finally:
        print(f"Exiting {name}")

# Using the decorated context manager
with simple_context_manager("test") as resource:
    print(f"Using: {resource}")

# 11. NESTED CONTEXT MANAGERS
print("\n11. NESTED CONTEXT MANAGERS")
print("-" * 30)

# Nested context managers
def nested_context_managers():
    """Example of nested context managers."""
    
    with Timer("outer operation"):
        with LoggingContext("inner operation"):
            print("Performing nested operations...")
            import time
            time.sleep(0.05)

# 12. ERROR HANDLING PATTERNS
print("\n12. ERROR HANDLING PATTERNS")
print("-" * 30)

# Pattern 1: Graceful degradation
def graceful_degradation():
    """Context manager with graceful degradation."""
    
    class FallbackContext:
        def __init__(self, primary, fallback):
            self.primary = primary
            self.fallback = fallback
        
        def __enter__(self):
            try:
                self.resource = self.primary()
                print("Using primary resource")
                return self.resource
            except Exception:
                self.resource = self.fallback()
                print("Using fallback resource")
                return self.resource
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if hasattr(self.resource, 'close'):
                self.resource.close()

# 13. PERFORMANCE CONSIDERATIONS
print("\n13. PERFORMANCE CONSIDERATIONS")
print("-" * 30)

# Performance benefits of 'with' statement
def performance_benefits():
    """Demonstrate performance benefits."""
    
    import time
    
    # Without 'with' statement
    start = time.time()
    for _ in range(1000):
        file = open("temp.txt", "w")
        file.write("test")
        file.close()
    without_with_time = time.time() - start
    
    # With 'with' statement
    start = time.time()
    for _ in range(1000):
        with open("temp.txt", "w") as file:
            file.write("test")
    with_with_time = time.time() - start
    
    print(f"Without 'with': {without_with_time:.4f} seconds")
    print(f"With 'with': {with_with_time:.4f} seconds")
    
    # Clean up
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")

# 14. BEST PRACTICES
print("\n14. BEST PRACTICES")
print("-" * 30)

print("Best Practices for 'with' Statement:")
print("1. Use 'with' for all resource management")
print("2. Create custom context managers for complex resources")
print("3. Handle exceptions properly in __exit__")
print("4. Use contextlib utilities for simple cases")
print("5. Document your context managers")
print("6. Test context managers thoroughly")
print("7. Use nested context managers when appropriate")
print("8. Consider performance implications")

# 15. SUMMARY
print("\n15. SUMMARY")
print("-" * 30)

print("What is the 'with' Statement?")
print("- A context management construct")
print("- Ensures proper resource cleanup")
print("- Handles exceptions gracefully")
print("- Provides cleaner, safer code")

print("\nContext Manager Protocol:")
print("- __enter__(): Called when entering context")
print("- __exit__(): Called when exiting context")
print("- Automatic resource management")
print("- Exception handling")

print("\nCommon Use Cases:")
print("- File operations")
print("- Database connections")
print("- Network connections")
print("- Locks and synchronization")
print("- Custom resource management")

print("\nBenefits:")
print("- Automatic cleanup")
print("- Exception safety")
print("- Cleaner code")
print("- Resource management")
print("- Reduced boilerplate")

print("\nBest Practices:")
print("- Always use 'with' for resource management")
print("- Create custom context managers when needed")
print("- Handle exceptions properly")
print("- Use contextlib utilities")
print("- Document your context managers")
print("- Test thoroughly") 