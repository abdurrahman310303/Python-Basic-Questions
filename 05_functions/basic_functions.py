def greet():
    print("Hello, World!")

def greet_person(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def multiply(x, y=1):
    return x * y

def get_full_name(first, last):
    return f"{first} {last}"

greet()
greet_person("Alice")
result = add_numbers(10, 5)
print(result)
print(multiply(5))
print(multiply(5, 3))
print(get_full_name("John", "Doe"))
