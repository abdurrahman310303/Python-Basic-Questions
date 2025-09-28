text = "Hello World Python Programming"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.count('o'))
print(text.find('World'))
print(text.index('Python'))

print(text.replace('Python', 'Java'))
print(text.split())
print(text.split('o'))

words = ['Hello', 'World', 'Python']
print(' '.join(words))
print('-'.join(words))

print(text.startswith('Hello'))
print(text.endswith('Programming'))

sample = "   Python Programming   "
print(sample.strip())
print(sample.lstrip())
print(sample.rstrip())

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))
