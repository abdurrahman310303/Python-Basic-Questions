import math

def calculate_area(radius):
    return math.pi * radius ** 2

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]

print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

area = calculate_area(5)
print(f"Circle area: {area:.2f}")

class SimpleClass:
    def __init__(self, value):
        self.value = value
    
    def display(self):
        return f"Value: {self.value}"

obj = SimpleClass(42)
print(obj.display())
