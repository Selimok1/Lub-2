# Запрашиваем у пользователя два числа
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    # Делим числа
    result = a / b
    print("Результат деления:", result)
except ZeroDivisionError:
    print("Ошибка! Деление на ноль невозможно.")
except ValueError:
    print("Ошибка! Надо вводить числа.")