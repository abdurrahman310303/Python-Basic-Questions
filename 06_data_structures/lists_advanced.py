numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, 0)
numbers.remove(3)
popped = numbers.pop()
print(numbers)
print(popped)

fruits = ["apple", "banana"]
fruits.extend(["orange", "grape"])
print(fruits)
print(len(fruits))
print(fruits.index("banana"))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

nested = [1, [2, 3], [4, [5, 6]]]
print(nested[2][1][0])
