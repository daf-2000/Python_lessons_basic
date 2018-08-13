# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


## -*- coding: utf-8 -*-
import re
list_wor = list()
list_h = list()
list_workers = list()
workers = open('workers', 'r', encoding="utf-8")
hours = open('hours_of', 'r', encoding="utf-8")
#re.split(pattern, string, maxsplit=0, flags=0)
def to_list(filename):
    list_class = list()
    for line in filename:
        if line.startswith('Имя'):
            continue
        else:
            list_class.append(re.split('\s+', line))
    return list_class

list_wor = to_list(workers)
list_h = to_list(hours)
for i in list_wor:
    for y in list_h:
        if y[0] in i and y[1] in i:
            i.append(y[2])
for i in list_wor:
    list_workers.append(list(filter(lambda i: i != '', i)))
for i in list_workers:
    i.append('')
#print(list_workers)
class workers_class:
    def __init__(self, name, surname, sal, pos, norm, worked_out, wage ):
        self.name = name
        self.surname = surname
        self.sal = sal
        self.pos = pos
        self.norm = norm
        self.worked_out = worked_out
        self.wage = wage
    def wage_c(self):
        if int(self.norm) >= int(self.worked_out):
            self.wage = int(self.worked_out)/int(self.norm)*int(self.sal)
        if int(self.norm) < int(self.worked_out):
            self.wage = (int(self.sal)/int(self.norm)*(int(self.worked_out) - int(self.norm))*2 + int(self.sal))
    def get_full_info(self):
        return print(self.name + ' ' + self.surname + ' ' + str(int(self.wage)))

for i in range(len(list_workers)):
    al = workers_class(*list_workers[i])
    al.wage_c()
    al.get_full_info()