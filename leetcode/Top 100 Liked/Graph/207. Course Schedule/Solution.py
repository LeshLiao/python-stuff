from typing import List
from collections import defaultdict

# Ref: https://www.youtube.com/watch?v=EgI5nU9etnU&ab_channel=NeetCode

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(list)
        for course, pre in prerequisites:
          graph[course].append(pre)

        # print(graph)

        visited = set()

        def dfs(node):
          if node in visited:
            return False
          if graph[node] == []:
            return True

          visited.add(node)

          for neighbor in graph[node]:
            # if neighbor not in visited:
            if dfs(neighbor) == False:
                return False

          visited.remove(node) # others subfunction will revisit it, so have to remove it.
          graph[node] = [] # To speed up
          return True

        for node in range(numCourses):
          if dfs(node) == False:
            return False

        return True

test_cases = [
  (2, [[1,0]], True),
  (2, [[0,1],[1,0]], False),
  (5, [[0,1],[0,2],[1,3],[1,4],[3,4]], True)
]

for i, (p1, p2, expected) in enumerate(test_cases, 1):
    sol = Solution()
    result = sol.canFinish(p1, p2)
    if (result == expected):
        print(f"({i}) passed")
    else:
        print(f"({i}) failed. Result:{result}")
