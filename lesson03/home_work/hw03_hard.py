# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
a = input('Введите задачу  в формате n x/y +/- n x/y: ')
if a == '0 + 0':
    print('0')
    exit()
zd_list = a.split()
#Дополняем лист в случае если не полный ввод (без целой и/или без дробной части):
if '/' in zd_list[0]:
    zd_list.insert(0,0)
if '/' not in zd_list[1]:
    zd_list.insert(1, '0/1')
if '/' in zd_list[3]:
    zd_list.insert(3, 0)
if len(zd_list) == 4:
    zd_list.append('0/1')
#Функция для вычисления наибольшего общего делителся для двух чисел
def naib_del(a, b):
    del_dr = []
    del_zn = []
    for i in range(1, abs(a) + 1):
        if a % i == 0:
            del_dr.append(i)
        if b % i == 0:
            del_zn.append(i)
    return max(set(del_dr) & set(del_zn))
#Определяем каждый знаменатель
znam = int(zd_list[1].split('/')[1])
znam1 = int(zd_list[4].split('/')[1])
#Вычисляем - числитель для каждой дроби (чтоб было без целой части)
if int(zd_list[0]) >= 0:
    chisl = int(zd_list[0]) * int(zd_list[1].split('/')[1]) + int(zd_list[1].split('/')[0])
else:
    chisl = int(zd_list[0]) * int(zd_list[1].split('/')[1]) - int(zd_list[1].split('/')[0])
if int(zd_list[3]) >= 0:
    chisl1 = int(zd_list[3]) * int(zd_list[4].split('/')[1]) + int(zd_list[4].split('/')[0])
else:
    chisl1 = int(zd_list[3]) * int(zd_list[4].split('/')[1]) - int(zd_list[4].split('/')[0])
#Определяем знак (сложение или вычитание) и как действовать в каждом из случаев
if '-' in str(zd_list[2]):
    chisl1 = -int(chisl1)
#Вычисляем общий знаменатель
zn_res = znam * znam1
#Вычисляем числитель конечного результата (без целой части пока, просто числитель)
ch_res = chisl * znam1 + chisl1 * znam
#Вычисляем целую часть и числитель дробной
if abs(ch_res) > zn_res and ch_res >= 0:
    cel = ch_res // zn_res
    dr = abs(ch_res % zn_res)
    if dr == 0:#Если остаток от деления числителя на знаменатель равен нулю, то результат будет целое число
        print(int(ch_res / zn_res))
        exit()
elif ch_res < 0:
    cel = abs(ch_res) // zn_res
    cel = - cel
    dr = abs(ch_res) % zn_res
    if dr == 0:
        print(int(ch_res / zn_res))
        exit()
    if cel == 0:
        cel = ''
        dr = - dr
else:
    dr = ch_res
    cel = ''
delitel = naib_del(dr, zn_res)#Определяем наибольший общий делитель
if int(dr) % int(zn_res) == 0:
    print(int(int(dr) / int(zn_res)))
else:
    print('{} {}/{}'.format(cel, int(dr / delitel), int(zn_res / delitel)))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

f = open('fruits.txt', 'r', encoding='utf-8')
list_1 = []
for fruit in f:
    if fruit == '\n':
        pass
    else:
        list_1.append(fruit.rstrip().strip('\ufeff'))
def let(fruit):
    letter = fruit[:1]
    f = open('file_{}'.format(letter), 'a')
    f.write(fruit + '\n')
for i in list_1:
    let(i)

