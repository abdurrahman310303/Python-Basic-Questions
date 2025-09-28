from collections import Counter, defaultdict, deque, namedtuple

text = "hello world hello python world"
word_count = Counter(text.split())
print(word_count)
print(word_count.most_common(2))

numbers = [1, 2, 3, 1, 2, 1]
num_count = Counter(numbers)
print(num_count)

dd = defaultdict(list)
data = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
for key, value in data:
    dd[key].append(value)
print(dict(dd))

dd_int = defaultdict(int)
for char in "hello":
    dd_int[char] += 1
print(dict(dd_int))

queue = deque([1, 2, 3, 4, 5])
queue.appendleft(0)
queue.append(6)
print(queue)
print(queue.popleft())
print(queue.pop())
print(queue)

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(p1)
print(p1.x, p1.y)

Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'New York')
print(person.name)
