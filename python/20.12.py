#1
# try:
#     n = int(input("Write a number:"))
#     print(n)
# except:
#     print("WRITE A FREAKING NUMBER")
# print(5)



#2
# try:
#     n = int(input("Write a number:"))
#     a = int(input("Write a sec num:"))
#     print(n/a)
# except ZeroDivisionError:
#     print("NO A FREAKING 0")

#3
# try:
#     x = int("7") #if write a Word exept may work
#     print(x)
# except ValueError:
#     print("Error: incorect!")

#4
# my_list= [1,2,3]
# try:
#     x = my_list[5]
#     print(x)
# except IndexError:
#     print("Error : Index without range!")

#5
# try:
#     l = "10" / 2
# except TypeError:
#     print("Error: uncorrect data type")

#6
# adt = {"a": 1, "b":2}
# try:
#     r = adt["c"]
#     print(r)
# except KeyError:
#     print("Error: Not founded key")

#7
# try:
#     o=int("hello")
#     p=10/0
# except ValueError:
#     print("Error: incorrect transformation")
# except ZeroDivisionError:
#     print("Error: YOU CAN NOT /0")

# import math
# print(math.factorial(5))


try:
    v = int(input("first num:"))
    b = int(input("second num:"))
    print("addition: ",v+b, "subtraction: ", v-b,"multiplication:", v*b,"division:", v/b )
except ZeroDivisionError:
    print("Error: YOU CAN NOT /0")


try:
    n = int(input("Write a number:"))
    print(n)
except:
    print("WRITE A FREAKING NUMBER")



my_range= [1,2,3]
try:
    x = my_range[5]
    print(x)
except IndexError:
    print("Error : Index without range!")

hsdf = {"a": 1, "b":2}
try:
    ss = hsdf["x"]
    print(ss)
except KeyError:
    print("UNKOWN KEY")

