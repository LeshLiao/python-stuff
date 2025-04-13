from typing import List
from collections import defaultdict
from abc import ABC, abstractmethod

class SolutionInterface(ABC):
    @abstractmethod
    def lengthOfLIS(self, nums):
        pass

class Solution(SolutionInterface):
    '''
        < max(dp)>  i

        0, 1, 0, 3, 2, 3
    dp  1, 2, 1, 3, 3, 4
    i
    j
    '''
    def lengthOfLIS(self, nums):

        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            #print("i = "+ str(i))
            max_dp_index = -1
            max_dp_count = 0
            for j in range(i-1,-1,-1):
                #print("j = "+ str(j))

                if nums[i] > nums[j] and dp[j] > max_dp_count:
                    max_dp_count = dp[j]
                    max_dp_index = j

            if max_dp_index != -1:  # found bigger dp count
                dp[i] = dp[max_dp_index] + 1

        # print(dp)
        return max(dp)


test_cases = [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1),
]

solutions = [Solution()]

for sol in solutions:
    print(f"\nTesting: {sol.__class__.__name__}")
    for i, (p1, expected) in enumerate(test_cases, 1):
        result = sol.lengthOfLIS(p1)
        if result == expected:
            print(f"  ({i}) passed")
        else:
            print(f"  ({i}) failed. Got {result}, expected {expected}")