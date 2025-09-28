from functools import reduce, partial, wraps
from operator import add, mul

numbers = [1, 2, 3, 4, 5]

sum_result = reduce(add, numbers)
print(f"Sum using reduce: {sum_result}")

product_result = reduce(mul, numbers)
print(f"Product using reduce: {product_result}")

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
triple = partial(multiply, 3)

print(f"Double 5: {double(5)}")
print(f"Triple 4: {triple(4)}")

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"Square of 6: {square(6)}")
print(f"Cube of 4: {cube(4)}")

def cache_results(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@cache_results
def expensive_calculation(n):
    print(f"Computing expensive calculation for {n}")
    return sum(range(n))

result1 = expensive_calculation(1000)
result2 = expensive_calculation(1000)
print(f"Results: {result1}, {result2}")

from functools import singledispatch

@singledispatch
def process_data(arg):
    print(f"Processing unknown type: {type(arg)}")

@process_data.register
def _(arg: int):
    print(f"Processing integer: {arg}")
    return arg * 2

@process_data.register
def _(arg: str):
    print(f"Processing string: {arg}")
    return arg.upper()

@process_data.register
def _(arg: list):
    print(f"Processing list: {arg}")
    return [x * 2 for x in arg]

process_data(42)
process_data("hello")
process_data([1, 2, 3])
process_data(3.14)

def compose_functions(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def square(x):
    return x ** 2

composed = compose_functions(square, multiply_by_two, add_one)
print(f"Composed function result: {composed(3)}")

from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci 30: {fibonacci(30)}")
print(f"Cache info: {fibonacci.cache_info()}")
