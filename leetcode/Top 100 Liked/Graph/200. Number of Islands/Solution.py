from typing import List

from abc import ABC, abstractmethod

class SolutionInterface(ABC):
    @abstractmethod
    def numIslands(self, grid: List[List[str]]) -> int:
        pass


class Solution(SolutionInterface):
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # Handle empty grid edge case
            return 0

        count = 0
        self.maxRow = len(grid)
        self.maxColumn = len(grid[0])

        for i in range(self.maxRow):
            for j in range(self.maxColumn):
                if grid[i][j] == "1":  # Found an unvisited land cell
                    count += 1
                    self.dfs(i, j, grid)

        return count

    def dfs(self, i: int, j: int, grid: List[List[str]]) -> None:
        if not (0 <= i < self.maxRow and 0 <= j < self.maxColumn):
            return  # Out of bounds check
        if grid[i][j] == "0":
            return  # Already visited (water)

        grid[i][j] = "0"  # Mark as visited by sinking the island

        for (r, c) in self.directions:
            self.dfs(i + r, j + c, grid)



class Solution2(SolutionInterface):
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]  # left, up, right, down

        row_length = len(grid)           # Number of rows
        column_length = len(grid[0])     # Number of columns

        def dfs(x, y):
            if grid[x][y] == '0':
                return
            grid[x][y] = '0'

            for add_x, add_y in directions:
                new_x = x + add_x
                new_y = y + add_y
                if new_x < 0 or new_x >= row_length or new_y < 0 or new_y >= column_length:
                    continue
                dfs(new_x, new_y)

        count = 0
        for x in range(row_length):
            for y in range(column_length):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x, y)

        return count




test_cases = [
  ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1),
  ([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 3),
]

solutions = [Solution(), Solution2()]

for sol in solutions:
    print(f"\nTesting: {sol.__class__.__name__}")
    for i, (p1, expected) in enumerate(test_cases, 1):
        result = sol.numIslands(p1)
        if result == expected:
            print(f"  ({i}) passed")
        else:
            print(f"  ({i}) failed. Got {result}, expected {expected}")
