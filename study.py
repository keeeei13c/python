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

