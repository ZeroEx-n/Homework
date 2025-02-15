# import random

# def print_list(lst):
#     for i in range(0, len(lst), 10):
#         print(lst[i:i+10])

# random_numbers = [random.uniform(0, 100) for _ in range(100)]

# print("Исходный список:")
# print_list(random_numbers)

# random_numbers.sort()

# print("\nОтсортированный список:")
# print_list(random_numbers)

# Чтобы избежать изменения исходного списка, не обязательно использовать
# кортеж. Можно создать его копию с помощью метода списка copy() или
# взять срез от начала до конца [:]. Скопируйте список первым и вторым
# способом и убедитесь, что изменение копий никак не отражается на
# оригинале.
# my_tuple = [True, False]
# print(my_tuple)
# a = [True, False]
# b = a.copy() 
# print(b)
# 3. Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0. Для
# заполнения кортежей числами напишите одну функцию. Объедините два
# кортежа с помощью оператора +, создав тем самым третий кортеж. С
# помощью метода кортежа count() определите в нем количество нулей.
# Выведите на экран третий кортеж и количество нулей в нем.
# import random
# def create_tuple(start, end, size):
#     return tuple(random.randint(start, end) for _ in range(size))
# s =create_tuple(0,5,10)
# x =create_tuple(-5,0,10)

# k = s+x
# q =k.count(0)
# print("third cortedge:", k)
# print("Sum of 0:", q)
# 4. Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а,
# 7в и т. п.). Внесите изменения в словарь согласно следующему: а) в одном
# из классов изменилось количество учащихся, б) в школе появился новый
# класс, с) в школе был расформирован (удален) другой класс. Вычислите
# общее количество учащихся в школе.
# c = {
#     "1А": 25,      
#     "1Б": 22,   
#     "2А": 24,  
#     "2Б": 20,  
#     "3А": 23,  
#     "3Б": 21,  
#     "4А": 26,  
#     "4Б": 25, 
#     "5А": 24,  
#     "5Б": 23,     
#     "6А": 27,
#     "6Б": 21, 
#     "7А": 28, 
#     "7Б": 25,  
#     "7В": 22,  
#     "8А": 30,  
#     "8Б": 29
# }
#№3
# fe = input("remove class by 1A to 8Б:")
# if fe in c:
#     del c[(fe)]
#     print(f'Class {fe} was removed')
# else:
#     print(f'Class {fe} was not founded')
# print("Updaten list:")
# №1
# fe = input("add new class member by 1A to 8Б:")
# m = int(input('New members:'))
# if feh in c:
#     c[feh] += m 
#     print(f'Class {feh} was update')
# else:
#     print(f'Class {feh} was not founded')
# print(f"Now in class {feh}: {c[feh]} students")
#№2
# fex = input("add class:")
# if fex in c:
#     c.update[(fex)]
# print(f'Class {fex} was add')
# 5. Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items передайте в
# написанную вами функцию, которая с
# оздает и возвращает новый словарь,
# "обратный" исходному, т. е. ключами являются строки, а значениями –
# числа.

# my_dict = {1: 'a', 2: 'b', 3: 'c'}
# items = my_dict.items()
# def reverse_dict(items):
#     reversed_dict = {}
#     for key, value in items:
#         reversed_dict[value] = key 
#     return reversed_dict
# reversed_dict = reverse_dict(items)
# print(reversed_dict)


