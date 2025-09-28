class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @classmethod
    def create_scientific(cls):
        return cls()
    
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        if operation == "add":
            result = self.add(a, b)
        elif operation == "multiply":
            result = self.multiply(a, b)
        else:
            result = None
        
        if result is not None:
            self.history.append(f"{operation}({a}, {b}) = {result}")
        
        return result

calc = Calculator()
print(calc.calculate("add", 5, 3))
print(calc.calculate("multiply", 4, 7))

print(Calculator.add(10, 20))
print(Calculator.multiply(6, 8))

scientific_calc = Calculator.create_scientific()
print(scientific_calc.calculate("add", 2, 3))

class MathUtils:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

print(MathUtils.is_prime(17))
print(MathUtils.factorial(5))
