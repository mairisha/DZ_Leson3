# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers = []
for i in range(5):
    x = int(input(''))
    numbers.append(x)
print(*numbers, sep=",")

summa = 0
for ind in range(len(numbers)):
    if ind % 2 != 0:
        summa = summa + numbers[ind]
print(summa)

###Напишите программу, которая найдёт произведение пар чисел списка.
###Парой считаем первый и последний элемент, второй и предпоследний и т.д.

some_list = input().split()
new_list = []
if len(some_list) % 2 == 0:
    middle = len(some_list) // 2
else:
    middle = len(some_list) // 2 + 1
    for start in range(0, middle):
        new_list.append(int(some_list[start]) * int(some_list[len(some_list) - start - 1]))
print(new_list)

###Задайте список из вещественных чисел. Напишите программу,
###которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

some_list = input().split()
maxx = 0
minn = 1
for el in some_list:
    if float(el) % 1 != 0:
        if float(el) % 1 < minn:
            minn = float(el) % 1
        if float(el) % 1 > maxx:
            maxx = float(el) % 1
print(round(maxx - minn, 2))

### Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = float(input())
some_list = []

while number >= 1:
    if number % 2 == 0:
        print(0)
        some_list.append(0)
        number = number/2
    else:
        print(1)
        some_list.append(1)
        number = number / 2
print(some_list)