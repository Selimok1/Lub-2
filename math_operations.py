# math_operations.py
def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b

def divide(a, b):
    # Делим числа, если b не равно нулю
    if b == 0:
        return "Деление на ноль невозможно"
    else:
        return a / b