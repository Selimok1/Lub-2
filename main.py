with open('data.txt', 'w') as file: # Создадим файл data.txt с 10 числами
    numbers = [13, 7, 25, 3, 18, 9, 30, 5, 22, 16]
    for num in numbers:
        file.write(str(num) + '\n')
with open('data.txt', 'r') as file:
    # Читаем все строки и преобразуем их в числа
    data = [int(line.strip()) for line in file]

# Вычисление необходимых значений
total_sum = sum(data)
average = total_sum / len(data)
maximum = max(data)
minimum = min(data)

# Запись результатов в result.txt
with open('result.txt', 'w') as result_file:
    result_file.write(f"Сумма: {total_sum}\n")
    result_file.write(f"Среднее: {average}\n")
    result_file.write(f"Максимум: {maximum}\n")
    result_file.write(f"Минимум: {minimum}\n")

print("Результаты записаны в result.txt")