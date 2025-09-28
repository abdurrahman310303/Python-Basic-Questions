import pickle
import json

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age}, '{self.email}')"
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['email'])

person = Person("Alice", 30, "alice@example.com")
data = [1, 2, 3, {"key": "value"}, person]

with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)
    print("Loaded data:", loaded_data)

pickled_string = pickle.dumps(person)
print("Pickled string length:", len(pickled_string))

unpickled_person = pickle.loads(pickled_string)
print("Unpickled person:", unpickled_person)

people = [
    Person("Alice", 30, "alice@example.com"),
    Person("Bob", 25, "bob@example.com"),
    Person("Charlie", 35, "charlie@example.com")
]

people_dicts = [person.to_dict() for person in people]
with open('people.json', 'w') as file:
    json.dump(people_dicts, file, indent=2)

with open('people.json', 'r') as file:
    loaded_dicts = json.load(file)
    loaded_people = [Person.from_dict(data) for data in loaded_dicts]
    for person in loaded_people:
        print(person)

complex_data = {
    'numbers': [1, 2, 3],
    'text': "Hello, World!",
    'nested': {'inner': [4, 5, 6]}
}

with open('complex.pickle', 'wb') as file:
    pickle.dump(complex_data, file, protocol=pickle.HIGHEST_PROTOCOL)

with open('complex.pickle', 'rb') as file:
    loaded_complex = pickle.load(file)
    print("Complex data:", loaded_complex)
