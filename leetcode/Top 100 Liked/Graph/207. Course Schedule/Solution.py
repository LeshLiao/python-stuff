from typing import List
from collections import defaultdict

# Ref: https://www.youtube.com/watch?v=EgI5nU9etnU&ab_channel=NeetCode

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(list)
        for course, pre in prerequisites:
          #graph[course].append(pre)
          graph[pre].append(course)
          # 0 -> 1
          # node(pre) -> neighbor(course)

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
    # 1. No prerequisites
    (3, [], True),
    # Explanation: All courses can be taken in any order.

    # 2. Linear dependency (chain)
    (4, [[1, 0], [2, 1], [3, 2]], True),
    # Explanation: One valid order is [0,1,2,3]

    # 3. Simple cycle
    (3, [[0, 1], [1, 2], [2, 0]], False),
    # Explanation: Cycle exists → cannot complete all courses

    # 4. Multiple components, one with a cycle
    (5, [[1, 0], [2, 3], [3, 2]], False),
    # Explanation: Component [2,3] has a cycle

    # 5. Multiple components, no cycles
    (5, [[1, 0], [2, 3]], True),
    # Explanation: All components are acyclic

    # 6. Self-dependency
    (2, [[0, 0]], False),
    # Explanation: Course 0 requires itself → invalid

    # 7. Large chain (no cycles)
    (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]], True),
    # Explanation: Long but valid dependency chain
]


for i, (p1, p2, expected) in enumerate(test_cases, 1):
    sol = Solution()
    result = sol.canFinish(p1, p2)
    if (result == expected):
        print(f"({i}) passed")
    else:
        print(f"({i}) failed. Result:{result}")
