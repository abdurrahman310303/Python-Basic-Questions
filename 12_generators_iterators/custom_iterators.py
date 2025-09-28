class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

class Range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += self.step

class EvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
    
    def __iter__(self):
        num = 0
        while num <= self.max_num:
            if num % 2 == 0:
                yield num
            num += 1

my_list = [1, 2, 3, 4, 5]
iterator = MyIterator(my_list)

for item in iterator:
    print(item)

custom_range = Range(0, 10, 2)
for num in custom_range:
    print(num)

even_nums = EvenNumbers(10)
for num in even_nums:
    print(num)

squares_iter = (x**2 for x in range(5))
for square in squares_iter:
    print(square)
