
# A set is a collection which is unordered, unchangeable*, and unindexed.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# difference
set_01 = {"apple", "banana", "cherry", "apple"}
set_02 = {"apple", "cherry", "apple"}
print(set_01.difference(set_02))
print(set_02.difference(set_01))

# interseciton
print(set_01.intersection(set_02))
