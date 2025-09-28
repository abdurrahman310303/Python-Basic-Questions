age = 18

if age >= 18:
    print("You are an adult")
    if age >= 65:
        print("You are a senior citizen")
    else:
        print("You are a working-age adult")
else:
    print("You are a minor")

for i in range(3):
    print(f"Level 1: {i}")
    for j in range(2):
        print(f"  Level 2: {j}")
        if j == 1:
            print(f"    Level 3: Final nested level")

def nested_function():
    x = 10
    
    def inner_function():
        return x * 2
    
    return inner_function()

result = nested_function()
print(f"Nested result: {result}")
