numbers = list(range(1, 21)) # список чисел от 1 до 20

evens = list(filter(lambda x: x % 2 == 0, numbers)) # оставить только четные

plus_ten = list(map(lambda x: x + 10, numbers)) # увеличить каждое число на 10

sorted_desc = sorted(plus_ten, reverse=True) # отсортировать по убыванию

print("Четные числа:", evens)
print("Увеличенные числа:", plus_ten)
print("Отсортированные по убыванию:", sorted_desc)