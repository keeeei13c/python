
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

def test_func(x,l=[]):
  l.append(x)
  return l

y = [1,2,3]
r = test_func(100,y)
print(r)
