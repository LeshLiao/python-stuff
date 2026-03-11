
from collections import defaultdict


# nums = ['A','B','C']

# for i, num in enumerate(nums):
#   print(str(i) + ":" + str(num))

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

# graph = defaultdict(list)

# for course, pre in prerequisites:
#   graph[course].append(pre)

# print(graph)


# class Solution(object):
#     def test(self, nums):
#         max_val = -1  # avoid using 'max' because it's a built-in function name

#         def checkMax(num):
#             nonlocal max_val  # this tells Python to use the outer max_val
#             if num > max_val:
#                 max_val = num

#         for num in nums:
#             checkMax(num)

#         return max_val

# s1 = Solution()
# print(s1.test([3,6, 2, 4]))  # Output: 4


# def longest_numbers(nums):
#     num_sets = set(nums)

#     count = 1
#     longest = 1

#     for num in num_sets:
#         if num - 1 in num_sets:
#             count = count + 1
#             longest = max(longest, count)
#             temp = num + 1
#             while temp in num_sets:
#                 count = count + 1
#                 longest = max(longest, count)
#                 temp = temp + 1
#             count = 1
#         else:
#             count = 1

#     return longest

# nums = [100,4,200,1,3,2]

# print(longest_numbers(nums))



# a = 3
# b = None

# print(a >= None)


# def searchRange(nums, target):
#     first_target = -1
#     left = 0
#     right = len(nums)-1

#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             first_target = mid
#             break
#         if target > nums[mid]:
#             left = mid + 1
#         elif target < nums[mid]:
#             right = mid - 1

#     print("mid="+str(mid))


#     left_index = -1
#     right_index = -1

#     if first_target != -1:
#         left_index = first_target
#         while target == nums[left_index]:
#             left_index -= 1
#             if left_index < 0 or left_index >= len(nums) or target != nums[left_index]:
#                 left_index += 1
#                 break


#         right_index = first_target
#         while target == nums[right_index]:
#             right_index += 1
#             if right_index < 0 or right_index >= len(nums) or target != nums[right_index]:
#                 right_index -= 1
#                 break

#         return [left_index, right_index]
#     else:
#         return [-1,-1]


# # Input: nums = [5,7,7,8,8,10], target = 8
# # Output: [3,4]

# nums = [5,7,7,8,8,10]
# target = 8

# print(searchRange(nums, target))

# num = 35
# print(int(num**0.5))

# def solution(str_arr):
#     dict = defaultdict(list)

#     for word in str_arr:
#         key = ''.join(sorted(word))
#         dict[key].append(word)

#     ans = []
#     for k in dict:
#         ans.append(dict[k])

#     return ans

# strs = ["eat","tea","tan","ate","nat","bat"]

# print(solution(strs))


# anagrams = {}

# if 'A' not in anagrams:
#     anagrams['A'] = []

# anagrams['A'].append(1)
# print(anagrams)

# from itertools import permutations

# word = "abc"
# my_dict = {}
# second_dict = defaultdict(bool)

# for p in permutations(word):
#     key = ''.join(p)
#     second_dict[key] = True
    #my_dict[key] = True

# bigString = "cbabcacabca"
# smallString = "abc"
# small_len = len(smallString)

# count = 0

# for i in range(len(bigString) - small_len + 1):  # +1 to include last window
#     window = bigString[i:i+small_len]  # fixed slicing
#     #if window in my_dict:  # safe dictionary lookup
#     if second_dict[window] == True:  # safe dictionary lookup
#         count += 1

# print(count)  # Output: 6



# def permutations(s):
#     if len(s) == 1:
#         print(f"Base case return: [{s}]")
#         return [s]

#     result = []
#     print(f"Permuting: {s}")
#     for i in range(len(s)):
#         rem = s[:i] + s[i+1:]
#         print(f"  Remaining: {rem}")
#         for perm in permutations(rem):
#             print(f"  Append: {s[i]} + {perm} = {s[i] + perm}")
#             result.append(s[i] + perm)
#     print(f"Return from {s}: {result}")
#     return result

# print(permutations("ab"))


print("hello")

prerequisites = [[1,0],[2,0]]

for a, b in prerequisites:
  print(a)
  print(b)
