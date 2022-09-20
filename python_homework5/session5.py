# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# txt = 'абвг аг asd asd asd абв абвгд'.split()
# data = [x for x in txt]
# txt = list (filter(lambda x: not x.count('абв'), data))
# print(txt)

# txt = 'абвг аг asd asd asd абв абвгд'.split()
# res = list(i for i in txt if 'абв' not in i)
# print (res)

# или вариант удалять искомый элемент через remove проходя с конца списка
# txt = 'абвг аг asd asd asd абв абвгд'.split()
# for i in reversed(txt):
#     if i.count('абв'):
#         txt.remove(i)      
# print (txt)



# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

#                   2 игрока
# turn = -1
# conf_amount = 2021
# player1 = 0
# player2 = 0
# countt = random.randint(1,2)
# print(f'первый ход игрока {countt}')
# while conf_amount > 0:
#     while turn < 1 or turn > 28 or turn > conf_amount:
#         turn = int(input(f'\n ход игрока {countt} (от 1 до 28 конфет, остаток {conf_amount}) - '))
#     conf_amount -= turn
#     if countt == 1:
#         player1 += turn
#         countt = 2
#     elif countt == 2:
#         player2 += turn
#         countt = 1
#     turn = -1
#     print (f'player1 - {player1} player2 - {player2} конфет осталось {conf_amount}')
# if countt == 2: 
#     player1 +=player2
#     player2 = 0
# else:
#     player2 +=player1
#     player1 = 0
# print (f'****player1 {player1} player2 {player2} конфет осталось {conf_amount}****')


#                               игра с ботом
# import random
# from turtle import clear
# turn = -1
# conf_amount = 2021
# player1 = 0
# player2 = 0
# countt = random.randint(1,2)
# print('\n', f'первый ход игрока {countt}')
# while conf_amount > 0:
#     while turn < 1 or turn > 28 or turn > conf_amount:
#         if countt == 1: 
#             turn = int(input(f'\n ход игрока {countt} (от 1 до 28 конфет, остаток {conf_amount}) - '))
#         else:
#             turn = random.randint(1, 28)
#             if conf_amount < 29:
#                 turn = conf_amount
#             if turn <= conf_amount: 
#                 print (f'\n ход игрока {countt} (от 1 до 28 конфет, остаток {conf_amount}) - {turn}')
#     conf_amount -= turn
#     if countt == 1:
#         player1 += turn
#         countt = 2
#     elif countt == 2:
#         player2 += turn
#         countt = 1
#     turn = -1
#     print (f' счёт player1 - {player1} player2 - {player2} \n (конфет осталось {conf_amount})')
# if countt == 2: 
#     player1 +=player2
#     player2 = 0
# else:
#     player2 +=player1
#     player1 = 0
# print (f'********итого player1 {player1} player2 {player2} конфет осталось {conf_amount}********')

#                       # бот с интеллектом
# import random
# turn = -1
# conf_amount = 2021
# player1 = 0
# player2 = 0
# countt = random.randint(1,2)
# # def bot_calc(conf_amount):
# #     turn = random.randint(1, 28)
# #     if conf_amount < 29:
# #         turn = conf_amount
# #     elif conf_amount < 56:
# #         turn = conf_amount - 29
# #     else:
# #         turn = int(28 - 812 / conf_amount)
# #     return turn
# print('\n', f'первый ход игрока {countt}')
# while conf_amount > 0:
#     while turn < 1 or turn > 28 or turn > conf_amount:
#         if countt == 1: 
#             turn = int(input(f'\n ход игрока {countt} (остаток {conf_amount}) - '))
#         else:
#             # bot_calc(conf_amount)
#             if conf_amount < 29:
#                 turn = conf_amount
#             elif conf_amount < 56:
#                 turn = conf_amount - 29
#             else:
#                 turn = int(28 - 812 / conf_amount)   
#         if turn <= conf_amount: 
#             print (f'\n ход игрока {countt} (остаток {conf_amount}) - {turn}')            
#     conf_amount -= turn
#     if countt == 1:
#         player1 += turn
#         countt = 2
#     elif countt == 2:
#         player2 += turn
#         countt = 1
#     turn = -1
#     print (f' счёт player1 - {player1} player2 - {player2} \n (конфет осталось {conf_amount})')
# if countt == 2: 
#     player1 +=player2
#     player2 = 0
# else:
#     player2 +=player1
#     player1 = 0
# print (f'********итого player1 {player1} player2 {player2} конфет осталось {conf_amount}********')


