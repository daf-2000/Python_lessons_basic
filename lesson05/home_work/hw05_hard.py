# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import os
import sys
import shutil
import subprocess
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm < file_name > - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def rm():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(file_path):
        if input('Вы уверены? Y/N: ') in ('Y', 'y'):
            os.remove(file_path)
            print('Файл {} удален'.format(file_path))
        else:
            print('Операция отменена')
    else:
        print('Такаго файла не существует')

def cd():
    path = dir_name
    if os.path.isdir(dir_name):
        if os.name == 'nt':
            subprocess.call(['cmd', '/k', 'cd {}'.format(dir_name)])
        if os.name =='posix':
            subprocess.call(['cd {}'.format(dir_name)])
            os.chdir(dir_name)
    else:
        print('Такого пути не существует')
def ls():
    os.getcwd()

def cp():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(file_path):
        if os.path.isfile(file_path + '.copy'):
            print('Копия уже существует')
            return
        else:
            shutil.copy(file_path, file_path + '.copy')
            print('Создан файл {}'.format(file_path + '.copy'))
    else:
        print('Такого файла не существует')

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
print(os.getcwd())