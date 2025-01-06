import json

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}

json_string = json.dumps(person)
print(json_string)

json_pretty = json.dumps(person, indent=4)
print(json_pretty)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

with open('person.json', 'r') as file:
    loaded_person = json.load(file)
    print(loaded_person)

parsed_data = json.loads(json_string)
print(parsed_data["name"])

data_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

with open('people.json', 'w') as file:
    json.dump(data_list, file, indent=2)
