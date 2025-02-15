# Найти все трехзначные простые числа. (Определить функцию,
# позволяющую распознавать простые числа.)
# def s(a):
#     if a <= 1:
#         return False
#     for i in range(2, int(a**0.5)):
#         if a % i == 0:
#             return False
#     return True

# d = []
# for j in range(100,1000):
#     if s(j):
#         d.append(j)

# print(d)

# 2. Даны два натуральных числа. Выяснить, в каком из них сумма цифр
# больше. (Определить функцию для расчета суммы цифр натурального
# числа.)

# def dd(n):
#     return sum(int(digit) for digit in str(n))

# n1 = int(input("First num:"))
# n2 = int(input("Second num:"))

# sum1 = dd(n1)
# sum2 = dd(n2)

# if sum1 > sum2:
#     print("N1>N2")
# elif sum1 < sum2:
#     print("N1<N2")
# else:
#     print("N1=N2")
