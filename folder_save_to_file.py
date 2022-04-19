import os
from bank_schet import  open_file_reading
def folder_save_to_file(spisok):
    file=['files: ']
    dris=['dirs: ']
    for j in spisok:
        if '.' in j:
            file.append(j)
        else:
            dris.append(j)
    put = file + dris

    with open('listdir.txt', 'w') as expense:
        expense.write(str(" ".join(put)))
    return 'Файл записан\nВ папке находятся файлы:\n'+open_file_reading('listdir.txt')


