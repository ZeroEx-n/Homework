#№3 бинарный поиск
# ls = [1,2,3,4,5,6,7,8,9,10]
# target = 7
# low, hight = 0, len(ls) - 1
# found = False
# while low <= hight:
#     mid = (low + hight) // 2
#     if ls[mid] == target:
#         found = True
#         break
#     elif ls[mid] < target:
#         low = mid + 1 
#     else:
#         hight = mid - 1
# print(found)
#№1 ищет мин значение 
# ls = [4,2,8,6,1]
# min_value = ls[0]
# for x in ls:
#     if x < min_value:
#         min_value = x
# print(min_value)
#№2 добавляет в d массив(список) положительные цифры 
# ls = [4,-2,8, -6,1]
# d =[]
# for a in ls:
#     if a >=0:
#         d.append(a)
# print(d)
#№4 Сдвиг
# ls = [4,2,8,6,2]
# shifted = [0] * len(ls)
# for i in range(len(ls)):
#     shifted[(i+1) % len(ls)]= ls[i]
# print(shifted)
#№5 проверка на корень 
# n = 64 
# powerof2 = True
# while n > 1:
#     if n % 2 != 0:
#         powerof2 = False
#         break
#     n //= 2
# print(powerof2)
#№6 сортировка по возрастванию
# lst =[4,2,8,6,1]
# for i in range(len(lst)):
#     mix_index = i
#     for h in range(i +1, len(lst)):    
#         if lst[h] < lst[mix_index]:
#             mix_index = h
#     lst[i], lst[mix_index] = lst[mix_index], lst[i]
# print(lst)
#№7
# las = [4,2,8,6,2,1,4]
# uniq = 0 
# for i in range(len(las)):
#     is_uniq = True
#     for t in range(len(las)):
#         if i !=t and las[i] == las[t]:
#             is_uniq = False
#             break
#         if is_uniq:
#             uniq += 1 
# print(uniq)