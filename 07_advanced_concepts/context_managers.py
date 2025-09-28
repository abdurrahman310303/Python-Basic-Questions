class ContextManager:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"Entering {self.name} context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting {self.name} context")
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
            return False
        return True
    
    def do_something(self):
        print(f"Doing something in {self.name}")

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Setting up context")
    try:
        yield "context_value"
    finally:
        print("Cleaning up context")

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        return False

with ContextManager("Test") as cm:
    cm.do_something()

try:
    with ContextManager("Error Test") as cm:
        cm.do_something()
        raise ValueError("Something went wrong")
except ValueError:
    print("Caught the exception outside context")

with my_context() as value:
    print(f"Using context value: {value}")

with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")

with FileManager("test.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")

from contextlib import suppress

with suppress(FileNotFoundError):
    with open("nonexistent.txt", "r") as f:
        content = f.read()

print("This runs even if file doesn't exist")
