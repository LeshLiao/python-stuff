from typing import List
from collections import defaultdict

from abc import ABC, abstractmethod

class SolutionInterface(ABC):
    @abstractmethod
    def climbStairs(self, n: int) -> int:
        pass


class Solution(SolutionInterface):
    """
    Using combinations:
        C(total_moves, num_ones) = total_moves! / (num_ones! * num_twos!)

    n = 5
    1 1 1 1 1 (1)
    2 1 1 1   4!/3!  (4x3x2x1)/(3x2x1) = (4)
    2 2 1    (3)

    """
    def climbStairs(self, n):

        def factorial(x):
            sum = 1
            for i in range(1,x+1):
                sum = sum * i
            return sum

        maximum_two = n // 2
        sum = 0

        for number_of_two in range(0,maximum_two+1):
            number_of_one = n - (number_of_two * 2)
            total_number = number_of_one + number_of_two
            sum += factorial(total_number) / factorial(number_of_one) / factorial(number_of_two)
        return sum



class SolutionFib(SolutionInterface):
    """
    This approach builds up a solution using the Fibonacci sequence:
        The number of ways to reach step `n` is the sum of the ways to reach steps `n-1` and `n-2`.
    """
    def climbStairs(self, n):

        dp = [0] * n

        # 1 2 3 5 8
        if n == 1:
            return 1

        if n == 2:
            return 2

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


test_cases = [
  (2, 2),
  (3, 3),
  (5, 8),
]

solutions = [Solution(), SolutionFib()]

for sol in solutions:
    print(f"\nTesting: {sol.__class__.__name__}")
    for i, (n, expected) in enumerate(test_cases, 1):
        result = sol.climbStairs(n)
        if result == expected:
            print(f"  ({i}) passed")
        else:
            print(f"  ({i}) failed. Got {result}, expected {expected}")