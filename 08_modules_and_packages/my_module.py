def calculate_area_circle(radius):
    import math
    return math.pi * radius ** 2

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_triangle(base, height):
    return 0.5 * base * height

PI = 3.14159

if __name__ == "__main__":
    print("This is a custom module")
    print(calculate_area_circle(5))
    print(calculate_area_rectangle(4, 6))
    print(calculate_area_triangle(3, 8))
