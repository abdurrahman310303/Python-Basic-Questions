with open('sample.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling example.\n")

with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

with open('sample.txt', 'a') as file:
    file.write("Appended line.\n")

import os
if os.path.exists('sample.txt'):
    print("File exists")
    print(f"File size: {os.path.getsize('sample.txt')} bytes")

try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
