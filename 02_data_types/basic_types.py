integer_num = 42
float_num = 3.14159
complex_num = 3 + 4j
boolean_val = True
string_val = "Hello, Python!"

print(integer_num, type(integer_num))
print(float_num, type(float_num))
print(complex_num, type(complex_num))
print(boolean_val, type(boolean_val))
print(string_val, type(string_val))

none_val = None
print(none_val, type(none_val))

print(f"Complex real part: {complex_num.real}")
print(f"Complex imaginary part: {complex_num.imag}")

truthy_values = [1, "hello", [1, 2], {"key": "value"}]
falsy_values = [0, "", [], {}, None, False]

for val in truthy_values:
    print(f"{val} is {'truthy' if val else 'falsy'}")

for val in falsy_values:
    print(f"{val} is {'truthy' if val else 'falsy'}")
