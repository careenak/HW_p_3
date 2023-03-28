
n = int(input("Введите количество элементов в массиве: "))
a = map(int, input("Введите эллементы массива через пробел: ").split())
x = int(input("Введите число для проверки: "))
print(sum(map(lambda z: int(z == x), a)))