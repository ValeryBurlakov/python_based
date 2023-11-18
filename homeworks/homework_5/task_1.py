# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# file_path = "C:/Users/User/Documents/example.txt"
import os
# file_path = 'file_in_current_directory.txt'
#
# def get_file_info(file_path):
#     # Разделяем путь на директорию и имя файла
#     file_dir, file_name = os.path.split(file_path)
#
#     # Разделяем имя файла на имя и расширение
#     name, extension = os.path.splitext(file_name)
#
#     # Возвращаем кортеж с результатами
#     return file_dir, name, extension
#
#
# print(get_file_info(file_path))

# ('C:/Users/User/Documents/', 'example', '.txt')


def get_file_info(file_path):
    # Разделяем путь на директорию и имя файла
    filedir, filename = os.path.split(file_path)
    # метод удаляет последний слеш, возвращаем чтобы удовлетворить автотестеров
    if filedir != '':
        filedir += '/'

    # Разделяем имя файла на имя и расширение
    name, extension = os.path.splitext(filename)

    # бездушная машина не воспринимает расширение так как она думает что файл без расширения это имя файла, но у
    # автотестеров какого-то хера это формат файла, поменяли местами
    if not extension.startswith('.'):
        extension = filename
        name = ''
        extension = '.' + extension

    # Возвращаем кортеж с результатами
    return filedir, name, extension


file_path = 'C:/Users/User/Documents/example.txt' # ('C:/Users/User/Documents/', 'example', '.txt')
print(get_file_info(file_path))
file_path = '/home/user/data/file' # ('/home/user/data/', '', '.file')
print(get_file_info(file_path))
file_path = 'D:/myfile.txt' # ('D:/', 'myfile', '.txt')
print(get_file_info(file_path))
file_path = 'C:/Projects/project1/code/script.py' # ('C:/Projects/project1/code/', 'script', '.py')
print(get_file_info(file_path))
file_path = '/home/user/docs/my.file.with.dots.txt' # ('/home/user/docs/', 'my.file.with.dots', '.txt')
print(get_file_info(file_path))
file_path = 'file_in_current_directory.txt'  # ('', 'file_in_current_directory', '.txt')
print(get_file_info(file_path))

# ('C:/Users/User/Documents/', 'example', '.txt')
# ('/home/user/data/', '', '.file')
# ('D:/', 'myfile', '.txt')
# ('C:/Projects/project1/code/', 'script', '.py')
# ('/home/user/docs/', 'my.file.with.dots', '.txt')
# ('', 'file_in_current_directory', '.txt')