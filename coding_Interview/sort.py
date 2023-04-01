
students = [("Apple", "70"), ("Banana", "60"), ("Orange", "80")]

my_sort = sorted(students, reverse=True)

for item in my_sort:
    print(item)


print("==========")


def grade(grades): return grades[1]


second_sort = sorted(students, key=grade)

for index, item in enumerate(second_sort):
    print("index=" + str(index))
    print(item[0])
    print(item[1])
