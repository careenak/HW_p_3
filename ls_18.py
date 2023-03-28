n = int(input("Введите количество элементов в массиве: "))
lst = map(int, input("Введите эллементы массива через пробел: ").split())
x = int(input("Введите число для проверки: "))
print(min(lst, key=lambda a:abs(a-x)))

