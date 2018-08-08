import os
import shutil
def cd(a):
    dir_path = os.path.join(os.getcwd(), a)
    if os.path.exists(dir_path):
        os.chdir(dir_path)
        print('Текущая директория {}'.format(dir_path))
        return
    else:
        print('Нет такой директории')
        return
def ls():
    for i in os.listdir('.'):
        print(i)
def rm(a):
    dir_path = os.path.join(os.getcwd(), a)
    if os.path.exists(dir_path):
        shutil.rmtree(a, ignore_errors=True)#Выбрал этот вариант удаления, так как os.rmdir() не позволяет удалять пустые папки
        print('Удалена директория {}'.format(a))
    else:
        print('Нет такой директории')
        return
def mkdir(a):
    dir_path = os.path.join(os.getcwd(), a)
    os.mkdir(dir_path)
    print('Создана директория {}'.format(dir_path))
def uptree():
    dir_path = '\\'.join(os.getcwd().split('\\')[:-1])#Путь до папки вверх = полный путь до текущей папки минус имя текущей(последней в пути)
    os.chdir(dir_path)
    print('Текущая директория: {}'.format(dir_path))