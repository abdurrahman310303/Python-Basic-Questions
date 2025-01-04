class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        self.age += 1

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

person1 = Person("Alice", 25)
print(person1.introduce())
person1.have_birthday()
print(person1.age)

student1 = Student("Bob", 20, "S123")
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)
print(student1.get_average())
