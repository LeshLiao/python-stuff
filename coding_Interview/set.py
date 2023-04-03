
# A set is a collection which is unordered, unchangeable*, and unindexed.
this_set = {"apple", "banana", "cherry"}
print(this_set)
this_set.add("orange")
print(this_set)

# Duplicates Not Allowed
this_set = {"apple", "banana", "cherry", "apple"}
print(this_set)

# difference
set_01 = {"apple", "banana", "cherry", "apple"}
set_02 = {"apple", "cherry", "apple"}
print(set_01.difference(set_02))
print(set_02.difference(set_01))

# intersection
print(set_01.intersection(set_02))
