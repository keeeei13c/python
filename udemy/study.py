# days = ['Mon','Tue','Wed']
# fruits = ['apple', 'banana', 'orange']
# drinks = ['coffee','tea','beer']

# for day, fruit, drink in zip(days, fruits, drinks):
#   print(day,fruit,drink)

# d = {'x': 100, 'y' : 200, 'z':300}
# for k,v in d.items():
#   print(k,':',v)

# def say_something():
#   s = 'hi'
#   return s

# result = say_something()
# print(result)

# def what_is_this(color):
#   if color == 'red':
#     return 'tomato'
#   elif color == 'green':
#     return 'green pepper'
#   else:
#     return 'I don\'t know'

# what_is_this('red')
# what_is_this('green')
# what_is_this('yellow')

# print()


# def add_num(a,b):
#   return a + b

# def menu(entree,drink,dessert):
#   print('entree =' ,entree)
#   print('drink = ',drink)
#   print('dessert = ',dessert)

# menu(entree='beef',drink='beer',dessert='ice')

# def test_func(x,l=[]):
#   l.append(x)
#   return l

# y = [1,2,3]
# r = test_func(100,y)
# print(r)

# def menu(entree,drink,dessert):
#   print(entree)
#   print(drink)
#   print(dessert)

# menu('beef','beer','ice')

# def say_something(*args):
#   for arg in args:
#     print(arg)

# say_something('Hi','mike','thank you')

# def menu(food, *args, **kwargs):
#   print(food)
#   print(args)
#   print(kwargs)

# menu('banana','apple','orange','tomato',entree='beef',drink='coffee')

# a = {
#   'entree':'beef',
#   'drink':'ice coffee',
#   'dessert':'ice'
# }

# menu(**a)

# def outer(a,b):
#   def inner():
#     return a + b

#   return inner

# f = outer(1,2)
# r = f()
# print(f)

# def print_info(func):
#   def wrapper(*args, **kwargs):
#     print('start')
#     result = func(*args, **kwargs)
#     print('end')
#     return result


# def add_num(a,b):
#   return a + b

# print('start')
# r = add_num(10,20)
# print('end')

# print(r)


"""
lambda
"""
# l = ['Mon','Tue','wed','Thu','fri','sat','Sun']

# def change_words(words, func):
#   for word in words:
#     print(func(word))

# # sample_func = lambda word: word.capitalize()
# change_words(l, lambda word: word.capitalize())

"""
generater
"""
# l = ['Good morning','Good afternoon','Good night']

# for i in l:
#   print(i)

# print('##############')

# def greeting():
#   yield 'Good morning'
#   yield 'Good afternoon'
#   yield 'Good night'

# for g in greeting():
#   print(g)

# g = greeting()
# print(next(g))
# print(next(g))
# print(next(g))

# t = (1,2,3,4,5)

# r=[]
# for i in t:
#   r.append(i)
# r = [i for i in t if i % 2 == 0]
# print(r)

# w = ['mon','tue','wen']
# f = ['coffee','milk','water']

# d = {}
# for x,y in zip(w,f):
#   d[x] = y

# print(d)

# d = {x:y for x,y in zip(w,f)}


"""
import文
"""
# import lesson_package.utils

# from lesson_package import utils
# from lesson_package.talk import human
# # r = utils.say_twice('hello')

# # print(r)
# print(human.sing())


"""
from lesson_package.utils import say_twice 

r = say_twice('hello')

print(r)

でも呼び出せるが好まれていない
どこから関数を呼び出しているかわかりにくいため
"""
# import builtins

# ranking = {
#   'A': 100,
#   'B': 85,
#   'C':97
# }
# print(sorted(ranking , key=ranking.get,reverse=True))

# from termcolor import colored

# print('test')

# print(colored('test','magenta'))
"""
__name__ と __main__ 理解あまりできていない
別ファイルからimport するとき勝手に作動しないように書いておくおまじない

if __name__ == __main__:

"""
# import config

# print('config',__name__)
# print(__name__)

# class Person(object):
#   def __init__(self, name='Mike'):
#     self.name = name

#   def say_something(self):
#     print('I am {}. hello'.format(self.name))
#     self.run(10)

#   def run(self,num):
#     print('run:' * num)

#   def __del__(self):
#     print('good bye')

# person = Person('johnson')
# person.say_something()

# del person
# print('#########')

# class Car(object):
#   def __init__(self,model=None):
#     self.model = model
#   def run(self):
#     print('run')
# class ToyotaCar(Car):
#   def run(self):
#     print('fast')

