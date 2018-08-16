#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

from tabulate import tabulate
import random
import sys
counter_pl = 0
counter_pc = 0
a = True
def karta():#Функция генерирующая карту для игрока и компьютера
    list_card = list()
    while len(list_card) < 15:
        k = random.randint(1,90)
        if k in list_card:
            continue
        else:
            list_card.append(k)
    list_card = [list_card[i:i + 5] for i in range(0, len(list_card), 5)]#разделяем числа на 3 листа в одном
    for i in range(len(list_card)):
        list_card[i] = sorted(list_card[i])
        for _ in range(4):
            list_card[i].insert(random.randint(1,9), '  ' )#Добавляем пробелы в карточку
    return list_card
def begin():#Функция обнуления карточек и счетчиков в случае повторного начала игры
    global m
    global player_c
    global pc_c
    global step_list
    global counter_pc
    global counter_pl
    m = True
    player_c = karta()
    pc_c = karta()
    step_list = [i for i in range(1, 91)]
    counter_pl = 0
    counter_pc = 0
begin()
def turn_new(step_list):#Функция определяющая следующее случайное число при выборе боченка
    r = random.choice(step_list)
    step_list.remove(r)
    return r
def turn_player(player_c, turn_num):#Функция ход игрока
    global counter_pl
    global m#Переменная используется для определения - правильный ли выбор сделал игрок
    l = False
    sel = input('Выпало число {}. Y - удалить число {} из карточки/любая клавиша + ввод - продолжить. Ваш выбор: '.format(turn_num,turn_num))
    for i in range(len(player_c)):
        if turn_num in player_c[i] and sel not in ['Y', 'y']:
            m = False
        if turn_num in player_c[i]:
            player_c[i][int(player_c[i].index(turn_num))] = '  '
            counter_pl += 1
            l = True
    if l == False and sel in ['Y', 'y']:
        m = False
    else:
        l = False
    return
def turn_pc(pc_c,turn_num):#функция ход компьютера
    global counter_pc
    for i in range(len(pc_c)):
        if turn_num in pc_c[i]:
            pc_c[i][int(pc_c[i].index(turn_num))] = '  '
            counter_pc += 1
    return
def results(player_c, pc_c, turn_num):#функция показывающая боченок и карточки каждый ход
    print('Выпало число {}\n\n'.format(turn_num))
    print('Ваша карточка\n {}'.format(tabulate(player_c)))
    print('Карточка компьютера\n {}'.format(tabulate(pc_c)))
def question():
    i = input('Сыграем еще раз Y/N?')
    if i in ['y', 'Y']:
        begin()
    else:
        print('Пока!')
        sys.exit(0)
while a == True:
    if m == False:
        print('Вы проиграли')
        question()
    if counter_pl == 15 and counter_pc != 15:
        print('Вы выйграли, УРААА!!!')
        question()
    if counter_pl != 15 and counter_pc == 15:
        print('Вы проиграли')
        question()
    if counter_pl == 15 and counter_pc == 15:
        print('Ничья!!!')
        question()
    turn_num = turn_new(step_list)
    results(player_c, pc_c, turn_num)
    turn_player(player_c, turn_num)
    turn_pc(pc_c, turn_num)

