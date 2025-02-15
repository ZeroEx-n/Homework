def bubble(lst):
    swap = True
    while swap:
        swap = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True


arr = []
for i in range(1, 11):
    a = int(input(f"Введите {i}-е число: "))
    arr.append(a)

bubble(arr)
print("Отсортированный список:", arr)


while True:
    target = int(input("Введите число для поиска: "))
    low, high = 0, len(arr) - 1
    found = False


    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            found = True
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if found:
        print(f"Число {target} найдено в списке!")
        break
    else:
        print(f"Число {target} не найдено, попробуйте снова.")
