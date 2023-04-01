
# indexing   [start:stop:step]

name = "Larry Page"

first_name = name[0:5]
print(first_name)
second_name = name[6:]
print(second_name)

reversed_name = name[::-1]
print(reversed_name)

# slicing

website1 = "http://google.com"
website2 = "http://wikipedia.org"

my_slice = slice(7, -4)

print(website1[my_slice])
print(website2[my_slice])

# split

str1 = 'bear, cat, dog, elephant'
arr = str1.split(', ')
print(arr)
