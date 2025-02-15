#  Решить примеры и сказать к какой сложности относится эта задача
# 1 – Создать список чисел и посчитать сумму всех чисел
# p = [1,2,12,5,3]
# total = sum(p)
# print(total)    
# 2 - Напишите программу, которая найдёт минимальный элемент в списке целых чисел.
# ls = [4,2,8,6,1]
# min_value = ls[0]
# for x in ls:
#     if x < min_value:
#         min_value = x
# print(min_value)
# 3 - Напишите программу, которая проверяет, является ли заданное число n степенью двойки.
# n = 4 
# powerof2 = True
# while n > 1:
#     if n % 2 != 0:
#         powerof2 = False
#         break
#     n //= 2
# print(powerof2)
# 4 - Подсчитайте количество одинаковых элементов между двумя списками.
# Пример:
# Ввод: lst1 = [1, 2, 3, 4], lst2 = [3, 4, 5, 6]
# Вывод: Количество совпадений: 2
def count_cs(lst1, lst2):
    c = set(lst1) & set(lst2)  # Пересечение двух множеств
    return len(c)


lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
result = count_cs(lst1, lst2)
print(f"Количество совпадений: {result}")

# 5 - Дан список чисел. Подсчитайте, сколько раз каждое число встречается в списке.
# Пример:
# Ввод: [1, 2, 2, 3, 3, 3]
# Вывод: 1 встречается 1 раз, 2 встречается 2 раза, 3 встречается 3 раза 
from collections import Counter

def count_occurrences(lst):
    counter = Counter(lst)
    for num, count in counter.items():
        print(f"{num} встречается {count} раз")

lst = [1, 2, 2, 3, 3, 3]
count_occurrences(lst)

