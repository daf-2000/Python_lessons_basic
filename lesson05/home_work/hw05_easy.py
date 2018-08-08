# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
#Первый скрипт:
import os
for i in range(1,10):
   dir_path = os.path.join(os.getcwd(), '{}_dir'.format(i))
   try:
      os.mkdir(dir_path)
      print('директория dir_{} создана'.format(str(i)))
   except FileExistsError:
      print('директория {} уже существует'.format(dir_path))

#Второй скрипт:
import os
for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), '{}_dir'.format(str(i)))
    if os.path.exists(dir_path):
        os.rmdir(dir_path)
        print('Директория {}_dir удалена'.format(str(i)))
    else:
        print('Такой папки не существует {}'.format(dir_path))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
for i in os.listdir('.'):
    if os.path.isdir(i):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil
shutil.copy(sys.argv[0], sys.argv[0] + '.copy')