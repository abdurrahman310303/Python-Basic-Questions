import math
import random
from datetime import datetime
import os

print(math.pi)
print(math.sqrt(16))
print(math.factorial(5))

print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c']))

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print(os.getcwd())
print(os.listdir('.'))
