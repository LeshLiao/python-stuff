
# List

my_list = ['A', 'B', 'C']

for index, item in enumerate(my_list):
    print('index={} ,item={}'.format(index, item))

another_list = ['D', 'E', 'F']

for item1, item2 in zip(my_list, another_list):
    print('{} ,{}'.format(item1, item2))

mix_list = [1, '2', True]

print(mix_list)

print(str(mix_list[0]) + ', ' + mix_list[1] + ', ' + str(mix_list[2]))

print(mix_list[0], ', ', mix_list[1], ', ', mix_list[2])

print('{}, {}, {}'.format(mix_list[0], mix_list[1], mix_list[2]))

print(f"{mix_list[0]}, {mix_list[1]}, {mix_list[2]}")
