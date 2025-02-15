

num =[1,2,3,4,5,6]
def sum_even_numbers(arr):
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num 
    return total
result = sum_even_numbers(num)
print(result)



# 2. Минимум и максимум массива
# Напишите функцию, которая принимает массив и возвращает максимальный и минимальное значение (min, max).

def find_min_max(arr):
    return min(arr), max(arr)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
min_value, max_value = find_min_max(numbers)
print(f"Минимальное значение: {min_value}, Максимальное значение: {max_value}")

# 3. Сумма чисел от 1 до N
# Напишите программу, которая запрашивает у пользователя число N и выводит сумму всех чисел от 1 до N.
def sum_numbers(N):
    return sum(range(1, N+1))

# Пример использования
N = int(input("Введите число N: "))
result = sum_numbers(N)
print(f"Сумма чисел от 1 до {N} = {result}")

# 4. Создание таблицы умножения
# Напишите программу, которая создает таблицу умножения для чисел от 1 до 10.
# Пример:
# 5 *1 =5
# 5*2 = 10
# 5 *3 = 15 
# Подсказка – “f”
def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")

multiplication_table()

# 5. Обратная строка
# Напишите функцию, которая принимает строку и возвращает ее в обратном порядке.
# Подсказка – reverse()
def reverse_string(s):
    return s[::-1]


word = input("Введите строку: ")
reversed_word = reverse_string(word)
print(f"Обратная строка: {reversed_word}")

# 6. Поиск гласных
# Напишити программу, которая принимает слово от пользователя и посчитайте сумму гласных букв в слове. Подчет гласных должен быть как для русских слов, так и для английских
def count_vowels(word):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = input("Введите слово: ")
vowel_count = count_vowels(word)
print(f"Количество гласных в слове: {vowel_count}")

# 7. Удаление повторяющихся элементов
# Напишите программу, которая принимает массив и возвращает новый массив, содержащий только уникальные элементы.
def remove_duplicates(a):
    return list(set(a))


numbers = [1, 2, 3, 1, 4, 5, 5, 6, 2]
unique_numbers = remove_duplicates(numbers)
print(f"Уникальные элементы: {unique_numbers}")

