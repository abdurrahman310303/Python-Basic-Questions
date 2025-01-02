student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
print(student.get("age"))
print(student.get("phone", "Not found"))

student["phone"] = "123-456-7890"
student.update({"city": "New York", "major": "CS"})
print(student)

del student["grade"]
removed = student.pop("phone")
print(student)
print(removed)

for key in student:
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")

keys = list(student.keys())
values = list(student.values())
print(keys)
print(values)
