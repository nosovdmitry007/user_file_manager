from module_for_tests import filtr1, filtr2, filtr3, filtr4, map1, map2, map3, map4, sort1, sqrt1, pow1, hypot1

def test_filtr1():
    for i in filtr1(['one', 'two', 'list', '', 'dict', '100', '1', '50']):
        assert int(i)/2 > -99999999999

def test_filtr2():
    assert filtr2([10, 111, 102, 213, 314, 515])[0]%2==1

def test_filtr3():
    for i in filtr3([10, 111, 102, 213, 314, 515]):
        assert i % 2 == 0

def test_filtr4():
    for i in filtr4(['one', 'two', 'list', '','df','d', 'dict']):
        assert len(i) > 2

numbers = [10, 15, 21, 33, 42, 55]

def test_map1():
    d = 0
    for i in map1(numbers):
        assert i == numbers[d] * 2 + 3
        d += 1

def test_map2():
    d = 0
    for i in map2(numbers):
        assert i == numbers[d] ** 2 + 99
        d += 1

def test_map3():
    d = 0
    for i in map3(numbers):
        assert i == numbers[d] ** 2 - 100
        d += 1


def test_map4():
    d = 0
    for i in map4(numbers):
        assert i == numbers[d] * 515 / 15
        d += 1

def test_sort1():
  z=sort1([10, 15, 21, 33, 42, 55])
  for i in range(1,len(z)):
    assert z[i-1]<=z[i]

def test_sort2():

  z=sort1(['f','a','g','q','j'])
  for i in range(1,len(z)):
    assert z[i-1]<=z[i]

import numpy

def test_sqrt1():
  assert sqrt1(2)==numpy.sqrt(2)


def test_pow1():
  assert pow1(2,3)==2**3

def test_hupot1():
  x=2
  y=3
  assert numpy.sqrt(x * x + y * y)==hypot1(x,y)

def test_hupot2():
  x=22
  y=39
  assert numpy.sqrt(x * x + y * y)==hypot1(x,y)

def test_hupot3():
  x = 26
  y = 35
  assert numpy.sqrt(x * x + y * y) == hypot1(x, y)