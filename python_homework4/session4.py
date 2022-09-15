# Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141

# import math
# from cmath import pi
# d = input('введите точность 0.00.... ')
# print (round(pi, len(d) - 1 - len(str(math.trunc(float(d))))))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('введите число '))
# list = []
# def Func(n):  
#     for j in range (2, int(n+1)):    # находим простое число
#         countt = 0
#         for i in range(2, j):
#             if j % i == 0:
#                 countt +=1   
#         if countt <=0:          
#             if n % j == 0:      # пробуем является ли найденное простое число множителем
#                 n /= j
#                 list.append(j)  # если множитель найден добавляем в список
#                 if n > 1:
#                     Func(n)     # ищем следующее
#                     return
#     return
# Func(n)
# print (list)



# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# list = [0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6, 9, 10, 11]
# uniq = [list[i] for i in range(len(list) - 1) if list[i] != list[i + 1] and list[i] != list[i - 1]]
# if list[-1] != list[-2]:
#     uniq.append(list[-1])
# print (list, uniq, sep='\n')



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# k = int(input('введите k - '))
# mnogochlen = ''
# for i in range(k+1, 0, -1):
#     mnogochlen += str(random.randint(0,100))
#     if i > 1:
#         mnogochlen += '*' + 'x' + '^' + str(i) + ' + '
# mnogochlen += ' = 0'
# data = open ('file.txt', 'w')
# data.write(mnogochlen)
# data.close
     


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
#     if file1[i-1] != '^':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close