#                           # играют два бота с интеллектом, выигрывает тот, кто ходит первым
# import random
# turn = -1
# conf_amount = 2021
# player1 = 0
# player2 = 0
# countt = random.randint(1,2)
# print('\n', f'первый ход игрока {countt}')
# input('')
# while conf_amount > 0:
#     while turn < 1 or turn > 28 or turn > conf_amount:
#         if conf_amount < 29:
#             turn = conf_amount
#         elif conf_amount < 56:
#             turn = conf_amount - 29
#         else:
#             turn = int(28 - 812 / conf_amount)   
#         if turn == 0:
#             turn += 1
#         if turn <= conf_amount: 
#             print (f'\n ход игрока {countt} (остаток {conf_amount}) - {turn}')            
#     conf_amount -= turn
#     if countt == 1:
#         player1 += turn
#         countt = 2
#     elif countt == 2:
#         player2 += turn
#         countt = 1
#     turn = -1
#     print (f' счёт player1 - {player1} player2 - {player2} \n (конфет осталось {conf_amount})')
# if countt == 2: 
#     player1 +=player2
#     player2 = 0
# else:
#     player2 +=player1
#     player1 = 0
# print (f'********итого player1 {player1} player2 {player2} конфет осталось {conf_amount}********')



# Создайте программу для игры в ""Крестики-нолики"".

# def prnt_matr(lst):
#     print("\033c")
#     for i in range (9):
#         print (lst [i], end = '  ')
#         if i == 2 or i == 5:
#             print('\n')
# def check_win(lst):
#     win = 0
#     if lst[0] == lst[1] and lst[1] == lst[2] or \
#     lst[3] == lst[4] and lst[4] == lst[5] or \
#     lst[6] == lst[7] and lst[7] == lst[8] or \
#     lst[0] == lst[3] and lst[3] == lst[6] or \
#     lst[1] == lst[4] and lst[4] == lst[7] or \
#     lst[2] == lst[5] and lst[5] == lst[8] or \
#     lst[0] == lst[4] and lst[4] == lst[8] or \
#     lst[2] == lst[4] and lst[4] == lst[6]:
#         if player == 1: win = 2
#         elif player == 2: win = 1    
#     return win
# lst = ['\u00B9','\u00B2',"\u00B3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"]
# player = 1
# countt_turn = 0
# while check_win(lst) != 1 and countt_turn < 9:
#     countt_turn += 1
#     prnt_matr(lst)
#     turn = int(input(f'\n\nходит игрок {player} '))
#     while lst[turn-1] == 'X' or lst[turn-1] == 'O':
#         turn = int(input(f'\n\nходит игрок {player} '))
#     if player == 1:
#         lst [turn - 1] = 'X'
#         player = 2
#     elif player == 2:
#         lst [turn - 1] = 'O'
#         player = 1 
# if countt_turn < 9: 
#     prnt_matr(lst)
#     print(f'\n\nвыиграл игрок {player}')
# else:
#     print('ничья')



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def packing(lst):       
#     countt = 1
#     tmp=' '
#     for i in lst:
#         countt = 1
#         countt2 = 0
#         tmp=' '        
#         for j in i:
#             if countt2 == 0:
#                 tmp = j
#             else:
#                 if j != tmp:
#                     lst1.append(countt)
#                     lst1.append(tmp)
#                     tmp = j
#                     countt = 1   
#                 elif j == tmp:
#                     countt += 1
#             if countt2 == len(i)-1: 
#                 lst1.append(countt)
#                 lst1.append(tmp)
#             countt2 += 1
#         lst1.append(1)
#         lst1.append(' ')
#     return lst1
# def unpacking(lst1):
#     for i in lst1:
#         if type(i) is int: 
#             tmp = i
#         elif type(i) is str:
#             for j in range(tmp):
#                 lst2.append(i)
#     return ''.join(lst2)            
# with open('fileinput.txt', 'r') as reading:
#     lst = reading.readlines()
# lst = lst[0].split()
# print(lst)
# lst1 = []
# lst2 = []      
# print(packing(lst))
# print(unpacking(lst1))
# with open('fileoutput.txt', 'w') as writing:
#     writing.writelines(lst2)