# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
# except:
#     ZeroDivisionError
#     print("Error try again")


# list = [1,3,9]
# try:
#     y = list[9]
#     print(y)
# except:
#     IndexError
#     print("Error range")



try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    

    result = num1 / num2
    print("Результат деления: ", result)
except ZeroDivisionError:
    print("Деление на ноль невозможно!")
except ValueError:
    print("Введите корректные числа!")




