from typing import List
from collections import defaultdict
from abc import ABC, abstractmethod

class SolutionInterface(ABC):
    @abstractmethod
    def wordBreak(self, s, wordDict):
        pass

class Solution(SolutionInterface):
    '''

        s          wordDict
    "leetcode", ["leet","code"]

    s=            l     e     e     t     c    o     d      e

                  j                       i

    dp[]         True False False False True False False False False

                                        s[j:i]

    '''
    def wordBreak(self, s, wordDict):
        wordDictSet = set(wordDict)

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDictSet:
                    dp[i] = True
                    break

        return dp[-1]

test_cases = [
    ("leetcode", ["leet","code"], True),
    ("applepenapple", ["apple","pen"], True),
    ("catsandog",["cats","dog","sand","and","cat"], False),
    ("ab",["a","b"], True),
    ("cars",["car","ca","rs"], True)
]

solutions = [Solution()]

for sol in solutions:
    print(f"\nTesting: {sol.__class__.__name__}")
    for i, (p1, p2, expected) in enumerate(test_cases, 1):
        result = sol.wordBreak(p1, p2)
        if result == expected:
            print(f"  ({i}) passed")
        else:
            print(f"  ({i}) failed. Got {result}, expected {expected}")