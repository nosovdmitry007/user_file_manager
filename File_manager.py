import os
import shutil


# 1
def new_folder():
    os.mkdir(input('Введите название новой папки: '))


# 2
def del_folder():
    papka = input('Введите название папки/файла для удаления: ')
    if os.path.exists(papka):
        if '.' in papka:
            os.rmdir(papka)
        else:
            os.remove(papka)
    else:
        print('Нет такой папки/файла')


# 3
def copy_file():
    papka_old = input('Введите название папки/файла для копирования: ')
    papka_new = input('Введите новое название папки/файла: ')
    if os.path.exists(papka_old):

        if '.' in papka_old:
            shutil.copytree(papka_old, papka_new)
        else:
            shutil.copy(papka_old, papka_new)
    else:
        print('Нет такой папки/файла')


# 4
def soderg():
    print(os.listdir())


# 5
def papki():
    k = []
    for j in os.listdir():
        if not '.' in j:
            k.append(j)
    print(k)


# 6
def fail():
    k = []
    for j in os.listdir():
        if '.' in j:
            k.append(j)
    print(k)


# 7
def syst():
    print(os.uname())


# 8
def user():
    print(os.getlogin())


# 9
def my_victorina():
    from victorina import vict
    vict()


# 10
#def my_schet():
 #   from bank_schet import schet
 #   schet()


# 11
def smena():
    os.chdir(input('Введите имя новой дериктории: '))


while True:
    print('\n1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку');
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход.')

    choice = input('\nВыберите пункт меню ')
    if choice == '1':
        new_folder()
    elif choice == '2':
        del_folder()
    elif choice == '3':
        copy_file()
    elif choice == '4':
        soderg()
    elif choice == '5':
        papki()
    elif choice == '6':
        fail()
    elif choice == '7':
        syst()
    elif choice == '8':
        user()
    elif choice == '9':
        my_victorina()
   # elif choice == '10':
   #     my_schet()
    elif choice == '11':
        smena()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')