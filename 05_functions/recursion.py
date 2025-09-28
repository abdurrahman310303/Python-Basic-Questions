def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def power_recursive(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power_recursive(base, exp - 1)

def sum_list_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])

def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

print(fibonacci_recursive(10))
print(factorial_recursive(5))
print(power_recursive(2, 8))
print(sum_list_recursive([1, 2, 3, 4, 5]))
print(reverse_string_recursive("hello"))
