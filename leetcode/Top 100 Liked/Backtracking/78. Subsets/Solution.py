from typing import List
from collections import defaultdict
from abc import ABC, abstractmethod

class SolutionInterface(ABC):
    @abstractmethod
    def subsets(self, nums):
        pass

class Solution(SolutionInterface):
    def subsets(self, nums):
        result = []
        def back_tracking(current, start):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                back_tracking(current, i+1)
                current.pop()

        back_tracking([], 0)
        return sorted(result)


test_cases = [
    ([1,2,3], sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])),
    ([0], [[],[0]]),
]

solutions = [Solution()]

for sol in solutions:
    print(f"\nTesting: {sol.__class__.__name__}")
    for i, (p1, expected) in enumerate(test_cases, 1):
        result = sol.subsets(p1)
        if result == expected:
            print(f"  ({i}) passed")
        else:
            print(f"  ({i}) failed. Got {result}, expected {expected}")