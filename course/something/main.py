from functionality import div
from othermodule import second

# print(div(9,3))
# second.myfunction()

# a = 'bbb' * 3
# print(a)

# spam = 0
# if spam == 1:
#   print('Hello')
# elif spam == 2:
#   print('Howdy')
# else:
#   print('Greetings')


# print(round(5.4))

# mystring = 'hello'
# mycopy = mystring
# mystring =  'world'
# print(mycopy)

# import random
# print(random.randint(1, 10))

# person = ('Erik', 38, True)
# name, age, registered = person

# print(name)
# print(age)
# print(registered)

# mine = {'The Godfather','Star Wars','The Dark Knight'}

# takuma = {'The Godfather','Pulp Fiction','Forrest Gump'}
# aybars = {'The Dark Knight','Fight Club','Pulp Fiction'}
# zoe = {'Star Wars','Forrest Gump','The Dark Knight'}

# differ1 = mine - takuma
# common1 = mine & takuma

# differ2 = mine - aybars
# common2 = mine & aybars

# differ3 = mine - zoe
# common3 = mine & zoe

# print(differ1)
# print(common1)

# print(differ2)
# print(common2)

# print(differ3)
# print(common3)

# dic = {
#   'frequency': '91.3',
#   'affiliations': 'National Public Radio',
#   'Format':'Public radio'
# }

# dic['owner'] = 'Wabash College'
# print(dic)

# del(dic['Format'])
# print(dic)

# mine = {'The Godfather','Star Wars','The Dark Knight'}
# takuma = {'The Godfather','Pulp Fiction','Forrest Gump'}
# aybars = {'The Dark Knight','Fight Club','Pulp Fiction'}
# zoe = {'Star Wars','Forrest Gump','The Dark Knight'}

# val = [x for x in range(1, 5) if x % 2 == 0]
# print(val)

# list2 = ['movie:' + x for x in ['The Godfather','Star Wars','The Dark Knight']]
# print(list2)

# list3 = [x + ' place' for x in ['The Godfather','Star Wars','The Dark Knight'] if len(x) == 3]
# print(list3)

# names = { "red", "blue", "green" }

# list3 = [x.upper().replace('E','U') for x in { "red", "blue", "green" }]
# print(list3)
# even == 2
def collatz(number):
  # print('number='+number)
  if number == 1:
    return

  if (number % 2 == 0):
    print(number // 2)
    return collatz(number // 2)
  else:
    print(3 * number + 1)
    return collatz(3 * number + 1)

x = int(input())
collatz(x)

# while True:
#   x = collatz(x)
#   if x == 1:
#     break
#   else:
#     collatz(x)