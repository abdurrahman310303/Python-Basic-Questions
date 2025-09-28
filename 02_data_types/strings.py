text1 = "Hello"
text2 = 'World'
text3 = """Multi-line
string content
here"""

print(text1 + " " + text2)
print(f"Formatted: {text1}, {text2}!")
print(text3)

operations = [
    text1.upper(),
    text1.lower(),
    text1.replace("H", "h"),
    text1.find("l"),
    text1.count("l"),
    len(text1)
]

for op in operations:
    print(op)

name = "Alice"
age = 25
score = 95.67

formatted_strings = [
    f"Name: {name}, Age: {age}",
    "Score: {:.1f}%".format(score),
    "Hello {}!".format(name)
]

for fs in formatted_strings:
    print(fs)
