from collections import deque
from typing import List

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

      startColor = image[sr][sc]

      maxRow = len(image)
      maxColumn = len(image[0])

      # print(maxRow)
      # print(maxColumn)

      if startColor == color:  return image

      queue = [(sr,sc)]
      visited = set()

      while queue:
        r,c = queue.pop(0)

        if (r, c) not in visited:
          visited.add((r, c))

          if image[r][c] != color :
            image[r][c] = color

            for a, b in [(0,1),(0,-1),(-1,0),(1,0)]:
              newRow = a + r
              newCol = b + c
              if 0 <= newRow < maxRow and 0 <=  newCol < maxColumn:
                if image[newRow][newCol] == startColor:
                  queue.append((newRow,newCol))
      return image


test_cases = [
    # input                               # expected
    ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2,  [[2,2,2],[2,2,0],[2,0,1]]),
    ([[0,0,0],[0,0,0]], 1, 0, 2,          [[2, 2, 2], [2, 2, 2]]),
]

sol = Solution()
for i, (p1, p2, p3, p4, expected) in enumerate(test_cases, 1):
    result = sol.floodFill(p1, p2, p3, p4)
    assert result == expected
    print(f"test case {i} passed")





