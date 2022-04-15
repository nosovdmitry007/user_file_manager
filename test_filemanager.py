from File_manager import new_folder, del_folder, copy_file
import shutil
import os

n1='123'
n2='1513jhbgdxc'
n3='gdskpl'
n4='5rfd'

def test_new_file1():
    new_folder(n1)
    assert os.path.exists(n1)


def test_new_file2():
    new_folder(n2)
    assert os.path.exists(n2)

def test_del_copy_file1():
    os.mkdir(n3)
    copy_file(n3, n4)
    assert os.path.exists(n2) and os.path.exists(n1)

def test_del_folder1():
    del_folder(n1)
    assert not os.path.exists(n1)

def test_del_folder2():
    del_folder(n2)
    assert not os.path.exists(n2)