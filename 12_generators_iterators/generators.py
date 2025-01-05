def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))

def square_generator(n):
    for i in range(n):
        yield i ** 2

squares = square_generator(5)
for square in squares:
    print(square)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

numbers = [1, 2, 3, 4, 5]
squared = (x**2 for x in numbers)
print(list(squared))
