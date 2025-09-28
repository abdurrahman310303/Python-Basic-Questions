numbers = [1, 4, 9, 16, 25]
squares = [x**2 for x in range(6)]
evens = [x for x in range(10) if x % 2 == 0]
upper_words = [word.upper() for word in ["hello", "world", "python"]]

print(numbers)
print(squares)
print(evens)
print(upper_words)

matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)

filtered = [x for x in range(20) if x % 3 == 0 and x % 2 == 0]
print(filtered)
