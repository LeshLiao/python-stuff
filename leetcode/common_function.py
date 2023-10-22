
str = "CAB"

# len()
len(str)
print(len(str))

# sorted()
sorted(str)
print(sorted(str))

# reverse() in-place
nums = [1,2,3]
nums.reverse()
print(nums)

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

# sort sub list
nums = [5,4,3,2,1]
nums[2:] = sorted(nums[2:])
print(nums)

# swap 2 value
nums = [1,2,3,4,5]
print(nums)
nums[0], nums[4] = nums[4], nums[0]
print(nums)