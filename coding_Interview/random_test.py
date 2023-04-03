import random

x = random.randint(1, 6)
y = random.random()

print(x)
print(y)

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
print(cards)
random.shuffle(cards)
print(cards)
