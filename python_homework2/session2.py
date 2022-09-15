# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num=input('input number ')
# sum=0
# for i in num:  
#     if ord(i)>47 and ord(i)<58 : 
#         sum=sum+int(i)
# print (f'- {num} -> {sum}')



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num=int(input('input number '))
# result=1
# count=0
# numbers1=[]
# numbers2=[]
# for i in range(1,num+1):                                    # подсчитывает и кладет в список результаты произведения
#     result*=i
#     numbers1.append(result)
# print (f'- пусть N = {num}, тогда {numbers1}', end=' ')     # выводит результаты умножения
# for m in range(1,num+1):                                    # отображает множители
#     countt=1    
#     while countt<=m:       
#         print (f'{countt}', end='')
#         countt+=1
#         if countt<=m: print (f'*', end='')
#     if m<num: print (f',', end=' ')

# n = int(input())
# res = [1]
# for i in range(2, n + 1):
#     res.append(res[-1] * i)
# print(res)       
  
  
# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# k=int(input('input number '))
# sum=0
# i=0
# list=[]
# for j in range(1,k+1):
#     list.append((1 + (1/j))**j)
#     # list[j]=(1 + (1/j+1))**j+1
#     sum+=list[i]
#     i+=1
# print (list)   
# print(sum) 

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
        
# k=int(input('input number '))
# sum=0
# i=0
# list=[]
# for j in range(1,k+1):
#     list.append((1 + (1/j))**j)
#     sum+=list[i]
#     i+=1
# print (list)   
# print(sum) 


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# import random
# n=int(input('input number '))
# list=[]
# for i in range(n):                      # генератор случайных чисел
#     a=random.randint(-n, n)
#     list.append(a)   
# print (list)
# index_list = input(f'введите позиции элементов от 1 до {n} через пробел').split()
# result=1
# for j in range(len(index_list)):        # перебор элементов с номерами позиций
#     a=int(index_list[j])-1
#     print (f'{result}*{int(list[a])}', end=' ')
#     result*=int(list[a])    
# print (f'= {result}')


# Реализуйте алгоритм перемешивания списка.

# import time
# list = [1,2,3,4,5,6,7,8,9,10,11]                 # задаем первоначальный список
# print (f'первоначальный список: {list}')
# digits_quantity=10                                          
# len_of_list = len(list)
# if len_of_list<10:                              # определяем количество цифр в длине списке и задаем число для использования в функции
#     digits_quantity=10
# elif len_of_list<100:
#     digits_quantity=100
# elif len_of_list<1000: 
#     digits_quantity=1000
# elif len_of_list<10000:
#     digits_quantity=10000
# def RandomNum (digits_quantity):                            # функция даёт рандомное число в диапазоне длины списка
#     a = 10000000 * time.perf_counter() % digits_quantity    # считается как последняя цифра или цифры в текущем времени эпохи  
#     return int(a)
# change_place=RandomNum(digits_quantity)
# new_list=[]                                                 # новый перемешанный список
# changed_indexex=[]                                          # список для сохранения измененных позиций
# for i in range(len(list)):                                                  # перемешивание списка при условии 
#     while change_place>len(list)-1 or change_place in changed_indexex:      # что рандомное число входит в диапазон длины списка
#         change_place = RandomNum(digits_quantity)                           # и оно отсутствует в списке уже измененных
#     new_list.append(list[change_place])
#     changed_indexex.append(change_place)
# print (f'перемешанный список:   {new_list}')
# print ()

# import random
# random.shuffle(list)
# print (f'с использованием встроенного метода shuffle {list}')