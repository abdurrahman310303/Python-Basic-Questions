fruits = {"apple", "banana", "orange", "grape"}
vegetables = {"carrot", "broccoli", "spinach", "tomato"}

print(fruits)
print(len(fruits))

fruits.add("mango")
fruits.add("apple")
print(fruits)

fruits.remove("banana")
fruits.discard("kiwi")
print(fruits)

print("apple" in fruits)
print("banana" in fruits)

union_set = fruits | vegetables
intersection_set = fruits & vegetables
difference_set = fruits - vegetables

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")

numbers1 = {1, 2, 3, 4, 5}
numbers2 = {4, 5, 6, 7, 8}

print(numbers1.issubset(numbers2))
print(numbers1.issuperset(numbers2))
print(numbers1.isdisjoint(numbers2))

frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
