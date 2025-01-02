def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def mixed_args(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print(sum_all(1, 2, 3, 4, 5))
print_info(name="John", age=30, city="New York")
mixed_args("Alice", 1, 2, 3, role="developer", experience=5)
