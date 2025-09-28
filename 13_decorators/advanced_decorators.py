def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
        return wrapper
    return decorator

def validate_types(**types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, types.values())):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} must be of type {expected_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class property_decorator:
    def __init__(self, func):
        self.func = func
        self.value = None
    
    def __get__(self, obj, objtype=None):
        if self.value is None:
            self.value = self.func(obj)
        return self.value

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success!"

@validate_types(a=int, b=int)
def add_numbers(a, b):
    return a + b

print(fibonacci(10))
print(fibonacci(10))

try:
    result = unreliable_function()
    print(result)
except Exception as e:
    print(f"Final failure: {e}")

print(add_numbers(5, 3))

try:
    add_numbers("5", 3)
except TypeError as e:
    print(f"Type error: {e}")
