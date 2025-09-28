fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]

print("Original fruits:", fruits)

fruits.append("date")
fruits.insert(1, "apricot")
fruits.remove("banana")

print("Modified fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

nested_list = [[1, 2], [3, 4], [5, 6]]
for sublist in nested_list:
    for item in sublist:
        print(item, end=" ")
    print()

list_operations = [
    len(numbers),
    max(numbers),
    min(numbers),
    sum(numbers),
    sorted(numbers, reverse=True)
]

for op in list_operations:
    print(op)
