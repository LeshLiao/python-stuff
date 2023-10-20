
str = "CAB"

# len()
len(str)
print(len(str))

# sorted()
sorted(str)
print(sorted(str))

# join()
str = ''.join(sorted(str))
print(str)

# max()
a = 1
b = 2
a = max(a,b)
print(a)

# set()
nums = [2,3,2,1]
nums = set(nums)
print(nums)

# defaultdict()
from collections import defaultdict
defaultdict_demo = defaultdict(int)
print(defaultdict_demo[3])
defaultdict_demo[3] = 300
print(defaultdict_demo[3])