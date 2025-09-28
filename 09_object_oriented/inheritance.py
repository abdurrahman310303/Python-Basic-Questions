class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow!"
    
    def purr(self):
        return f"{self.name} is purring"

class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name, "Bird")
        self.can_fly = can_fly
    
    def make_sound(self):
        return "Tweet!"
    
    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying!"
        return f"{self.name} cannot fly"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")
bird = Bird("Tweety")

animals = [dog, cat, bird]

for animal in animals:
    print(animal.info())
    print(animal.make_sound())
    print()

print(dog.fetch())
print(cat.purr())
print(bird.fly())
