import os
def folder_save_to_file(spisok=os.listdir()):
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


