# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# sum = 0
# list = [2, 3, 5, 9, 3, 5, 9, 8, 1]
# print (list)
# for i in range(len(list)-1):
#     x = i % 2
#     if x != 0: 
#         sum += list[i]
#         print (list[i], end = ', ')
# print (f' сумма = {sum}')

# # вариант с методом
# list = [2, 3, 5, 9, 3]
# def Sum(list):    
#     sum = 0
#     i = 1
#     while i < len(list)-1:
#         x = i % 2
#         if x != 0: 
#             sum += list[i]
#         i+=1
#     return sum
# print (f'{list} -> сумма = {Sum(list)}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import math
# multiple = 0
# list = [2, 3, 4, 5, 6]
# print (list)
# for i in range(math.ceil(len(list)/2)):
#     multiple = list[i] * list[(-i)-1]
#     print(f'{list[i]} * {list[-i-1]} = {multiple}')



# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 10.01]
min = list[0] % 1
max = list[0] % 1
for i in list:
    item = i % 1    
    if item < min: min = item
    if item > max: max = item
print ('{} min = {} max = {} => {}'.format(list, round(min,2), round(max,2), round(max - min, 2)))



# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('input number '))
# x = num
# list=[]
# while x>0:
#     list.append(x % 2)
#     x = int (x / 2)
# print (f'{num} ->', end = ' ')
# for i in list[::-1]:
#     print (i, end = '')



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

# list = []
# k = 8
# x = 0
# y = 1
# for i in range(-k,-1):
#     z = x - y
#     list.append(z)
#     x = y
#     y = z
# lenn = len(list) - 1
# for j in range(int(lenn / 2)):
#     tmp = list[j]
#     list[j] = list [lenn]
#     list [lenn] = tmp
#     lenn -= 1
# x = 0
# y = 1
# list.append(x)
# list.append(y)
# for i in range(k-1):
#     z = x + y
#     list.append(z)
#     x = y
#     y = z    
# print (list)