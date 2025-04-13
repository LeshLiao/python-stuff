from typing import List
from collections import defaultdict

class Solution:
    def rob(self, nums):

        dp = [0] * len(nums)

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            dp[0] = nums[0]
            return dp[0]
        if len(nums) == 2:
            dp[1] = max(nums[0], nums[1])
            return dp[1]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # nums [2, 7, 9, 3, 1]
        # dp    2, 7, 2+9, 2+9, 2+9+1

        for i in range(2,len(nums)):
            do_rob = dp[i-2] + nums[i]
            do_not = dp[i-1]
            dp[i] = max(do_rob, do_not)

        return dp[-1]


test_cases = [
  ([1,2,3,1], 4),
  ([2,7,9,3,1], 12),
  ([2,1,1,2], 4)
]

for i, (p1, expected) in enumerate(test_cases, 1):
    sol = Solution()
    result = sol.rob(p1)
    if (result == expected):
        print(f"({i}) passed")
    else:
        print(f"({i}) failed. Result:{result}")
