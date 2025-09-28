square = lambda x: x**2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(square(5))
print(add(3, 7))
print(is_even(4))
print(is_even(5))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(squares)
print(evens)

from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)