# class TeslaCar(Car):
#   def run(self):
#     print('super fast')

#   def auto_run(self):
#     print('auto run')

# tesla_car = TeslaCar('Model S')
# print(tesla_car.model)
# tesla_car.run()
# tesla_car.auto_run()


# class A(object):
#   pass

# a = A()
# a.name = 'Mike'
# a.age = 20
# print(a.name,a.age)

# class Person(object):
#   def talk(self):
#     print('talk')

# class Car(object):
#   def run(self):
#     print('run')

# class PersonCarRobot(Person,Car):
#   def fly(self):
#     print('fly')

# person_car_robot = PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()
# person_car_robot.fly()


# class Person(object):

#   kind = 'human'

#   def __init__(self):
#     self.x = 100

# a = Person()
# print(a.kind)
# b = Person
# print(b.kind)

# class Word(object):

#   def __init__(self,text):
#     self.text = text

#   def __str__(self):
#      return 'Word!!!!!!!!!!'

#   def __len__(self):
#     return len(self.text)
#   def __add__(self):
#     self.text.lower()+ word.text.lower()
# w = Word('testssss')
# print(len(w))


# f = open('test.txt' , 'w')
# f.write('Test\n')
# f.close()

# s = """\
#      AAA
#      BBB
#      CCC
#      DDD
#     """

# with open('test.txt','w') as f:
#     f.write(s)

# with open('test.txt', 'r') as f:
#     print(f.read())

#     while True:
#         chunk = 2
#         line = f.read(chunk)
#         print(line)
#         if not line:
#             break


"""
seekの使い方
"""
# with open('test.txt', 'r') as f:
#     print(f.tell())
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))
#     f.seek(14)
#     print(f.read(1))
#     f.seek(20)
#     print(f.read(1))

# s = """\
#      AAA
#      BBB
#      CCC
#      DDD
#     """

# with open('test.txt','w+') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

# import string

# with open ('design/email.txt') as f:
#   t = string.Template(f.read())
# contents = t.substitute(name='Mike', contents='How are you')
# print(contents)


# import csv
# with open('test.csv', 'w') as csv_file:
#     fieldnames = ['Name', 'Count']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name': 'A', 'Count': 1})
#     writer.writerow({'Name': 'C', 'Count': 2})


# with open('test.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['Name'],row['Count'])

# import os
# import pathlib
# import glob
# import shutil

# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('design'))
# os.symlink('renamed.txt','symlink.txt')
# os.mkdir('test_dir')
# os.rmdir('test_dir')

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# os.mkdir('test_dir/test_dir2/test_dir3')

# print(os.listdir('test_dir/test_dir2'))

# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# print(glob.glob('test_dir/test_dir2/*'))
# shutil.rmtree('test_dir')

import tarfile


"""
オイラーの等式を書きたかった
"""
# import math
# r = math.pi

# e = math.e
# i = -1
# p = math.pi

# print(e^i*p + 1 )


#Big O notation Example

#0(log(n))

# def func2(n):
#     if n <= 1:
#         return
#     else:
#         print(n)
#         func2(n/2)
# func2(10)


#0(n)
# def func3(numbers):
#   for num in numbers:
#     print(num)

# func3([1,2,3,4])


#(n * log(n))

# def func4(n):
#   for i in range(int(n)):
#     print(i , end=' ')
#   print()

#   if n <= 1:
#     return
#   func4(n/2)

# func4(10)

# 0(n**2)
# def func5(numbers):
#   for i in range(len(numbers)):
#     for j in range(len(numbers)):
#       print(numbers[i],numbers[j])
#     print()

# func5([1,2,3,4,5,6,7,8,9,10])

#sort 
# l = [(1,'Mike'),(5,'Rina'),(2,'Bill'),(4,'Emily'),(2,'June')
# ]

# def stable(l):
#   l[1], l[2] = l[2],l[1]
#   l[2], l[4] = l[4],l[2]

# print(stable())


"""bogo_sort"""

# import random

# def in_order(numbers):
#   return (i for in range(len(numbers[])))
  # for i in range(len(numbers)-1):
  #   if numbers[i] > numbers[i+1]:
  #     return False
  # return True


# def bogo_sort(numbers):
#   while not in_order(numbers):
#       random.shuffle(numbers)
#   return numbers

# if __name__ == '__main__':
#     print(bogo_sort([1,5,6,3,2]))

