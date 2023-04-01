
# before using walrus
walrus = False
print(walrus)


# after using walrus
print(walrus := True)


# before using walrus
food_list = list()
while True:
    new_food = input("What food do you like?")
    if new_food == 'quit':
        break
    food_list.append(new_food)

print(food_list)


# after using walrus
beverage_list = list()
while (new_item := input("What beverage do you like?")) != 'quit':
    beverage_list.append(new_item)

print(beverage_list)
