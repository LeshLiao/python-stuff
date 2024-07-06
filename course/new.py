
# # string 3 times
# a = 'bbb' * 3
# print(a)

# # round
# print(round(5.4))

# # random
# import random
# print(random.randint(1, 10))


# # unpack a tuple
# person = ('Erik', 38, True)
# name, age, registered = person

# #

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


# def collatz(number):
#   if number == 1:
#     return 1
#   if (number % 2 == 0):
#     print(number // 2)
#     return collatz(number // 2)
#   else:
#     print(3 * number + 1)
#     return collatz(3 * number + 1)

# x = int(input())
# x = 3
# collatz(x)

# Forced keyword arguments

# def f(*, a, b):
#     print(a, b)

# f(a=1, b=2)


# def func1(a,b):
#   print(a,b)

# args = {'a': 2,'b':6}
# func1(**args)

def your_function(*,keyword,num):
  str = ''
  for i in range(num):
    str += ' '
  return str + keyword

print(your_function(keyword='abc',num=5))

add_one = lambda x: '<p>' + x + '</p>'
print(add_one('Hello'))

d = {'firstName':'Elon', 'lastName':'Musk', 'ID' : 123}

# Iterate Python dictionary keys
for k in d:
  print(k)

# Iterate dictionary values
for v in d.values():
  print(v)

# Iterate dictionary keys and values
for k,v in d.items():
  print(k,v)
