#только цифры
def filtr1(list1):
    return list(filter(str.isdigit, list1))


#Из списка чисел оставить только нечетные
def filtr2(list2):
    return list(filter(lambda x: x % 2 == 1, list2))

#Из списка чисел оставить только четные
def filtr3(list3):
    return list(filter(lambda x: x % 2 == 0, list3))

#Из списка слов оставить только те, у которых количество букв больше двух:
def filtr4(list4):
    return list(filter(lambda x: len(x) > 2, list4))

def map1(map1):
    return list(map(lambda x: x * 2 + 3, map1))

def map2(map2):
    return list(map(lambda x: x ** 2+99, map2))

def map3(map3):
    return list(map(lambda x: x ** 2-100, map3))

def map4(map4):
    return list(map(lambda x: x*515/15, map4))

def sort1(numbers):
  return sorted(numbers)

import math

def pi1():
  return float(math.pi)

def sqrt1(nump):
  return math.sqrt(nump)

def pow1(nump1,nump2):
  return math.pow(nump1,nump2)

def hypot1(nump1,nump2):
  return math.hypot(nump1,nump2)