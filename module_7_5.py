import time
import os

"""1 Используйте os.walk для обхода каталога, путь к которому указывает переменная directory"""


def scan_dir(directory):
    for root, dirs, fil in os.walk(directory):
        print(f'Обход каталога, путь directory : {root}, {dirs}, {fil}')


def scan_file(directory):
    """Примените os.path.join для формирования полного пути к файлам"""
    files = os.listdir(directory)
    if os.path.exists(directory):
        os.chdir(directory)
        now = os.getcwd()
        for file in files:
            file_path = os.path.join(now, file)
            """Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла"""
            recent_changes = (os.path.getmtime(file_path))
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(recent_changes))
            """Используйте os.path.getsize для получения размера файла."""
            file_size = os.path.getsize(file_path)
            """Используйте os.path.dirname для получения родительской директории файла."""
            parent_dir = os.path.dirname(file_path)
            print(f'Обнаружен файл: {file},\n'
                  f' Путь: {file_path},\n'
                  f' Размер: {file_size} байт, Время изменения: {formatted_time},\n'
                  f' Родительская директория: {parent_dir}')

def check_path(text='Введите путь'):
    while True:
        way_dir = (input(f'{text}'))
        if os.path.exists(way_dir):
             return way_dir
             break
        else:
            print('Такой путь не найден ')
            continue
def ent_path():
    while True:
        entr = (input('Введите 1  для обхода каталога\n'
                      'Введите 2  для обхода данных о файлов каталога\n'
                      'Введите 3 для обхода текущего каталога\n'
                      'Введите 4 для обхода данных о файлов текущего каталога :  '))
        if int(entr) == 1:
            text = ('Введите путь к директории : ')
            scan_dir(check_path(text))
            break
        if int(entr) == 2:
            text = ('Введите путь к файлу : ')
            scan_file(check_path(text))
            break
        if int(entr) == 3:
            scan_dir('.')
            break
        if int(entr) == 4:
            text = ('.')
            scan_file('.')
            break
        if int(entr) != 1 or 2:
            print('Выберете нужную цифру')
            continue

ent_path()
print()
print(' """ THE END """ ')
